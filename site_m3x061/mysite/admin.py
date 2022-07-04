from django.contrib import admin

# Register your models here.
from mysite.models import Subject, Student, Teacher


class SubjectAdmin(admin.ModelAdmin):
    pass
admin.site.register(Subject, SubjectAdmin)

class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student, StudentAdmin)

class TeacherAdmin(admin.ModelAdmin):
    pass
admin.site.register(Teacher, TeacherAdmin)
