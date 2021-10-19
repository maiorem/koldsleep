from django.db import models

# Create your models here.
class Board(models.Model) :
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    cdate = models.DateTimeField()

    def __str__ (self) :
        return self.title