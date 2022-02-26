from django.contrib import admin

from .models import *


@admin.register(Quiz)
class QuizModel(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionModel(admin.ModelAdmin):
    pass


@admin.register(Option)
class OptionModel(admin.ModelAdmin):
    pass


@admin.register(QuizResult)
class QuizResultModel(admin.ModelAdmin):
    pass
