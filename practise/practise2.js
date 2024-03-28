// const fs = require("fs")

// let read = fs.readFileSync("text.txt","utf-8")
// read = read.replace("file","folder")
// fs.writeFileSync("newtext1.txt",read)
// console.log("New File created...")
// console.log(read)

var ourRequest = new XMLHttpRequest();

ourRequest.open('GET',"data.json");
ourRequest.onload = function(){
//  var ourData=ourRequest.responseText;
console.log(ourRequest.responseText);
}
ourRequest.send();
