import datetime
import pytz

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name

    def total_time(self):
        if self.entry_set.count() > 0:
            entries = [e.duration() for e in self.entry_set.all()]
            entries = [e for e in entries if type(e) == datetime.timedelta]
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
        return "Entry of Project {}, {} ago.".format(self.project.name,ago - datetime.timedelta(microseconds=ago.microseconds))
    
    def duration(self):
        duration = self.end_time - self.start_time
        return duration - datetime.timedelta(microseconds=duration.microseconds)
