document.addEventListener('DOMContentLoaded', function () {


    document.querySelector('#poop').submitHandler() 
            console.log('hiii')
            

        
    

    // Edit likes
    document.querySelectorAll('.like').forEach(btn => {
        btn.onclick = function () {
           fetch('/likepost', {
               method: 'PUT',
               body: JSON.stringify({toggle_like: true, post_id: btn.dataset.postid})
           })
            .then(response => response.json())
            .then(result => {
                if (result.error) {
                    console.log(`Error liking post: ${result.error}`);
                } else {
                    console.log("Likes updated")

                    let likes_count = document.querySelector(`#likes${btn.dataset.postid}`)

                    if (parseInt(result.likes_num) < parseInt(likes_count.innerHTML)) {
                        btn.innerHTML = "<i class='fa-light fa-heart'></i>"
                    } else if (parseInt(result.likes_num) > parseInt(likes_count.innerHTML)) {
                        btn.innerHTML = "<div style='color: rgb(32, 120, 244);'><i class='fa-light fa-heart'></i></div>"
                    }
                    document.querySelector(`#likes${btn.dataset.postid}`).innerHTML = result.likes_num
                }
            })
        }
    })

});