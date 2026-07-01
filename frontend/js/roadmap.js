
const career =
localStorage.getItem("recommendedCareer");

document.getElementById("careerTitle").innerHTML =
career + " Roadmap";

const roadmapData={

"AI Engineer":[
"Learn Python",
"NumPy",
"Pandas",
"Statistics",
"Machine Learning",
"Deep Learning",
"TensorFlow",
"Build 5 AI Projects",
"Resume Preparation",
"Interview Preparation"
],

"Data Scientist":[
"Python",
"SQL",
"Pandas",
"Statistics",
"Power BI",
"Machine Learning",
"Projects",
"Resume",
"Interview",
"Apply Jobs"
],

"Full Stack Developer":[
"HTML",
"CSS",
"JavaScript",
"React",
"Django",
"MySQL",
"Projects",
"GitHub",
"Resume",
"Interview"
],

"Cyber Security Engineer":[
"Networking",
"Linux",
"Python",
"Ethical Hacking",
"Kali Linux",
"OWASP",
"Projects",
"Resume",
"Interview",
"Jobs"
],

"Cloud Engineer":[
"AWS",
"Azure",
"Docker",
"Kubernetes",
"Linux",
"Terraform",
"Projects",
"Resume",
"Interview",
"Jobs"
]

};

let completed=0;

let list=document.getElementById("roadmapList");

roadmapData[career].forEach(step=>{

let div=document.createElement("div");

div.className="step";

div.innerHTML="⬜ "+step;

div.onclick=function(){

if(!div.classList.contains("completed")){

div.classList.add("completed");

div.innerHTML="✅ "+step;

completed++;

}

else{

div.classList.remove("completed");

div.innerHTML="⬜ "+step;

completed--;

}

updateProgress();

};

list.appendChild(div);

});

function updateProgress(){

let percent=(completed/roadmapData[career].length)*100;

document.getElementById("progressBar").style.width=
percent+"%";

document.getElementById("progressText").innerHTML=
completed+" / "+roadmapData[career].length+
" Skills Completed";
}

updateProgress();
