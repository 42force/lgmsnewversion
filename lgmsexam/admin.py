
# Register your models here.


from django.contrib import admin
from .models import StandardCategory, StandardCategoryGrade, StandardTest, StandardTestResult
from rangefilter.filter import DateRangeFilter


#rangefilter.filter changed the rangefilter module
class StandardCategoryInline(admin.TabularInline):
    model = StandardCategory
    extra = 1
    
class StandardTestAdmin(admin.ModelAdmin):
    inlines = (StandardCategoryInline,)
admin.site.register(StandardTest, StandardTestAdmin)

class StandardCategoryGradeInline(admin.TabularInline):
    model = StandardCategoryGrade
    extra = 1
    
class StandardTestResultAdmin(admin.ModelAdmin):
    inlines = (StandardCategoryGradeInline,)
    list_display = ['student', 'test', 'date']
    list_filter = ['test', ('date', DateRangeFilter)]
    search_fields = ['student__fname', 'student__lname', 'test__name']
admin.site.register(StandardTestResult, StandardTestResultAdmin)