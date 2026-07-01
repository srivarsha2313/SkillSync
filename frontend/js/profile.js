// =======================================
// SkillSync - Profile Page
// =======================================

// Backend URL
const API_URL = "http://127.0.0.1:8000/api";


// ===============================
// LOAD PROFILE
// ===============================

async function loadProfile() {

    // Get logged-in user
    let user = JSON.parse(localStorage.getItem("loggedInUser"));

    if (!user) {

        alert("Please login first");

        window.location.href = "login.html";

        return;
    }

    try {

        const response = await fetch(

            `${API_URL}/profile/${user.email}/`

        );

        const data = await response.json();

        if (data.success) {

            document.getElementById("name").value = data.name;
            document.getElementById("email").value = data.email;
            document.getElementById("careerGoal").value = data.career_goal;
            document.getElementById("college").value = data.college;
            document.getElementById("department").value = data.department;
            document.getElementById("year").value = data.year;
            document.getElementById("github").value = data.github;
            document.getElementById("linkedin").value = data.linkedin;
            document.getElementById("bio").value = data.bio;

        } else {

            alert(data.message);

        }

    } catch (error) {

        console.log(error);

        alert("Unable to load profile.");

    }

}



// ===============================
// SAVE PROFILE
// ===============================

async function saveProfile() {

    let profileData = {

        email: document.getElementById("email").value,

        career_goal: document.getElementById("careerGoal").value,

        college: document.getElementById("college").value,

        department: document.getElementById("department").value,

        year: document.getElementById("year").value,

        github: document.getElementById("github").value,

        linkedin: document.getElementById("linkedin").value,

        bio: document.getElementById("bio").value

    };

    console.log(profileData);

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/api/profile/update/",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(profileData)
            }
        );

        const result = await response.json();

        console.log(result);

        if (result.success) {

            alert("Profile Updated Successfully");

        } else {

            alert(result.message);

        }

    } catch (error) {

        console.log(error);

    }

}