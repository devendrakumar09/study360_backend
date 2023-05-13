from django.contrib import admin
from .models import *
# Register your models here.

class AnswerAdmin(admin.StackedInline):
    model = Answers

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]

admin.site.register(MainCategory)
admin.site.register(Categories)
admin.site.register(Set)
admin.site.register(Queston,QuestionAdmin)
admin.site.register(Answers)
