// ---------- ADD SKILL ----------


async function addSkill(event){

    event.preventDefault();


    let user = JSON.parse(localStorage.getItem("user"));


    let skill = document.getElementById("skill").value;



    if(!skill){

        alert("Enter skill");
        return;

    }



    const response = await fetch(
        "http://127.0.0.1:8000/api/skills/add/",
        {


            method:"POST",


            headers:{

                "Content-Type":"application/json"

            },


            body:JSON.stringify({

                email:user.email,

                skill_name:skill

            })


        }
    );



    const result = await response.json();



    if(result.success){


        alert("Skill Added");


        document.getElementById("skill").value="";


    }


    else{


        alert(result.message);


    }


}