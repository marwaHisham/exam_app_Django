from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Exam
from .models import Chapter
from .models import Course
from .models import Teacher
admin.site.register(Question)
admin.site.register(Exam)
admin.site.register(Course)
admin.site.register(Chapter)
admin.site.register(Teacher)