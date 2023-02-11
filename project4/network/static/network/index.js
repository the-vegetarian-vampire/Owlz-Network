document.addEventListener('DOMContentLoaded', function () {

    // By default 'Hoot' button should be disabled: again: per lecture 5: 114:00 - https://youtu.be/x5trGVMKTdY?t=4442 
    document.querySelector('#submit').disabled = true;

    document.querySelector('#hoot').onkeyup = () => {
        if (document.querySelector('#hoot').value.length > 0) {
            document.querySelector('#submit').disabled = false;
        } else {
        document.querySelector('#submit').disabled = true;
        }
    }

});