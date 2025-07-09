from django.db import models

class Student(models.Model):
    fullname = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.CharField(max_length=255)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.fullname

    class Meta:
        db_table = 'students'
        managed = True
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

