console.log("Welcome to notes app. This is app.js");
showNotes()
// If user adds a note, add it to the localStorage
let addBtn = document.getElementById("addBtn");
addBtn.addEventListener("click", function(e) {
  let addTxt = document.getElementById("addTxt");
  let notes = localStorage.getItem("notes");
  if (notes == null) {
    notesObj = [];
  } else {
    notesObj = JSON.parse(notes);
  }
  notesObj.push(addTxt.value);
  localStorage.setItem("notes", JSON.stringify(notesObj));
  addTxt.value = "";
//   console.log(notesObj);
  showNotes();
});

function showNotes(){
    let notes = localStorage.getItem("notes")
    if (notes == null ) {
       
        notesObj = [];
      } else {
        notesObj = JSON.parse(notes);
      }
       let html =""
       notesObj.forEach(function(element,index){
        html += ` <div class="noteCard my-2 mx-2 card" style="width: 18rem;">
        <div class="card-body">
            <h5 class="card-title">Note ${index + 1}</h5>
            <p class="card-text"> ${element}</p>
            <button id="${index}"onclick="deleteNote(this.id)" class="btn btn-primary">Delete Note</button>
        </div>
    </div>`;

       })
       let notesEle = document.getElementById('notes')
       if(notesObj.length!=0){
        notesEle.innerHTML=html
       }else{
        notesEle.innerHTML =`Nothing to show! Use "Add a Note" section to add your Notes` 
       }
}
function deleteNote(index) {
    let notesObj;

    let notes = localStorage.getItem("notes");
    if (notes == null) {
        notesObj = [];
    } else {
        notesObj = JSON.parse(notes);
    }

    console.log("Deleting note at index:", index);
    notesObj.splice(index, 1); // Remove the note at the specified index

    localStorage.setItem("notes", JSON.stringify(notesObj));

    showNotes(); // Update the displayed notes
}
