// var createbtn = document.getElementById('createbutton')

// createbtn.addEventListener('click',function(e){
//     //     var newButton = document.createElement("button")
//     //     newButton.textContent="New Button"

// // newButton.classList.add("new-button")
// // document.body.appendChild(newButton)
// var main=document.createElement("p")
// main.innerText="This is the paragraph"
// main.classList.add("input-box")
// main.classList.add("button")
// document.body.appendChild(main)
// var container = document.querySelector(".notes-container")
// container.appendChild(main)
// var  btncreate = document.createElement("button")
// btncreate.innerText="DELETE"
// btncreate.classList.add(btncreate)
// main.appendChild(btncreate)
// alert("Note was created")

// btncreate.addEventListener('click',function(e){
//         alert("notes was deleted")
//     })
// // alert("button is clicked")
// })
// Function to update local storage with notes
function updateStorage() {
    localStorage.setItem("notes", notesContainer.innerHTML);
}

// Function to show notes from local storage
function showNotes() {
    notesContainer.innerHTML = localStorage.getItem("notes") || ""; // Load notes or empty string if no notes exist
}

// Call showNotes function when the page loads
window.onload = function() {
    showNotes();
};

const notesContainer = document.querySelector(".notes-container");
const createBtn = document.querySelector(".btn");

createBtn.addEventListener('click', function() {
    let inputBox = document.createElement("p");
    let img = document.createElement("img");
    inputBox.className = "input-box";
    inputBox.setAttribute("contenteditable", "true");
    img.src = "delete.png";
    notesContainer.appendChild(inputBox).appendChild(img);
});

notesContainer.addEventListener('click', function(e) {
    if (e.target.tagName === 'IMG') {
        e.target.parentElement.remove();
        updateStorage();
    }
    else if (e.target.tagName === "P") {
        notes = document.querySelectorAll(".input-box");
        notes.forEach(nt => {
            nt.onkeyup = function() {
                updateStorage();
            };
        });
    }
});
