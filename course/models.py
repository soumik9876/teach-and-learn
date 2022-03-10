from django.contrib.auth import get_user_model
from django.db import models

from accounts.models import Teacher, Student
from core.models import BaseModel
from django.utils.translation import gettext as _

User = get_user_model()


def rename_and_save(instance, filename):
    return f"{instance.course.title}/{instance.course.video_set.count() + 1}{filename}"


class CourseCategory(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("Category title"))
    description = models.TextField(verbose_name=_("Category description"), blank=True)

    class Meta:
        verbose_name = _("Course category")
        verbose_name_plural = _("Course categories")

    def __str__(self):
        return self.title


class Course(BaseModel):
    image_link = models.URLField(max_length=255, verbose_name=_("Course Image Link"), null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name=_("Course title"), unique=True)
    description = models.TextField(verbose_name=_("Course description"), blank=True)
    price = models.FloatField(verbose_name=_("Course price"), default=0)
    teacher = models.ManyToManyField(Teacher, verbose_name=_("Course teachers"))
    student = models.ManyToManyField(Student, verbose_name=_("Enrolled students"), blank=True)
    category = models.ForeignKey(CourseCategory, verbose_name=_("Course category"), on_delete=models.SET_NULL,
                                 null=True, blank=True)

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")

    def __str__(self):
        return f"{self.title}"


class Video(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("Video title"))
    watched_by = models.ManyToManyField(Student, verbose_name="Watched by", blank=True)
    content_creator = models.ManyToManyField(Teacher, verbose_name=_("Content creators"))
    course = models.ForeignKey(Course, verbose_name=_("Course"), on_delete=models.CASCADE)
    video_file = models.FileField(upload_to=rename_and_save, null=True, blank=True)
    video_link = models.URLField(max_length=255, verbose_name=_("Course Image Link"), null=True, blank=True)

    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")

    def __str__(self):
        return f"{self.course.title} - {self.title}"


class Blog(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("Blog Title"))
    writers = models.ManyToManyField(Teacher, verbose_name=_("Writers"))
    course = models.ForeignKey(Course, verbose_name=_("Course"), on_delete=models.CASCADE)
    content = models.TextField(verbose_name=_("Blog content"), blank=True)

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")

    def __str__(self):
        return self.title


class Comment(BaseModel):
    content = models.TextField(verbose_name=_("Comment content"))
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    video = models.ForeignKey(Video, on_delete=models.SET_NULL, null=True, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return f"{self.user} - {self.content[:10]}"
