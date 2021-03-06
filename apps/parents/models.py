from django.db import models
from students.models import Student

# Create your models here.

SEX = (
        (True, 'male'),
        (False, 'female')
    )


class Parent(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='parent/photo', blank=True, null=True)
    sex = models.BooleanField(choices=SEX, default=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=11, null=True)
    enabled = models.BooleanField(default=True)
    student = models.ForeignKey(Student, related_name='s_parent', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '家长'
        verbose_name_plural = verbose_name
        unique_together = ('id', 'student')