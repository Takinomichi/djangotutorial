from django.contrib import admin
from .models import Question, Choice

# admin.site.register(Question)
# admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    # extra = 3 means that 3 empty Choice objects will be displayed in the admin interface
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #fields = ["pub_date", "question_text"]
    # create fieldsets to group the fields in the admin interface
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date Information", {"fields": ['pub_date']}),
    ]
    # This will display the choices next to the questions creation form
    inlines = [ChoiceInline]
    # Show a list of questions with their fields
    list_display = ("question_text", "pub_date", "was_published_recently")
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)