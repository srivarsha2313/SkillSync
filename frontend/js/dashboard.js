const API_URL="http://127.0.0.1:8000/api";

async function loadDashboard(){

    let user=JSON.parse(localStorage.getItem("loggedInUser"));

    if(!user){

        window.location.href="login.html";

        return;

    }

    try{

        const response=await fetch(

            `${API_URL}/dashboard/${user.email}/`

        );

        const data=await response.json();

        if(data.success){

            document.getElementById("userName").innerText=data.name;

            document.getElementById("careerReadiness").innerText=data.career_readiness+"%";

            document.getElementById("skillCount").innerText=data.skills;

            document.getElementById("projectCount").innerText=data.projects;

            document.getElementById("certificateCount").innerText=data.certificates;

            document.getElementById("careerGoal").innerText=data.career_goal;

        }

    }

    catch(error){

        console.log(error);

    }

}

function logout(){

    localStorage.removeItem("loggedInUser");

    window.location.href="login.html";

}

async function loadPlacementScore(){

    try{

        const response = await fetch(
            "http://127.0.0.1:8000/api/placement-score/"
        );

        const data = await response.json();

        if(!data.success) return;

        document.getElementById("overallScore").innerText =
            data.overall + "%";

        document.getElementById("overallProgress").style.width =
            data.overall + "%";

        document.getElementById("placementStatus").innerText =
            data.status;

        document.getElementById("assessmentScore").innerText =
            data.assessment + "%";

        document.getElementById("skillsScore").innerText =
            data.skills + "%";

        document.getElementById("projectsScore").innerText =
            data.projects + "%";

        document.getElementById("resumeScore").innerText =
            data.resume + "%";

        document.getElementById("interviewScore").innerText =
            data.interview + "%";

        document.getElementById("certificateScore").innerText =
            data.certificates + "%";

    }

    catch(error){

        console.log(error);

    }

}

loadPlacementScore();

function loadAnalytics(){

    const ctx = document.getElementById("analyticsChart");

    new Chart(ctx, {

        type: "bar",

        data: {

            labels: [

                "Assessment",

                "Skills",

                "Projects",

                "Resume",

                "Interview",

                "Certificates"

            ],

            datasets: [

                {

                    label: "Progress",

                    data: [

                        85,

                        80,

                        90,

                        100,

                        88,

                        75

                    ],

                    backgroundColor: [

                        "#FF6B6B",

                        "#4ECDC4",

                        "#FFD93D",

                        "#6BCB77",

                        "#4D96FF",

                        "#9D4EDD"

                    ]

                }

            ]

        },

        options: {

            responsive:true,

            plugins:{

                legend:{

                    display:false

                }

            },

            scales:{

                y:{

                    beginAtZero:true,

                    max:100

                }

            }

        }

    });

}

loadAnalytics();