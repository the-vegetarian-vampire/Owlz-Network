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
var all_placeholders  = ['Owl-gebra is hard...', 'Hoot there it is!', 'Hoot out to the universe!','Owl you need is love.','Create a Hoot!'];
const random = all_placeholders[Math.floor(Math.random() * all_placeholders.length)]; 
console.log(random);

document.getElementById("hoot").placeholder = random;

});

// Updates no of likes for a given ID
function updateLikes(id, likes) {
    let likeCount = document.getElementById(`post_likecount_${id}`);

    likeCount.innerHTML = likes;
}

// Edit likes
document.addEventListener('DOMContentLoaded', function() {

    // Add event listener that listens for any clicks on the page
    document.addEventListener('click', event => {
        
        // Save the element the user clicked on
        const element = event.target;

        // If the user clicked on a like icon
        if (element.id.startsWith('post_likeicon_')) {
        
            // Save post ID from data in element
            let id = element.dataset.id;
            
            // Make fetch request to update page without full reload
            fetch(`/updatelike/${id}`, {
                method: "POST"
            })
            .then(function(response) {
                if (response.ok) {
                    return response.json()
                }
                // If response receives an error, rejects the promise and returns an error to the console.
                else {
                    return Promise.reject('There has been an error.')
                }
            }).then(function(data) {
                
                // Saving data from response
                const likes = data.likesCount;
                const likesPost = data.likesPost;

                // Like icon on page
                let likeIcon = document.getElementById(`post_likeicon_${id}`);
                
                // Update no of likes on page
                updateLikes(id, likes)

                // Updates like icon correctly according to whether user likes post or not
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

});