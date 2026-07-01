from django.contrib import admin

from .models import (
    UserProfile,
    CareerAssessment,
    CareerRoadmap,
    Skill,
    Project,
    Certificate,
    InterviewQuestion,
    InterviewHistory,
)

admin.site.register(UserProfile)
admin.site.register(CareerAssessment)
admin.site.register(CareerRoadmap)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Certificate)
admin.site.register(InterviewQuestion)
admin.site.register(InterviewHistory)