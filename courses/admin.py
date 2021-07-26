from django.contrib import admin

from courses.models import Course, HomeworkTask, Solution


class SolutionInline(admin.TabularInline):
    model = Solution
    extra = 0


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)


@admin.register(HomeworkTask)
class HomeworkTaskAdmin(admin.ModelAdmin):
    inlines = [SolutionInline,]


# @admin.register(Solution)
# class SolutionAdmin(admin.ModelAdmin):
#     pass
