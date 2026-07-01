from django.db import models


# ==========================
# USER PROFILE
# ==========================

class UserProfile(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    password = models.CharField(max_length=100)

    career_goal = models.CharField(
        max_length=100,
        default="Not Specified"
    )

    college = models.CharField(
        max_length=200,
        blank=True
    )

    department = models.CharField(
        max_length=100,
        blank=True
    )

    year = models.CharField(
        max_length=20,
        blank=True
    )

    github = models.URLField(blank=True)

    linkedin = models.URLField(blank=True)

    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


# ==========================
# CAREER ASSESSMENT
# ==========================

class CareerAssessment(models.Model):

    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE
    )

    interest = models.CharField(max_length=100)

    subject = models.CharField(max_length=100)

    work_style = models.CharField(max_length=100)

    language = models.CharField(max_length=100)

    maths = models.CharField(max_length=20)

    recommended_career = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.recommended_career}"


# ==========================
# CAREER ROADMAP
# ==========================

class CareerRoadmap(models.Model):

    career = models.CharField(max_length=100)

    step_number = models.IntegerField()

    step_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.career} - Step {self.step_number}"

# ==========================
# Skill Model
# ==========================

class Skill(models.Model):

    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE
    )

    skill_name = models.CharField(max_length=100)

    completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.skill_name}"

# ==========================
# Project Model
# ==========================

class Project(models.Model):

    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    github = models.URLField(blank=True)

    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# ==========================
# Certificate Model
# ==========================

class Certificate(models.Model):

    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    organization = models.CharField(max_length=200)

    issue_date = models.DateField()

    certificate_link = models.URLField(blank=True)

    def __str__(self):
        return self.title

# ==========================
# Interview Question Model
# ==========================

class InterviewQuestion(models.Model):

    career = models.CharField(max_length=100)

    difficulty = models.CharField(max_length=20)

    question = models.TextField()

    answer = models.TextField()

    def __str__(self):
        return f"{self.career} - {self.difficulty}"

class InterviewHistory(models.Model):

    career = models.CharField(max_length=100)

    score = models.IntegerField()

    status = models.CharField(max_length=50)

    interview_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.career} - {self.score}%"
