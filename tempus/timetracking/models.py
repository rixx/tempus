from django.db import models

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

class Entry(models.Model):
    project = models.ForeignKey(Project)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return "Entry for {}, {} ago".format(self.project, datetime.datetime.now() - self.end_time)
