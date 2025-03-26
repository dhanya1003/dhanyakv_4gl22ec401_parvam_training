from django.db import models # type: ignore

# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=10, unique=True)
    branch = models.CharField(max_length=50)
    sem = models.IntegerField()
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=50)
    ISBA_number = models.IntegerField()

    def __str__(self):
        return self.name