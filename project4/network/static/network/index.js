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

// Update likes per post
function updateLikes(id, likes) {
    let likeCount = document.getElementById(`post_likecount_${id}`);

    likeCount.innerHTML = likes;
}
// Likes // @csrf_exempt via views.py
document.addEventListener('DOMContentLoaded', function() {
    document.addEventListener('click', event => {
        const element = event.target;

        // If the user clicked on a like icon
        if (element.id.startsWith('post_likeicon_')) {
        
            // Save post ID from data in element
            let id = element.dataset.id;
            
            // Fetch request to update page without full reload
            fetch(`/likepost/${id}`, {
                method: "POST"
            })
            .then(function(response) {
                if (response.ok) {
                    return response.json()
                }
                // If response receives an error, reject promise and return error.
                else {
                    return Promise.reject('There has been an error.')
                }
            }).then(function(data) {
                
                // Saving data from response
                const likes = data.likesCount;
                const likesPost = data.likesPost;

                // Like icon on page
                let likeIcon = document.getElementById(`post_likeicon_${id}`);
                
                // Update num of likes on page
                updateLikes(id, likes)

                // Update like icon
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

// edit post
document.querySelector('#save_edit').onclick = () => {
   console.log("onclick success")
}

// fetch(`/edit/{$id}`,)


});
