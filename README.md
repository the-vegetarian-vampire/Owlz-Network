
![owl-xtr-small copy 2](https://user-images.githubusercontent.com/105305546/217709262-47f916ed-bc1e-4686-82bc-e787f8720dab.png)
## Owlz!

Project 4 for Harvard's CS50w Web Programming with Python and JavaScript.

📹 `Youtube:` ...TBD

### Overview:
A social media site for making posts, following users, and `hooting` out to the world!

-----

### Specifications:
Built with `Javascript`, `Python`, `Django`, `HTML/CSS`, `Bootstrap`, and `SQLite`. 

The site makes use of [Django's](https://docs.djangoproject.com/en/4.1/ref/contrib/humanize/) `humanize` template filters via `naturaltime` as well as [pagination](https://docs.djangoproject.com/en/4.1/topics/pagination/): displaying 10 posts per page. If there are more than ten posts, `“Next”` takes the user to the next page of posts. If not on the first page, `“Previous”` takes the user to the previous page.

-----

### To Run:
1. Pip install `Django`
2. In the terminal, cd into the project4 directory.
3. Run `python3 manage.py makemigrations network` to make migrations for the network app.
4. Run `python3 manage.py migrate` to apply migrations to the database.
5. Run `python3 manage.py runserver` to start the Django web server and visit the website in the browser.

## Login/Register
Users can `Register` an account with a specified password and `Login`.

<img width="1024" alt="Screen Shot 2023-02-09 at 3 37 12 PM" src="https://user-images.githubusercontent.com/105305546/217932690-69d72589-bcc5-4e3b-9210-2dc082d83435.png">

## Hoots! or Posts
Users can create text-based posts, in this case `HOOTS!`, users can `like` hoots, and `edit` hoots. The user can view all hoots/posts under the `All Posts` tab.

To `like` a hoot: users click the thumbs-up icon and the page is updated via `JavaScript` asynchronously.

To `edit` a hoot: users click `“Edit”` on their own posts, make specified changes, and click `"Save"`.

## Following
Users can follow other users, and view only those users they are following under the `following` tab.

## Profile
Users have a profile page, and clicking on `Profile` takes a user to the specified user's profile displaying: number of `followers` and `posts` of the specified user. 

## Data Models
