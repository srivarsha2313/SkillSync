let questions = [];
let currentIndex = 0;

// Load questions from Django API
async function loadQuestions() {

    const career = document.getElementById("career").value;

    try {

        const response = await fetch(
            `http://127.0.0.1:8000/api/interview/${encodeURIComponent(career)}/`
        );

        const data = await response.json();

        if (data.success && data.questions.length > 0) {

            questions = data.questions;
            currentIndex = 0;

            showQuestion();

        } else {

            alert("No interview questions found for this career.");

        }

    } catch (error) {

        console.error(error);
        alert("Unable to connect to the server.");

    }

}

// Display current question
function showQuestion() {

    const q = questions[currentIndex];

    document.getElementById("difficulty").innerText = q.difficulty;

    document.getElementById("question").innerText = q.question;

    document.getElementById("answer").innerText = q.answer;

    document.getElementById("answer").classList.add("hidden");

    updateProgress();

}

// Show / Hide Answer
function toggleAnswer() {

    document
        .getElementById("answer")
        .classList.toggle("hidden");

}

// Next Question
function nextQuestion() {

    if (currentIndex < questions.length - 1) {

        currentIndex++;
        showQuestion();

    } else {

        alert("🎉 You have completed all interview questions!");

    }

}

// Previous Question
function previousQuestion() {

    if (currentIndex > 0) {

        currentIndex--;
        showQuestion();

    }

}

// Update Progress Bar
function updateProgress() {

    const percentage =
        ((currentIndex + 1) / questions.length) * 100;

    document.getElementById("progress").style.width =
        percentage + "%";

    document.getElementById("progressText").innerText =
        `Question ${currentIndex + 1} / ${questions.length}`;

}