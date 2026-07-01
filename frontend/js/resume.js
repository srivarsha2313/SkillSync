
// ============================================
// SkillSync Resume Builder
// Part 1
// ============================================

const API_URL = "http://127.0.0.1:8000/api";

// ============================================
// Load Resume
// ============================================

async function loadResume() {

    let user = JSON.parse(localStorage.getItem("loggedInUser"));

    if (!user) {

        alert("Please login first");

        window.location.href = "login.html";

        return;

    }

    try {

        const response = await fetch(
            `${API_URL}/resume/${user.email}/`
        );

        const result = await response.json();

        if (result.success) {

            document.getElementById("phone").value = result.phone;
            document.getElementById("address").value = result.address;
            document.getElementById("objective").value = result.objective;
            document.getElementById("skills").value = result.skills;
            document.getElementById("education").value = result.education;
            document.getElementById("projects").value = result.projects;
            document.getElementById("certifications").value = result.certifications;
            document.getElementById("languages").value = result.languages;
            document.getElementById("hobbies").value = result.hobbies;

        }

    }

    catch (error) {

        console.log(error);

    }

    

}


// ============================================
// Preview Resume
// ============================================

function previewResume() {

    let user = JSON.parse(localStorage.getItem("loggedInUser"));

    if (!user) {

        alert("Please Login");

        return;

    }

    let preview = document.getElementById("preview");

    preview.style.display = "block";

    preview.innerHTML = `

        <h2>${user.name}</h2>

        <hr>

        <p><b>Email:</b> ${user.email}</p>

        <p><b>Phone:</b> ${document.getElementById("phone").value}</p>

        <p><b>Address:</b> ${document.getElementById("address").value}</p>

        <br>

        <h3>🎯 Career Objective</h3>

        <p>${document.getElementById("objective").value}</p>

        <br>

        <h3>💻 Skills</h3>

        <p>${document.getElementById("skills").value}</p>

        <br>

        <h3>🎓 Education</h3>

        <p>${document.getElementById("education").value}</p>

        <br>

        <h3>📂 Projects</h3>

        <p>${document.getElementById("projects").value}</p>

        <br>

        <h3>🏆 Certifications</h3>

        <p>${document.getElementById("certifications").value}</p>

        <br>

        <h3>🌍 Languages</h3>

        <p>${document.getElementById("languages").value}</p>

        <br>

        <h3>🎨 Hobbies</h3>

        <p>${document.getElementById("hobbies").value}</p>

    `;

}



// ============================================
// Download Resume as PDF
// ============================================

function downloadResume() {

    previewResume();

    const resume = document.getElementById("preview");

    const options = {

        margin: 0.5,

        filename: "SkillSync_Resume.pdf",

        image: {

            type: "jpeg",

            quality: 1

        },

        html2canvas: {

            scale: 2

        },

        jsPDF: {

            unit: "in",

            format: "a4",

            orientation: "portrait"

        }

    };

    html2pdf().set(options).from(resume).save();

}


// ============================================
// Print Resume
// ============================================

function printResume() {

    previewResume();

    let content = document.getElementById("preview").innerHTML;

    let printWindow = window.open("", "_blank");

    printWindow.document.write(`

        <html>

        <head>

            <title>Resume</title>

            <style>

                body{

                    font-family:Poppins,sans-serif;

                    margin:40px;

                }

                h2{

                    color:#4F46E5;

                }

                h3{

                    margin-top:20px;

                }

            </style>

        </head>

        <body>

            ${content}

        </body>

        </html>

    `);

    printWindow.document.close();

    printWindow.print();

}


