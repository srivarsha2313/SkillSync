import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *

import google.generativeai as genai
from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

from .models import InterviewHistory

from .models import (
    UserProfile,
    Skill,
    Project,
    Certificate,
    InterviewHistory
)

from rest_framework import viewsets

from .models import Skill, Project, Certificate

from .serializers import (
    SkillSerializer,
    ProjectSerializer,
    CertificateSerializer
)

# ==========================================
# REGISTER
# ==========================================

@csrf_exempt
def register(request):

    if request.method != "POST":
        return JsonResponse({
            "success": False,
            "message": "Only POST request allowed"
        })

    try:

        data = json.loads(request.body)

        UserProfile.objects.create(
            name=data["name"],
            email=data["email"],
            password=data["password"],
            career_goal=data.get("career_goal", "Not Specified")
        )

        return JsonResponse({
            "success": True,
            "message": "Registration Successful"
        })

    except Exception as e:

        return JsonResponse({
            "success": False,
            "message": str(e)
        })


# ==========================================
# LOGIN
# ==========================================

@csrf_exempt
def login(request):

    if request.method != "POST":
        return JsonResponse({
            "success": False,
            "message": "Only POST request allowed"
        })

    try:

        data = json.loads(request.body)

        user = UserProfile.objects.get(
            email=data["email"],
            password=data["password"]
        )

        return JsonResponse({
            "success": True,
            "name": user.name,
            "email": user.email,
            "career_goal": user.career_goal
        })

    except UserProfile.DoesNotExist:

        return JsonResponse({
            "success": False,
            "message": "Invalid Email or Password"
        })

    except Exception as e:

        return JsonResponse({
            "success": False,
            "message": str(e)
        })


# ==========================================
# GET PROFILE
# ==========================================

@csrf_exempt
def get_profile(request, email):

    try:

        user = UserProfile.objects.get(email=email)

        return JsonResponse({

            "success": True,

            "name": user.name,
            "email": user.email,
            "career_goal": user.career_goal,
            "college": user.college,
            "department": user.department,
            "year": user.year,
            "github": user.github,
            "linkedin": user.linkedin,
            "bio": user.bio

        })

    except UserProfile.DoesNotExist:

        return JsonResponse({

            "success": False,
            "message": "User not found"

        })

    except Exception as e:

        return JsonResponse({

            "success": False,
            "message": str(e)

        })


# ==========================================
# UPDATE PROFILE
# ==========================================

@csrf_exempt
def update_profile(request):

    if request.method != "POST":

        return JsonResponse({

            "success": False,
            "message": "Only POST request allowed"

        })

    try:

        data = json.loads(request.body)

        email = data.get("email", "").strip()

        user = UserProfile.objects.filter(email=email).first()

        if not user:

            return JsonResponse({

                "success": False,
                "message": "User not found"

            })

        user.career_goal = data.get("career_goal", "")
        user.college = data.get("college", "")
        user.department = data.get("department", "")
        user.year = data.get("year", "")
        user.github = data.get("github", "")
        user.linkedin = data.get("linkedin", "")
        user.bio = data.get("bio", "")

        user.save()

        return JsonResponse({

            "success": True,
            "message": "Profile Updated Successfully"

        })

    except Exception as e:

        return JsonResponse({

            "success": False,
            "message": str(e)

        })


# ==========================================
# CAREER ASSESSMENT
# ==========================================

@csrf_exempt
def career_assessment(request):

    if request.method != "POST":

        return JsonResponse({

            "success": False,
            "message": "Only POST request allowed"

        })

    try:

        data = json.loads(request.body)

        user = UserProfile.objects.get(email=data["email"])

        interest = data["interest"]
        subject = data["subject"]
        work_style = data["work_style"]
        language = data["language"]
        maths = data["maths"]

        # ======================================
        # Smart Recommendation Logic
        # ======================================

        career = "Software Engineer"

        if interest == "Artificial Intelligence":

            if language == "Python" and maths == "Yes":
                career = "AI Engineer"
            else:
                career = "Machine Learning Engineer"

        elif interest == "Data Science":

            if maths == "Yes":
                career = "Data Scientist"
            else:
                career = "Data Analyst"

        elif interest == "Web Development":

            if language == "JavaScript":
                career = "Full Stack Developer"
            else:
                career = "Frontend Developer"

        elif interest == "Cyber Security":

            career = "Cyber Security Engineer"

        elif interest == "Cloud Computing":

            career = "Cloud Engineer"

        CareerAssessment.objects.create(

            user=user,

            interest=interest,
            subject=subject,
            work_style=work_style,
            language=language,
            maths=maths,

            recommended_career=career

        )

        # Update user's career goal automatically
        user.career_goal = career
        user.save()

        return JsonResponse({

            "success": True,

            "career": career,

            "message": "Assessment Completed Successfully"

        })

    except UserProfile.DoesNotExist:

        return JsonResponse({

            "success": False,

            "message": "User not found"

        })

    except Exception as e:

        return JsonResponse({

            "success": False,

            "message": str(e)

        })
# ==========================================
# GET CAREER ROADMAP
# ==========================================

def get_roadmap(request, career):

    try:

        roadmap = CareerRoadmap.objects.filter(
            career=career
        ).order_by("step_number")

        roadmap_data = []

        for step in roadmap:

            roadmap_data.append({
                "step_number": step.step_number,
                "step_name": step.step_name
            })

        return JsonResponse({
            "success": True,
            "career": career,
            "roadmap": roadmap_data
        })

    except Exception as e:

        return JsonResponse({
            "success": False,
            "message": str(e)
        })
# ==========================================
# ADD SKILL
# ==========================================

@csrf_exempt
def add_skill(request):

    if request.method != "POST":

        return JsonResponse({
            "success": False,
            "message": "Only POST request allowed"
        })

    try:

        data = json.loads(request.body)

        user = UserProfile.objects.get(email=data["email"])

        Skill.objects.create(

            user=user,

            skill_name=data["skill_name"]

        )

        return JsonResponse({

            "success": True,

            "message": "Skill Added Successfully"

        })

    except Exception as e:

        return JsonResponse({

            "success": False,

            "message": str(e)

        })


# ==========================================
# GET SKILLS
# ==========================================

def get_skills(request, email):

    try:

        user = UserProfile.objects.get(email=email)

        skills = Skill.objects.filter(user=user)

        data = []

        for skill in skills:

            data.append({

                "id": skill.id,

                "skill_name": skill.skill_name,

                "completed": skill.completed

            })

        return JsonResponse({

            "success": True,

            "skills": data

        })

    except Exception as e:

        return JsonResponse({

            "success": False,

            "message": str(e)

        })


# ==========================================
# UPDATE SKILL
# ==========================================

@csrf_exempt
def update_skill(request):

    if request.method != "POST":

        return JsonResponse({

            "success": False,

            "message": "Only POST request allowed"

        })

    try:

        data = json.loads(request.body)

        skill = Skill.objects.get(id=data["id"])

        skill.completed = data["completed"]

        skill.save()

        return JsonResponse({

            "success": True,

            "message": "Skill Updated"

        })

    except Exception as e:

        return JsonResponse({

            "success": False,

            "message": str(e)

        })


# ==========================================
# DELETE SKILL
# ==========================================

@csrf_exempt
def delete_skill(request):

    if request.method != "POST":

        return JsonResponse({

            "success": False,

            "message": "Only POST request allowed"

        })

    try:

        data = json.loads(request.body)

        skill = Skill.objects.get(id=data["id"])

        skill.delete()

        return JsonResponse({

            "success": True,

            "message": "Skill Deleted"

        })

    except Exception as e:

        return JsonResponse({

            "success": False,

            "message": str(e)

        })
# ==========================================
# DASHBOARD
# ==========================================

def dashboard(request, email):

    try:

        user = UserProfile.objects.get(email=email)

        assessment = CareerAssessment.objects.filter(
            user=user
        ).last()

        skills = Skill.objects.filter(user=user).count()

        completed_skills = Skill.objects.filter(
            user=user,
            completed=True
        ).count()

        career = user.career_goal

        readiness = 20

        if assessment:
            readiness += 20

        if skills > 0:
            readiness += 20

        return JsonResponse({

            "success": True,

            "name": user.name,

            "career_goal": career,

            "skills": skills,

            "completed_skills": completed_skills,

            "projects": 0,

            "certificates": 0,

            "career_readiness": readiness

        })

    except Exception as e:

        return JsonResponse({

            "success": False,

            "message": str(e)

        })
# ==========================================
# ADD PROJECT
# ==========================================

@csrf_exempt
def add_project(request):

    if request.method != "POST":
        return JsonResponse({
            "success": False,
            "message": "Only POST request allowed"
        })

    try:

        data = json.loads(request.body)

        user = UserProfile.objects.get(email=data["email"])

        Project.objects.create(

            user=user,

            title=data["title"],

            description=data["description"],

            github=data.get("github", ""),

            completed=False

        )

        return JsonResponse({

            "success": True,

            "message": "Project Added Successfully"

        })

    except Exception as e:

        return JsonResponse({

            "success": False,

            "message": str(e)

        })


# ==========================================
# GET PROJECTS
# ==========================================

def get_projects(request, email):

    try:

        user = UserProfile.objects.get(email=email)

        projects = Project.objects.filter(user=user)

        data = []

        for project in projects:

            data.append({

                "id": project.id,

                "title": project.title,

                "description": project.description,

                "github": project.github,

                "completed": project.completed

            })

        return JsonResponse({

            "success": True,

            "projects": data

        })

    except Exception as e:

        return JsonResponse({

            "success": False,

            "message": str(e)

        })


# ==========================================
# UPDATE PROJECT
# ==========================================

@csrf_exempt
def update_project(request):

    if request.method != "POST":

        return JsonResponse({

            "success": False,

            "message": "Only POST request allowed"

        })

    try:

        data = json.loads(request.body)

        project = Project.objects.get(id=data["id"])

        project.completed = data["completed"]

        project.save()

        return JsonResponse({

            "success": True,

            "message": "Project Updated"

        })

    except Exception as e:

        return JsonResponse({

            "success": False,

            "message": str(e)

        })


# ==========================================
# DELETE PROJECT
# ==========================================

@csrf_exempt
def delete_project(request):

    if request.method != "POST":

        return JsonResponse({

            "success": False,

            "message": "Only POST request allowed"

        })

    try:

        data = json.loads(request.body)

        project = Project.objects.get(id=data["id"])

        project.delete()

        return JsonResponse({

            "success": True,

            "message": "Project Deleted"

        })

    except Exception as e:

        return JsonResponse({

            "success": False,

            "message": str(e)

        })
# ==========================================
# ADD CERTIFICATE
# ==========================================

@csrf_exempt
def add_certificate(request):

    if request.method != "POST":
        return JsonResponse({
            "success": False,
            "message": "Only POST request allowed"
        })

    try:

        data = json.loads(request.body)

        user = UserProfile.objects.get(email=data["email"])

        Certificate.objects.create(
            user=user,
            title=data["title"],
            organization=data["organization"],
            issue_date=data["issue_date"],
            certificate_link=data.get("certificate_link", "")
        )

        return JsonResponse({
            "success": True,
            "message": "Certificate Added Successfully"
        })

    except Exception as e:

        return JsonResponse({
            "success": False,
            "message": str(e)
        })


# ==========================================
# GET CERTIFICATES
# ==========================================

def get_certificates(request, email):

    try:

        user = UserProfile.objects.get(email=email)

        certificates = Certificate.objects.filter(user=user)

        data = []

        for certificate in certificates:

            data.append({
                "id": certificate.id,
                "title": certificate.title,
                "organization": certificate.organization,
                "issue_date": str(certificate.issue_date),
                "certificate_link": certificate.certificate_link
            })

        return JsonResponse({
            "success": True,
            "certificates": data
        })

    except Exception as e:

        return JsonResponse({
            "success": False,
            "message": str(e)
        })


# ==========================================
# DELETE CERTIFICATE
# ==========================================

@csrf_exempt
def delete_certificate(request):

    if request.method != "POST":
        return JsonResponse({
            "success": False,
            "message": "Only POST request allowed"
        })

    try:

        data = json.loads(request.body)

        certificate = Certificate.objects.get(id=data["id"])

        certificate.delete()

        return JsonResponse({
            "success": True,
            "message": "Certificate Deleted"
        })

    except Exception as e:

        return JsonResponse({
            "success": False,
            "message": str(e)
        })
# ==========================================
# Resume Model
# ==========================================

class Resume(models.Model):

    user = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE
    )

    phone = models.CharField(max_length=20)

    address = models.CharField(max_length=300)

    objective = models.TextField()

    skills = models.TextField()

    education = models.TextField()

    projects = models.TextField()

    certifications = models.TextField()

    languages = models.TextField()

    hobbies = models.TextField()

    def __str__(self):
        return self.user.name
# ==========================================
# SAVE / UPDATE RESUME
# ==========================================

@csrf_exempt
def save_resume(request):

    if request.method != "POST":

        return JsonResponse({
            "success": False,
            "message": "Only POST request allowed"
        })

    try:

        data = json.loads(request.body)

        user = UserProfile.objects.get(email=data["email"])

        Resume.objects.update_or_create(

            user=user,

            defaults={

                "phone": data["phone"],
                "address": data["address"],
                "objective": data["objective"],
                "skills": data["skills"],
                "education": data["education"],
                "projects": data["projects"],
                "certifications": data["certifications"],
                "languages": data["languages"],
                "hobbies": data["hobbies"]

            }

        )

        return JsonResponse({

            "success": True,

            "message": "Resume Saved Successfully"

        })

    except Exception as e:

        return JsonResponse({

            "success": False,

            "message": str(e)

        })


# ==========================================
# GET RESUME
# ==========================================

def get_resume(request, email):

    try:

        user = UserProfile.objects.get(email=email)

        resume = Resume.objects.get(user=user)

        return JsonResponse({

            "success": True,

            "phone": resume.phone,
            "address": resume.address,
            "objective": resume.objective,
            "skills": resume.skills,
            "education": resume.education,
            "projects": resume.projects,
            "certifications": resume.certifications,
            "languages": resume.languages,
            "hobbies": resume.hobbies

        })

    except Resume.DoesNotExist:

        return JsonResponse({

            "success": False,

            "message": "Resume not found"

        })

    except Exception as e:

        return JsonResponse({

            "success": False,

            "message": str(e)

        })

# ==========================================
# GET INTERVIEW QUESTIONS
# ==========================================

def get_interview_questions(request, career):

    try:

        questions = InterviewQuestion.objects.filter(career=career)

        data = []

        for q in questions:

            data.append({

                "id": q.id,

                "difficulty": q.difficulty,

                "question": q.question,

                "answer": q.answer

            })

        return JsonResponse({

            "success": True,

            "questions": data

        })

    except Exception as e:

        return JsonResponse({

            "success": False,

            "message": str(e)

        })

from django.http import JsonResponse
import json

def generate_interview_questions(request):

    career = request.GET.get("career")

    difficulty = request.GET.get("difficulty", "Medium")

    if not career:
        return JsonResponse({
            "success": False,
            "message": "Career is required."
        })

    prompt = f"""
Generate 10 interview questions for a {career}.

Difficulty: {difficulty}

Return ONLY valid JSON.

Format:

[
  {{
    "question":"...",
    "answer":"..."
  }}
]

Do not include markdown.
Do not include explanation.
Only JSON.
"""

    try:

        response = model.generate_content(prompt)

        text = response.text.strip()

        # Remove markdown if AI returns it
        text = text.replace("```json", "").replace("```", "").strip()

        questions = json.loads(text)

        return JsonResponse({
            "success": True,
            "questions": questions
        })

    except Exception as e:

        return JsonResponse({
            "success": False,
            "message": str(e)
        })



from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def evaluate_answer(request):

    InterviewHistory.objects.create(
    career=career,
    score=int(result["score"].split("/")[0]) * 10,
    status="Completed"
)


    if request.method != "POST":
        return JsonResponse({
            "success": False,
            "message": "POST request required."
        })

    try:

        data = json.loads(request.body)

        question = data.get("question")
        student_answer = data.get("student_answer")
        career = data.get("career")

        prompt = f"""
You are an expert technical interviewer.

Career: {career}

Interview Question:
{question}

Student Answer:
{student_answer}

Evaluate the answer.

Return ONLY valid JSON.

Format:

{{
    "score":"8/10",
    "feedback":"Explain what the student did well and what can be improved.",
    "model_answer":"Provide the ideal answer in 4-6 sentences."
}}

Do not return markdown.
Only JSON.
"""

        response = model.generate_content(prompt)

        text = response.text.strip()

        text = text.replace("```json","").replace("```","").strip()

        result = json.loads(text)

        return JsonResponse({
            "success": True,
            "result": result
        })

    except Exception as e:

        return JsonResponse({
            "success": False,
            "message": str(e)
        })

# ==========================================
# AI Job Recommendation
# ==========================================

@csrf_exempt
def generate_job_recommendations(request):

    if request.method != "GET":
        return JsonResponse({
            "success": False,
            "message": "GET request required."
        })

    career = request.GET.get("career")
    experience = request.GET.get("experience", "Student")

    if not career:
        return JsonResponse({
            "success": False,
            "message": "Career is required."
        })

    prompt = f"""
You are an AI Career Advisor.

Generate EXACTLY 5 job recommendations.

Career:
{career}

Experience Level:
{experience}

These recommendations should be suitable for students, freshers, and internship seekers.

Return ONLY valid JSON.

Format:

[
  {{
    "company":"Google",
    "role":"AI Engineer Intern",
    "location":"Bangalore",
    "salary":"₹8-12 LPA",
    "skills":["Python","TensorFlow","SQL"],
    "reason":"Suitable for students with AI and Python knowledge.",
    "apply_link":"https://careers.google.com/"
  }}
]

Rules:

1. Return ONLY JSON.
2. No markdown.
3. No explanations.
4. Generate exactly 5 jobs.
"""

    try:

        response = model.generate_content(prompt)

        text = response.text.strip()

        text = text.replace("```json", "").replace("```", "").strip()

        jobs = json.loads(text)

        return JsonResponse({
            "success": True,
            "jobs": jobs
        })

    except Exception as e:

        return JsonResponse({
            "success": False,
            "message": str(e)
        })

from django.http import JsonResponse

def placement_score(request):

    # Demo: first user
    user = UserProfile.objects.first()

    if not user:
        return JsonResponse({
            "success": False,
            "message": "No users found."
        })

    # Count completed records
    skill_count = Skill.objects.filter(
        user=user,
        completed=True
    ).count()

    project_count = Project.objects.filter(
        user=user,
        completed=True
    ).count()

    certificate_count = Certificate.objects.filter(
        user=user
    ).count()

    latest_interview = InterviewHistory.objects.order_by(
        "-interview_date"
    ).first()

    interview_score = (
        latest_interview.score
        if latest_interview
        else 0
    )

    # Convert counts into percentages
    skills = min(skill_count * 20, 100)

    projects = min(project_count * 25, 100)

    certificates = min(certificate_count * 20, 100)

    resume = 100

    assessment = 85

    interview = interview_score

    overall = round(
        assessment * 0.20 +
        skills * 0.20 +
        projects * 0.15 +
        resume * 0.15 +
        interview * 0.20 +
        certificates * 0.10
    )

    if overall >= 85:
        status = "Excellent"

    elif overall >= 70:
        status = "Good"

    elif overall >= 50:
        status = "Average"

    else:
        status = "Needs Improvement"

    return JsonResponse({

        "success": True,

        "overall": overall,

        "status": status,

        "assessment": assessment,

        "skills": skills,

        "projects": projects,

        "resume": resume,

        "interview": interview,

        "certificates": certificates,

        "skill_count": skill_count,

        "project_count": project_count,

        "certificate_count": certificate_count

    })


from django.http import JsonResponse

def interview_history(request):

    history = InterviewHistory.objects.order_by("-interview_date")

    data = []

    for item in history:

        data.append({
            "career": item.career,
            "score": item.score,
            "status": item.status,
            "date": item.interview_date.strftime("%d-%m-%Y %H:%M")
        })

    return JsonResponse({
        "success": True,
        "history": data
    })

# ==========================================
# AI Career Advisor
# ==========================================

@csrf_exempt
def career_advisor(request):

    if request.method != "POST":

        return JsonResponse({
            "success": False,
            "message": "POST request required."
        })

    try:

        data = json.loads(request.body)

        question = data.get("question")

        if not question:

            return JsonResponse({
                "success": False,
                "message": "Question is required."
            })

        prompt = f"""
You are SkillSync AI Career Advisor.

Your job is to guide students regarding:

- Career Guidance
- Skills
- Interview Preparation
- Resume
- Projects
- Certifications
- Job Preparation

Student Question:

{question}

Give a professional answer.

Maximum 200 words.

Do not use markdown.
"""

        response = model.generate_content(prompt)

        return JsonResponse({

            "success": True,

            "answer": response.text

        })

    except Exception as e:

        return JsonResponse({

            "success": False,

            "message": str(e)

        })


class SkillViewSet(viewsets.ModelViewSet):

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer



class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer



class CertificateViewSet(viewsets.ModelViewSet):

    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

