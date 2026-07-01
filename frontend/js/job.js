async function generateJobs(){

    const career = document.getElementById("career").value;
    const experience = document.getElementById("experience").value;

    const loading = document.getElementById("loading");
    const container = document.getElementById("jobsContainer");

    loading.style.display = "block";
    container.innerHTML = "";

    try{

        const response = await fetch(
            `http://127.0.0.1:8000/api/generate-jobs/?career=${encodeURIComponent(career)}&experience=${encodeURIComponent(experience)}`
        );

        const data = await response.json();

        loading.style.display = "none";

        if(!data.success){

            container.innerHTML="<h3>Unable to generate recommendations.</h3>";
            return;

        }

        data.jobs.forEach(job=>{

            let skillsHTML="";

            job.skills.forEach(skill=>{

                skillsHTML+=`<span class="skill">${skill}</span>`;

            });

            container.innerHTML+=`

            <div class="job-card">

                <h2>${job.company}</h2>

                <p><strong>Role:</strong> ${job.role}</p>

                <p><strong>Location:</strong> ${job.location}</p>

                <p><strong>Salary:</strong> ${job.salary}</p>

                <div class="skills">

                    ${skillsHTML}

                </div>

                <p>${job.reason}</p>

                <a
                    href="${job.apply_link}"
                    target="_blank"
                    class="apply-btn">

                    Apply Now

                </a>

            </div>

            `;

        });

    }

    catch(error){

        loading.style.display="none";

        container.innerHTML="<h3>Server Error.</h3>";

        console.log(error);

    }

}