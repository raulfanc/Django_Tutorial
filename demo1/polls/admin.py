from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# class ChoiceInline(admin.StackedInline):  # have extra 3 choices for one question
#     model = Choice
#     extra = 3

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']  # can only have one of these, to control the option showing in admin page
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]    # add choices in the same page, usually array, or tuple

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)