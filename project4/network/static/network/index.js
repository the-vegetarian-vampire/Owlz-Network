document.addEventListener('DOMContentLoaded', function () {

// Default 'Hoot' button disabled: per lecture 5: 114:00 - https://youtu.be/x5trGVMKTdY?t=4442 
document.querySelector('#submit').disabled = true;
document.querySelector('#hoot').onkeyup = () => {
    if (document.querySelector('#hoot').value.length > 0) {
        document.querySelector('#submit').disabled = false;
    } else {
    document.querySelector('#submit').disabled = true;
    }
}

// Change 'Hoot' placeholder to random string from array
// var myArray = ['Owl sayz what?', 'Do you feel fly?', 'Hoot there it is!', 'Hoot out to the universe!'];
// const random = myArray[Math.floor(Math.random() * myArray.length)]; 
// console.log(random, myArray[random]);


// Change 'Tweet' placeholder to random string from array
var myArray = ['Tweet here!', 'Feel the Tweet?', 'Tweet there it is!'];
const random = myArray[Math.floor(Math.random() * myArray.length)]; 
console.log(random, myArray[random]);


document.querySelector('#placeholder') = () => {
    random
 }

});