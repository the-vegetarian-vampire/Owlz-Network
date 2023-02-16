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

// Change 'Hoot' placeholder to random string from array!
var all_placeholders  = ['Owl sayz what?', 'Do you feel fly?', 'Hoot there it is!', 'Hoot out to the universe!'];
const random = all_placeholders[Math.floor(Math.random() * all_placeholders.length)]; 
console.log(random, all_placeholders[random]);


document.getElementById("hoot").placeholder = random;

});