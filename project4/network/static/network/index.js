function clearEditView(postId) {
    // Remove textarea, save button and cancel button
    document.getElementById(`textarea_${postId}`).remove()
    document.getElementById(`save_${postId}`).remove()
    document.getElementById(`cancel_${postId}`).remove()

    // Show content, edit button and no of likes
    document.getElementById(`post_content_${postId}`).style.display = 'block';
    document.getElementById(`edit_${postId}`).style.display = 'inline-block';
    document.getElementById(`post_likes_${postId}`).style.display = 'block';

}


document.addEventListener('DOMContentLoaded', function () {

// Default 'Hoot' button disabled per lecture 5: 114:00 - https://youtu.be/x5trGVMKTdY?t=4442 
document.querySelector('#submit_hoot').disabled = true;
document.querySelector('#hoot').onkeyup = () => {
    if (document.querySelector('#hoot').value.length > 0) {
        document.querySelector('#submit_hoot').disabled = false;
    } else {
    document.querySelector('#submit_hoot').disabled = true;
    }
}
// Change 'Hoot' placeholder to random string from array
var all_placeholders  = ['Owl-gebra is hard.', 'Hoot there it is!', 'Hoot out to the universe!','Owl you need is love.','Create a Hoot!'];
const random = all_placeholders[~~(Math.random() * all_placeholders.length)]; 
console.log(random);

document.getElementById("hoot").placeholder = random;

//Function to play *bird sound upon "HOOT"
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
            // Update page without reload
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
// If the thing the user clicked is the edit button
if (element.id.startsWith('edit_')) {
            
    // Save necessary variables
    const editButton = element;
    const postId = editButton.dataset.id;
    const postText = document.getElementById(`post_content_${postId}`);

    // Adding prepopulated text area element
    let textArea = document.createElement('textarea');
    textArea.innerHTML = postText.innerHTML;
    textArea.id = `textarea_${postId}`;
    textArea.className = 'form-control';
    document.getElementById(`post_contentgroup_${postId}`).append(textArea);

    // Hiding text containing original content
    postText.style.display = 'none';

    // Hiding likes
    document.getElementById(`post_likes_${postId}`).style.display = 'none';

    // Remove edit button
    editButton.style.display = 'none';

    // Adding 'Cancel' button
    const cancelButton = document.createElement('button');
    cancelButton.innerHTML = 'Cancel';
    cancelButton.className = 'btn btn-outline-dark btn-sm';
    cancelButton.id = `cancel_${postId}`

    // Adding 'Save' button
    const saveButton = document.createElement('button');
    saveButton.innerHTML = 'Save';
    saveButton.className = 'btn green-button btn-sm mt-2 px-2';
    saveButton.id = `save_${postId}`

    // Add save button to DOM
    document.getElementById(`save_buttons_${postId}`).append(saveButton);

    // Event listener for when user clicks new 'Cancel' button
    cancelButton.addEventListener('click', function() {
        clearEditView(postId)
    })
    
    // Add cancel button to DOM
    document.getElementById(`post_headline_${postId}`).append(cancelButton)
    

    // Fetch request when the user clicks 'save' button
    saveButton.addEventListener('click', function() {
        
        textArea = document.getElementById(`textarea_${postId}`);
        
        // Make fetch request to update page without full reload
        fetch(`/edit_hoot/${postId}`, {
            method: 'POST',
            body: JSON.stringify({
                // Pass through the new content typed in the text area
                content: textArea.value,
            })
        })
        
        .then(response => {
            if (response.ok || response.status == 400) {
                return response.json()
            // Throws error for users who don't have permission (ie users not logged in)
            } else if(response.status === 404) {
                clearEditView(postId)
                
                // Hide edit button to prevent happening again
                editButton.style.display = 'none';

                // Creates validation message
                addValidationMessage("You are not authorised to do this", `post_contentgroup_${postId}`)

                // Rejects promise and throws error
                return Promise.reject('Error 404')

            } else {
                return Promise.reject('There has been an error: ' + response.status)
            } 
        })

        .then(result => {
            
            // If successful, load user's sent inbox
            if (!result.error) {
            
                // Sets on screen text to what the user edited
                postText.innerHTML = result.content;
                
                // Removes all edit fields and restores to normal view
                clearEditView(postId)
            } 
            else {
                clearEditView(postId)

                // Hide edit button to prevent happening again
                editButton.style.display = 'none';
                
                addValidationMessage(result.error, `post_contentgroup_${postId}`)
                // Add validation message
                /* const warningMessage = document.createElement('p');
                warningMessage.innerHTML = result.error;
                warningMessage.className = 'text-danger';
                
                // add validation message to DOM
                document.getElementById(`post_contentgroup_${postId}`).append(warningMessage); */
                
            }
        })
        .catch(error => {
            console.error(error);
        })
    })

}

        });
    
    // Bookmark Hoot
    
    /*
    // update post as -- 'edited' --
    = function  () {
        if (submit_edit) {
            const timeDiv = document.querySelector('#time_of_post')
            timeDiv.innerHTML = `
            <small class="text-muted" id="time_of_post">• <em>edited</em></small>
            `
        } else {
            const timeDiv = document.querySelector('#time_of_post')
            timeDiv.innerHTML = `
            <small class="text-muted" id="time_of_post">•{{ post.time|naturaltime }}</small>
            `
        }
       
    }
            */

