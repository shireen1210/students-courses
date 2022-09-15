from django.contrib import admin
from .models import Student
from .models import Course

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display=('cname','cid')
    search_fields=('cname','cid')
    list_filter=('cname','cid')

admin.site.register(Student)
admin.site.register(Course,CourseAdmin)
