const API = "http://127.0.0.1:8000/api";

// ===========================
// Add Certificate
// ===========================

async function addCertificate(){

    let user = JSON.parse(localStorage.getItem("loggedInUser"));

    let data = {

        email: user.email,

        title: document.getElementById("title").value,

        organization: document.getElementById("organization").value,

        issue_date: document.getElementById("issueDate").value,

        certificate_link: document.getElementById("certificateLink").value

    };

    const response = await fetch(API + "/certificates/add/",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify(data)

    });

    const result = await response.json();

    if(result.success){

        alert("Certificate Added Successfully");

        document.getElementById("title").value="";
        document.getElementById("organization").value="";
        document.getElementById("issueDate").value="";
        document.getElementById("certificateLink").value="";

        loadCertificates();

    }

    else{

        alert(result.message);

    }

}

// ===========================
// Load Certificates
// ===========================

async function loadCertificates(){

    let user = JSON.parse(localStorage.getItem("loggedInUser"));

    const response = await fetch(API + "/certificates/" + user.email + "/");

    const result = await response.json();

    let html = "";

    result.certificates.forEach(certificate=>{

        html += `

        <div class="certificate">

            <h3>${certificate.title}</h3>

            <p><b>Organization:</b> ${certificate.organization}</p>

            <p><b>Issue Date:</b> ${certificate.issue_date}</p>

            <p>

                <a href="${certificate.certificate_link}" target="_blank">

                    View Certificate

                </a>

            </p>

            <button class="delete-btn"

            onclick="deleteCertificate(${certificate.id})">

            Delete

            </button>

        </div>

        `;

    });

    document.getElementById("certificateList").innerHTML = html;

}

// ===========================
// Delete Certificate
// ===========================

async function deleteCertificate(id){

    await fetch(API + "/certificates/delete/",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            id:id
        })

    });

    loadCertificates();

}

