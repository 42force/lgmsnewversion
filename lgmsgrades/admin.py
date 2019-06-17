from django.contrib import admin
from .models import Grade

# Register your models here.

class GradeCommentAdmin(admin.ModelAdmin):
    pass
class GradeAdmin(admin.ModelAdmin):
    list_display = ['grade', 'course', 'student', 'marking_period', 'override_final']
    list_filter = ['date', 'override_final']
    search_fields = ['student__fname', 'student__lname', 'course__fullname', 'course__shortname']
admin.site.register(Grade, GradeAdmin)
