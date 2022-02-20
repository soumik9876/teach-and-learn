from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from core.models import BaseModel


class User(AbstractUser):
    pass


class Teacher(BaseModel):
    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE)
    specialized_in = models.ManyToManyField("course.CourseCategory", verbose_name=_("Expertise in"), null=True,
                                            blank=True)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        return self.user.username


class Student(BaseModel):
    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.user.username
