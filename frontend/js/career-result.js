// ---------- CAREER RESULT ----------


let user = JSON.parse(localStorage.getItem("user"));



if(!user){

window.location.href="login.html";

}



async function loadCareer(){



try{


const response = await fetch(

`http://127.0.0.1:8000/api/roadmap/${user.career_goal}/`

);



const data = await response.json();



document.getElementById("careerName").innerHTML =
user.career_goal;




document.getElementById("careerDescription").innerHTML =

data.description || 
"Your personalized career path";





let roadmapBox =
document.getElementById("roadmap");



roadmapBox.innerHTML="";



if(data.steps){


data.steps.forEach(step=>{


roadmapBox.innerHTML +=

`
<p class="item">

${step}

</p>

`;


});


}






let skillsBox =
document.getElementById("skills");



skillsBox.innerHTML="";



if(data.skills){


data.skills.forEach(skill=>{


skillsBox.innerHTML +=

`

<span class="item">

${skill}

</span>

`;


});


}






let projectBox =
document.getElementById("projects");



projectBox.innerHTML="";



if(data.projects){


data.projects.forEach(project=>{


projectBox.innerHTML +=

`

<span class="item">

${project}

</span>

`;


});


}




}


catch(error){


console.log(error);


alert("Unable to load career result");


}



}





loadCareer();