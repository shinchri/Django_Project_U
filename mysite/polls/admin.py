from django.contrib import admin
from .models import Question, Choice

''' 
# changes the order of fields
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
'''


# Choice objects are edited on the Question page
# to save spaces, use 'admin.TabularInline' instead of StackedInline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

    # by default, django displays str()
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # adds filter sidebar
    list_filter = ['pub_date']

    # adds searching
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)