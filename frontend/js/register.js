// ---------- REGISTER ----------

async function registerUser(event) {

    event.preventDefault();


    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let careerGoal = document.getElementById("careerGoal").value;


    if (!name || !email || !password) {

        alert("Please fill all fields");
        return;

    }


    try {

        const response = await fetch(
            "http://127.0.0.1:8000/api/register/",
            {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify({

                    name: name,
                    email: email,
                    password: password,
                    career_goal: careerGoal


                })

            }
        );


        const result = await response.json();


        console.log(result);


        if (result.success === true) {


            alert(result.message);


            window.location.href = "login.html";


        }

        else {


            alert(result.message || "Registration Failed");


        }


    }


    catch(error) {


        console.error("Error:", error);


        alert("Server Connection Failed");


    }

}