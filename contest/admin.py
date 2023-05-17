from django.contrib import admin
from .models import *
# Register your models here.
class ContestInformationAdmin(admin.StackedInline):
    model = ContestInformation

class ContestAdmin(admin.ModelAdmin):
    inlines = [ContestInformationAdmin]

class AnswerAdmin(admin.StackedInline):
    model = Answers

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]


admin.site.register(Categories)
admin.site.register(Contest,ContestAdmin)
admin.site.register(Questions,QuestionAdmin)
admin.site.register(Subscribe)
