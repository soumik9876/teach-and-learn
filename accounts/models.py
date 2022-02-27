from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from core.models import BaseModel


class User(AbstractUser):
    def get_full_name(self):
        return super().get_full_name()

    def get_google_profile_data(self):
        social_account = SocialAccount.objects.filter(user=self).first()
        try:
            return social_account.extra_data
        except (AttributeError, Exception):
            return {}


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
