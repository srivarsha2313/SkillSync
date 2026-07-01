// =====================================
// SkillSync Career Assessment
// =====================================

const questions = [

    {
        question: "Which field interests you the most?",
        key: "interest",
        options: [
            "Artificial Intelligence",
            "Data Science",
            "Web Development",
            "Cyber Security",
            "Cloud Computing"
        ]
    },

    {
        question: "Which subject do you enjoy the most?",
        key: "subject",
        options: [
            "Programming",
            "Mathematics",
            "Statistics",
            "Networking"
        ]
    },

    {
        question: "What is your preferred work style?",
        key: "work_style",
        options: [
            "Individual",
            "Team"
        ]
    },

    {
        question: "Which programming language do you like most?",
        key: "language",
        options: [
            "Python",
            "Java",
            "C++",
            "JavaScript"
        ]
    },

    {
        question: "Do you enjoy Mathematics?",
        key: "maths",
        options: [
            "Yes",
            "No"
        ]
    }

];

let currentQuestion = 0;

let answers = {};


// =========================
// Load First Question
// =========================

window.onload = function () {

    loadQuestion();

};


// =========================
// Load Question
// =========================

function loadQuestion() {

    document.getElementById("questionNumber").innerText =
        currentQuestion + 1;

    document.getElementById("questionText").innerText =
        questions[currentQuestion].question;

    let progress =
        ((currentQuestion + 1) / questions.length) * 100;

    document.getElementById("progressBar").style.width =
        progress + "%";

    let container =
        document.getElementById("optionsContainer");

    container.innerHTML = "";

    questions[currentQuestion].options.forEach(option => {

        let div = document.createElement("div");

        div.className = "option";

        div.innerText = option;

        if (answers[questions[currentQuestion].key] === option) {

            div.classList.add("selected");

        }

        div.onclick = function () {

            document
                .querySelectorAll(".option")
                .forEach(opt => opt.classList.remove("selected"));

            div.classList.add("selected");

            answers[questions[currentQuestion].key] = option;

        };

        container.appendChild(div);

    });

    document.getElementById("prevBtn").style.display =
        currentQuestion === 0 ? "none" : "block";

    if (currentQuestion === questions.length - 1) {

        document.getElementById("nextBtn").innerText =
            "Submit";

    }

    else {

        document.getElementById("nextBtn").innerText =
            "Next";

    }

}


// =========================
// Next Question
// =========================

function nextQuestion() {

    let key = questions[currentQuestion].key;

    if (!answers[key]) {

        alert("Please select an option.");

        return;

    }

    if (currentQuestion < questions.length - 1) {

        currentQuestion++;

        loadQuestion();

    }

    else {

        submitAssessment();

    }

}


// =========================
// Previous Question
// =========================

function previousQuestion() {

    if (currentQuestion > 0) {

        currentQuestion--;

        loadQuestion();

    }

}
// =====================================
// Submit Assessment
// =====================================

const API_URL = "http://127.0.0.1:8000/api";

async function submitAssessment() {

    let user = JSON.parse(localStorage.getItem("loggedInUser"));

    if (!user) {

        alert("Please login first");

        window.location.href = "login.html";

        return;

    }

    let assessmentData = {

        email: user.email,

        interest: answers.interest,

        subject: answers.subject,

        work_style: answers.work_style,

        language: answers.language,

        maths: answers.maths

    };

    try {

        const response = await fetch(

            `${API_URL}/career-assessment/`,

            {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify(assessmentData)

            }

        );

        const result = await response.json();

        if(result.success){

            showResult(result.career);

        }

        else{

            alert(result.message);

        }

    }

    catch(error){

        console.log(error);

        alert("Server Error");

    }

}
// =====================================
// Show Result
// =====================================

function showResult(career){

    let description = "";

    let icon = "💼";

    let match = Math.floor(Math.random()*6)+95;

    switch(career){

        case "AI Engineer":

            icon="🤖";

            description="Design intelligent systems using Artificial Intelligence and Machine Learning.";

            break;

        case "Data Scientist":

            icon="📊";

            description="Analyze data and build predictive models for business decisions.";

            break;

        case "Full Stack Developer":

            icon="🌐";

            description="Develop complete web applications using frontend and backend technologies.";

            break;

        case "Cyber Security Engineer":

            icon="🔐";

            description="Protect organizations from cyber attacks and secure digital systems.";

            break;

        case "Cloud Engineer":

            icon="☁️";

            description="Build and manage scalable cloud infrastructure and services.";

            break;

        default:

            description="A promising career in Software Engineering.";

    }

    document.querySelector(".question").style.display="none";

    document.getElementById("optionsContainer").style.display="none";

    document.querySelector(".buttons").style.display="none";

    document.querySelector(".progress-container").style.display="none";

    document.querySelector(".progress-text").style.display="none";

    document.getElementById("result").style.display="block";

    document.getElementById("result").innerHTML=`

        <h2>🎉 Assessment Completed</h2>

        <h1>${icon} ${career}</h1>

        <h3>${match}% Career Match</h3>

        <p>${description}</p>

        <br>

        <button onclick="window.location.href='dashboard.html'">

            Back to Dashboard

        </button>

    `;

}