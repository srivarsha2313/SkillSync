const chatBox = document.getElementById("chatBox");
const questionInput = document.getElementById("question");

// Allow Enter key to send message
questionInput.addEventListener("keypress", function(event) {

    if (event.key === "Enter") {

        event.preventDefault();

        askAI();

    }

});

async function askAI() {

    const question = questionInput.value.trim();

    if (question === "") {

        alert("Please enter a question.");

        return;

    }

    // User message
    chatBox.innerHTML += `
        <div class="user-message">
            ${question}
        </div>
    `;

    questionInput.value = "";

    // Loading message
    chatBox.innerHTML += `
        <div class="ai-message loading" id="loadingMessage">
            🤖 Thinking...
        </div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/api/career-advisor/",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    question: question
                })
            }
        );

        const data = await response.json();

        document.getElementById("loadingMessage").remove();

        if (data.success) {

            chatBox.innerHTML += `
                <div class="ai-message">
                    ${data.answer}
                </div>
            `;

        } else {

            chatBox.innerHTML += `
                <div class="ai-message">
                    ❌ ${data.message}
                </div>
            `;

        }

    } catch (error) {

        document.getElementById("loadingMessage").remove();

        chatBox.innerHTML += `
            <div class="ai-message">
                ❌ Unable to connect to the server.
            </div>
        `;

        console.log(error);

    }

    chatBox.scrollTop = chatBox.scrollHeight;

}