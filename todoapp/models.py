from django.db import models


# models

class ToDo(models.Model):
    Title = models.CharField(max_length=100, blank=False)
    Description = models.TextField(blank = False)
    Date = models.DateField(blank=False)
    Category =models.CharField(max_length=40)
    Completed = models.BooleanField(default=False)


    def __str__(self):
        return self.Title
