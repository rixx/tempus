import datetime
import pytz

from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class BaseTimetracking(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40)
    slug_filter = {}

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = self.slugify()

        super().save(*args, **kwargs)

    def slugify(self, slug_field='slug'):
        max_length = self.__class__._meta.get_field(slug_field).max_length
        long_slug = slugify(self.name)
        slug = slugify(self.name)[:max_length]
        tries = 0
        owner_filter = {}

        if hasattr(self, 'owner'):
            owner_filter['owner'] = self.owner

        while self.__class__.objects.filter(slug=slug, **owner_filter).exists():
            tries += 1
            ending = '-{}'.format(tries)
            slug = '{}{}'.format(long_slug[:max_length-len(ending)], ending)

        return slug


class Category(BaseTimetracking):
    owner = models.ForeignKey(User)

    class Meta:
        unique_together = (('owner', 'name'), )


class Tag(BaseTimetracking):
    owner = models.ForeignKey(User)


class Project(BaseTimetracking):
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        unique_together = (('slug', 'category'),)

    def __str__(self):
        return '{} (Category {})'.format(self.name, self.category)

    def total_time(self):
        if self.entry_set.count() > 0:
            entries = [e.duration() for e in self.entry_set.all()]
            entries = [e for e in entries if isinstance(e, datetime.timedelta)]
            entries = sum(entries, datetime.timedelta())
            entries = entries - datetime.timedelta(microseconds=entries.microseconds)
            return entries
        else:
            return datetime.timedelta(0)

    def delta_to_last_edit(self):
        if self.entry_set.count() > 0:
            latest_entry = self.entry_set.latest('end_time')
            delta = datetime.datetime.now(pytz.timezone('Europe/Berlin')) - latest_entry.end_time
            return delta - datetime.timedelta(microseconds=delta.microseconds)
        else:
            return datetime.timedelta(0)


class Entry(models.Model):
    project = models.ForeignKey(Project)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        ago = datetime.datetime.now(pytz.timezone('Europe/Berlin')) - self.end_time
        return "Entry of Project {}, {} ago.".format(
            self.project.name,
            ago - datetime.timedelta(microseconds=ago.microseconds)
        )

    def duration(self):
        duration = self.end_time - self.start_time
        return duration - datetime.timedelta(microseconds=duration.microseconds)
