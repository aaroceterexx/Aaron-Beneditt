// Aaron Beneditt
let list=[];
let lastNewId=-1;
const rows= document.getElementById("rows");
const search= document.getElementById("search");
const sort= document.getElementById("sort");
const msg= document.getElementById("msg");
const form= document.getElementById("form");
const nameIn=document.getElementById("name");
const ageIn=document.getElementById("age");
const courseIn=document.getElementById("course");
const formMsg= document.getElementById("formMsg");

// Inicializa el sistema al cargar, activa evento y carga el JSON.
window.onload=()=> {
  loadJson();
  search.oninput= update;
  sort.onchange= update;
  form.onsubmit=(e)=> {
    e.preventDefault();
    addStudent();
  };
};
async function loadJson(){
  const res=await fetch("students.json");
  list=await res.json();
  update(); //carga la info del json
}
function update(){
  const q=search.value.toLowerCase().trim();
  let show= list.filter(s => s.name.toLowerCase().includes(q));
//le pone formato al texto, minusculas y quita espacios
  if(show.length=== 0){
    msg.textContent="**No results found**";
    msg.className="error";}
  else{
    msg.textContent= "Showing "+show.length+" students.";
    msg.className= "";
  }//sirve para quitar el estilo de error cuando ya no hay error
  if(sort.value=== "name"){
    show.sort((a,b)=> a.name.localeCompare(b.name));
  }//ordena de a-z
  if(sort.value=== "age"){
    show.sort((a,b)=> a.age-b.age);
  }//ordena por edad
  draw(show);
}
function draw(show){
  rows.innerHTML= "";
  for(let s of show){
    const tr=document.createElement("tr");
    tr.innerHTML=`
      <td>${s.id}</td>
      <td>${s.name}</td>
      <td>${s.age}</td>
      <td>${s.course}</td>
    `;//pal orden de la tabla
    if(s.id=== lastNewId){
      tr.className= "newRow";
      setTimeout(()=> { tr.className= ""; }, 1500);
    }//esta le pone un color distinto al estudiante nuevo
    rows.appendChild(tr);
  }
}
function addStudent(){
  const name= nameIn.value.trim();
  const ageStr= ageIn.value.trim();//arregla los valores  quitando espacio
  const course= courseIn.value.trim();
  if(name=== "" || ageStr=== "" || course=== ""){
    formMsg.textContent= "**You need to fill all of the fields**";
    formMsg.className= "error";
    return;}
  if(/\d/.test(name)){//pa evitr que tenga unumeros el nombre
    formMsg.textContent= "**Name CANNOT contain digits*";
    formMsg.className= "error";
    return;}
  const age=Number(ageStr);
  if(!Number.isFinite(age)){//se asegura que la edad sea un numero
    formMsg.textContent= "**Age MUST be a number**";
    formMsg.className= "error";
    return;}
let new_Id;
if(list.length=== 0) {
  new_Id= 1;}
  else{//logica pa crear un ID mas dependiendo de cuanto hay
  const ids= list.map(s=> s.id);
  const maxId= Math.max(...ids);
  new_Id= maxId+ 1;
  }
  list.push({
    id: new_Id,
    name: name, //agrega el nuevo objeto
    age: age,
    course: course
  });
  lastNewId= new_Id;
  nameIn.value= "";
  ageIn.value="";
  courseIn.value= "";
  formMsg.textContent= "**New Student ha been added**";
  formMsg.className= "";
  update();
}

