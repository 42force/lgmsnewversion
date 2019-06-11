from django.contrib import admin


from .models import Course, CourseEnrollment, CourseMeet, DaysOff, Day, MarkingPeriod
# Register your models here.

def copy(modeladmin, request, queryset):
    for object in queryset:
        object.copy_instance(request)

        
class CourseMeetInline(admin.TabularInline):
    model = CourseMeet
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    def render_change_form(self, request, context, *args, **kwargs):
        try:
            txt = "<h5>Students enrolled:</h5>"
            for student in context['original'].get_enrolled_students():
                txt += unicode(student) + '<br/>'
            txt = txt[:-5]
            context['adminform'].form.fields['teacher'].help_text += txt
        except:
            pass
        return super(CourseAdmin, self).render_change_form(request, context, args, kwargs)
    
    list_display = ['__unicode__', 'teacher', 'grades_link']
    search_fields = ['fullname', 'shortname', 'description', 'teacher__username']
    list_filter = ['teacher', 'level', 'marking_period', 'marking_period__school_year', 'active', 'graded', 'homeroom']
    inlines = [CourseMeetInline]
    actions = [copy]
    
    def save_model(self, request, obj, form, change):
        """Override save_model because django doesn't have a better way to access m2m fields"""
        obj.save()
        form.save_m2m()
        obj.save()
        

class DaysOffInline(admin.TabularInline):
    model = DaysOff
    extra = 1
    
admin.site.register(Day)
    
class CourseEnrollmentAdmin(admin.ModelAdmin):
    search_fields = ['course__fullname', 'user__username', 'user__fname', 'role']
    list_display = ['course', 'user', 'role', 'attendance_note']
admin.site.register(CourseEnrollment, CourseEnrollmentAdmin)

class MarkingPeriodAdmin(admin.ModelAdmin):
    inlines = [DaysOffInline]
admin.site.register(MarkingPeriod, MarkingPeriodAdmin)

admin.site.register(Course, CourseAdmin)
