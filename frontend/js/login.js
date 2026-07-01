// ---------- LOGIN ----------

async function loginUser(event) {

    event.preventDefault();

    let email = document.getElementById("loginEmail").value;
    let password = document.getElementById("loginPassword").value;

    try {

        const response = await fetch("http://127.0.0.1:8000/api/login/", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                email: email,
                password: password

            })

        });

        const result = await response.json();

        if (result.success) {

            localStorage.setItem("loggedInUser", JSON.stringify(result));

            alert("Login Successful 🎉");

            window.location.href = "dashboard.html";

        }

        else {

            alert(result.message);

        }

    }

    catch (error) {

        console.error(error);

        alert("Server Connection Failed");

    }

}