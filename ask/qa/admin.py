from django.contrib import admin
from qa.models import Question, Answer

# Register your models here.
# http://www.djangobook.com/en/2.0/chapter06.html
admin.site.register(Question)
admin.site.register(Answer)
