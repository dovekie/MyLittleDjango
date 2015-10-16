from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline): # sets up Choice to be edited within Question (three choices for each question)
	# above, TabularInline makes the choices into a table-like form
	# another option is StackedInline, which is less compressed.
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	# fields = ['pub_date', 'question_text'] # this determines the order in which the fields are displayed on the /admin/ page
	fieldsets = [ # this puts them in order and groups them by (Title, {'fields': ['list', 'of', 'fields'], 'classes': [html classes]})
		(None, {'fields': ['question_text']}),
		('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}) # 'collapse' makes a field hide itself until clicked
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently')


admin.site.register(Question, QuestionAdmin)

