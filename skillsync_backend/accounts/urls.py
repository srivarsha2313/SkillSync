from django.contrib import admin
from django.urls import path, include

from accounts.views import *


urlpatterns = [

    # ==========================
    # Admin
    # ==========================

    path('admin/', admin.site.urls),


    # ==========================
    # Authentication
    # ==========================

    path("register/", register),

    path("login/", login),


    # ==========================
    # Profile
    # ==========================

    path("profile/update/", update_profile),

    path("profile/<str:email>/", get_profile),


    # ==========================
    # Dashboard
    # ==========================

    path("dashboard/<str:email>/", dashboard),


    # ==========================
    # Career Assessment
    # ==========================

    path("career-assessment/", career_assessment),


    # ==========================
    # Roadmap
    # ==========================

    path("roadmap/<str:career>/", get_roadmap),


    # ==========================
    # Skills
    # ==========================

    path("skills/add/", add_skill),

    path("skills/<str:email>/", get_skills),

    path("skills/update/", update_skill),

    path("skills/delete/", delete_skill),



    # ==========================
    # Projects
    # ==========================

    path("projects/add/", add_project),

    path("projects/<str:email>/", get_projects),

    path("projects/update/", update_project),

    path("projects/delete/", delete_project),



    # ==========================
    # Certificates
    # ==========================

    path("certificates/add/", add_certificate),

    path("certificates/<str:email>/", get_certificates),

    path("certificates/delete/", delete_certificate),



    # ==========================
    # Resume
    # ==========================

    path("resume/save/", save_resume),

    path("resume/<str:email>/", get_resume),



    # ==========================
    # Interview
    # ==========================

    path("interview/<str:career>/", get_interview_questions),

    path("generate-interview/", generate_interview_questions),

    path("evaluate-answer/", evaluate_answer),



    # ==========================
    # AI / Jobs
    # ==========================

    path("generate-jobs/", generate_job_recommendations),

    path("placement-score/", placement_score),

    path("interview-history/", interview_history),

    path("career-advisor/", career_advisor),



    # ==========================
    # REST API
    # ==========================

    path("", include("accounts.api_urls")),


]