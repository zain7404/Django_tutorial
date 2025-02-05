from django.contrib import admin
from .models import courseType, courseReview, courseStore ,courseInstructor

class courseReviewInline(admin.TabularInline):
    model = courseReview
    extra = 2

class courseTypeAdmin(admin.ModelAdmin):
    list_display = ('name','type','date_added')
    inlines = [courseReviewInline]

class storeAdmin(admin.ModelAdmin):
    list_display = ('name','location')
    filter_horizontal = ('course_types',)

class instructorAdmin(admin.ModelAdmin):
    list_display = ('instructor_name','course','valid_until')

# Register your models here.
admin.site.register(courseType,courseTypeAdmin)
admin.site.register(courseStore,storeAdmin)
admin.site.register(courseInstructor,instructorAdmin)