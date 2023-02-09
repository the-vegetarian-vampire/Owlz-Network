
![owl-xtr-small copy 2](https://user-images.githubusercontent.com/105305546/217709262-47f916ed-bc1e-4686-82bc-e787f8720dab.png)
## Owlz!

Project 4 for Harvard's CS50w Web Programming with Python and JavaScript.

📹 `Youtube:` ...TBD

### Overview:
A Twitter-like social media site for making posts and following users.

### Specifications:
Built with `Javascript`, `Python`, `Django`, `HTML/CSS`, `Bootstrap`, and `SQLite`. 

The site also makes use of [Django's](https://docs.djangoproject.com/en/4.1/ref/contrib/humanize/) `humanize` template filters via `naturaltime`.

The site also makes use of `pagination`: displaying 10 posts per page. If there are more than ten posts, a “Next” button takes the user to the next page of posts. If not on the first page, “Previous” takes the user to the previous page.

## Posts
Users can `create` text-based posts, `like` posts, and `edit` posts. The user can view all posts under the `All Posts` tab.

To `like`: users click the thumbs-up icon and the page is updated via `JavaScript` asynchronously.

To `edit`: users click `“Edit”` on their own posts, make specified changes, and click `"Save"`.

## Following
Users can follow other users, and view only those users they are following under the `following` tab.

## Profile
Users have a profile page, and clicking on `Profile` takes a user to the specified user's profile displaying: number of `followers` and `posts` of the specified user. 
