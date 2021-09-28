from django.db import models
from django import forms
from django.db.models.deletion import CASCADE

class Tag(models.Model):
    notas = models.CharField(max_length=40, default='oi')
        
    def __str__(self):
        return "{}".format(self.notas)

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE)

    def __str__(self):
        return '{}.{}'.format(self.id, self.title)