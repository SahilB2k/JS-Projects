var createbtn = document.getElementById('createbutton')

createbtn.addEventListener('click',function(e){
    //     var newButton = document.createElement("button")
    //     newButton.textContent="New Button"

// newButton.classList.add("new-button")
// document.body.appendChild(newButton)
var main=document.createElement("p")
main.innerText="This is the paragraph"
main.classList.add("input-box")
main.classList.add("button")
document.body.appendChild(main)
var container = document.querySelector(".notes-container")
container.appendChild(main)
var  btncreate = document.createElement("button")
btncreate.innerText="DELETE"
btncreate.classList.add(btncreate)
main.appendChild(btncreate)
alert("Note was created")

btncreate.addEventListener('click',function(e){
        alert("notes was deleted")
    })
// alert("button is clicked")
})
