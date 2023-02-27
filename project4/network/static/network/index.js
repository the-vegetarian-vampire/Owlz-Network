document.addEventListener('DOMContentLoaded', function () {

// Default 'Hoot' button disabled per lecture 5: 114:00 - https://youtu.be/x5trGVMKTdY?t=4442 
document.querySelector('#submit').disabled = true;
document.querySelector('#hoot').onkeyup = () => {
    if (document.querySelector('#hoot').value.length > 0) {
        document.querySelector('#submit').disabled = false;
    } else {
    document.querySelector('#submit').disabled = true;
    }
}
// Change 'Hoot' placeholder to random string from array
var all_placeholders  = ['Owl-gebra is hard.', 'Hoot there it is!', 'Hoot out to the universe!','Owl you need is love.','Create a Hoot!'];
const random = all_placeholders[Math.floor(Math.random() * all_placeholders.length)]; 
console.log(random);

document.getElementById("hoot").placeholder = random;

});

/* Function to play bird sound upon "HOOT"
let play = document.getElementById("submit");
function playSound(){
    let audio = new Audio("bird.mp3" is this right?);
    audio.play()
}
play.addEventListener("click", playSound)
*/

// Update likes per post
function updateLikes(id, likes) {
    let likeCount = document.getElementById(`post_likecount_${id}`);
    likeCount.innerHTML = likes;
}

// Likes // @csrf_exempt via views.py
document.addEventListener('DOMContentLoaded', function() {
    document.addEventListener('click', event => {
        const element = event.target;

        // Icon click
        if (element.id.startsWith('post_likeicon_')) {
            // Save post ID from data in element
            let id = element.dataset.id;
            // Fetch request to update page without reload
            fetch(`/likepost/${id}`, {
                method: "POST"
            })
            .then(function(response) {
                if (response.ok) {
                    return response.json()
                }
                else {
                    return Promise.reject('Error.')
                }
            }).then(function(data) {
                // Save data from response
                const likes = data.likesCount;
                const likesPost = data.likesPost;
                // Like icon on page
                let likeIcon = document.getElementById(`post_likeicon_${id}`);
                // Update num of likes
                updateLikes(id, likes)
                // update icon
                if (likesPost) {
                    likeIcon.className = 'likeicon fa-heart fas';
                } else {
                    likeIcon.className = 'likeicon fa-heart far';
                }
                
            }).catch(function(ex) {
                console.log("parsing failed", ex);
            });
        }
})

// Edit post

// fetch(`/edit/{$id}`,)


});

