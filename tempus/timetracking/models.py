from django.db import models
import datetime

class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class Tag(models.Model):
    tag_name = models.CharField(max_length=200)

    def __str__(self):
        return self.tag_name

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.project_name

    def total_time(self):
        if self.entry_set.count() > 0:
            return sum(e.duration() for e in self.entry_set.all())
        else:
            return datetime.timedelta(0)

    def delta_to_last_edit(self):
        if self.entry_set.count() > 0:
            latest_entry = self.entry_set.latest('end_time')
            return datetime.datetime.now() - latest_entry.end_time
        else:
            return datetime.timedelta(0)

class Entry(models.Model):
    project = models.ForeignKey(Project)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return "Entry for {}, {} ago".format(self.project, datetime.datetime.now() - self.end_time)
    
    def duration(self):
        return end_time - start_time
