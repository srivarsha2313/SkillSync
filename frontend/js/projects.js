const API="http://127.0.0.1:8000/api";

async function addProject(){

let user=JSON.parse(localStorage.getItem("loggedInUser"));

let data={

email:user.email,

title:document.getElementById("title").value,

description:document.getElementById("description").value,

github:document.getElementById("github").value

};

const response=await fetch(API+"/projects/add/",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify(data)

});

const result=await response.json();

if(result.success){

alert("Project Added");

loadProjects();

}

}

async function loadProjects(){

let user=JSON.parse(localStorage.getItem("loggedInUser"));

const response=await fetch(API+"/projects/"+user.email+"/");

const result=await response.json();

let html="";

result.projects.forEach(project=>{

html+=`

<div class="project">

<h3>${project.title}</h3>

<p>${project.description}</p>

<p><a href="${project.github}" target="_blank">GitHub</a></p>

<button onclick="deleteProject(${project.id})">

Delete

</button>

</div>

`;

});

document.getElementById("projectList").innerHTML=html;

}

async function deleteProject(id){

await fetch(API+"/projects/delete/",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

id:id

})

});

loadProjects();

}