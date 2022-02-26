from django.db import models
from accounts.models import Teacher, Student
from core.models import BaseModel
from course.models import Course
from django.utils.translation import gettext as _


class Quiz(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("Quiz title"))
    description = models.TextField(verbose_name=_("Quiz description"), blank=True)
    course = models.ForeignKey(Course, verbose_name=_("Course"), on_delete=models.CASCADE)
    teacher = models.ManyToManyField(Teacher, verbose_name=_("Teacher"))

    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")

    def __str__(self):
        return f"{self.title} - {self.course.title}"


class Question(BaseModel):
    question = models.TextField(verbose_name=_("Question"))
    quiz = models.ManyToManyField(Quiz, verbose_name=_("Quiz"), blank=True)

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

    def __str__(self):
        return f"{self.question} - {self.quiz.title}"


class Option(BaseModel):
    option = models.TextField(verbose_name=_("option"))
    question = models.ForeignKey(Question, verbose_name=_("Question"), on_delete=models.CASCADE)
    is_correct = models.BooleanField(verbose_name=_("Is correct"), default=False)

    class Meta:
        verbose_name = _("Option")
        verbose_name_plural = _("Options")

    def __str__(self):
        return f"{self.question} - {self.option} - {self.is_correct}"


class QuizResult(BaseModel):
    got_marks = models.IntegerField(verbose_name=_("Got marks"), default=0)
    total_marks = models.IntegerField(verbose_name=_("Total marks"), default=0)
    student = models.ForeignKey(Student, verbose_name=_("Student"), on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, verbose_name=_("Quiz"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Quiz Result")
        verbose_name_plural = _("Quiz Results")

    def __str__(self):
        return f"{self.student.user.username} - {self.got_marks}/{self.total_marks}"

    def save(self, *args, **kwargs):
        self.total_marks = self.quiz.question_set.count()
        return super(QuizResult, self).save(*args, **kwargs)
