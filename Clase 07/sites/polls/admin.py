from django.contrib import admin

from polls.models import Question


@admin.register(Question)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'pub_date')