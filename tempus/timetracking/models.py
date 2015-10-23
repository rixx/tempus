from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=200)

class Tag(models.Model):
    tag_name = models.CharField(max_length=200)

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)

class Entry(models.Model):
    project = models.ForeignKey(Project)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
