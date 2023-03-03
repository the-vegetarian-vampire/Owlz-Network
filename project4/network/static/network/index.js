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

//Function to play *bird* sound upon "HOOT"
/*
let play = document.getElementById("submit");
function playSound(){
    let audio = new Audio('bird.mp3');
    audio.play()
}
play.addEventListener("click", playSound)
*/

});

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

// Edit Hoot
document.querySelectorAll('.btn-outline-dark').forEach(btn => {
    btn.onclick = function () {
        btn.style.display = 'none'
        console.log('Hoot number',btn.dataset.postid)
        
        // Hide delete button
        document.querySelector('#delete_button').style.display = 'none';

        let contentDiv = document.querySelector(`#post_content_${btn.dataset.postid}`)
        console.log()
        
            contentDiv.innerHTML =
            `<form id="edit-post-form" class="card-text" style="margin-top: 1rem; margin-bottom: 1.6rem">
                    <div class="form-group" style="margin-bottom: .7rem">
                        <textarea 
                            style="overflow: hidden; resize: none"
                            oninput='this.style.height = "";this.style.height = this.scrollHeight + "px"'
                            class="form-control"
                            id="edit-post-textarea">${contentDiv.innerHTML}</textarea>
                    </div>
                    <input type="submit" class="btn btn-warning post-submit btn-sm" value="Save" style="float: right; font-size: 11px; margin-right: 4px "/>
                    <button class="btn btn-outline-dark btn-sm" id="close_button" style="float: right; font-size: 11px; margin-right: .4rem">Close</button>
                </form>`

                
                document.querySelector('#close_button').onclick = function () {
                    btn.style.display = 'block' 
                }

                document.querySelector('#edit-post-form').onsubmit = () => {
                    // retrieve data entered by the user
                    const content = document.querySelector('#edit-post-textarea').value;
                    const post_id = btn.dataset.postid
                    console.log("edit value recieved")
                    fetch('/edit_hoot', {
                        method: 'PUT',
                        body: JSON.stringify({content, post_id})
                    })
                        .then(response => response.json())
                        .then(result => {
                            if (result.error) {
                                console.log(`Error editing post: ${result.error}`);
                            } else {
                                console.log(result.message)
                                contentDiv.innerHTML = content
                                btn.style.display = 'block'
                            }
                        })
                        .catch(err => {
                            console.log(err)
                        })
                    return false;
                }
    
    }
})

});


// Bookmark Hoot

