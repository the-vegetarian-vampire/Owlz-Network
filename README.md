![owl-small](https://user-images.githubusercontent.com/105305546/220189470-607ad15d-6827-49a4-abe5-64d0ef588c29.png)

## Owlz! 
*"Create a Hoot!"*

Project 4 for Harvard's CS50w Web Programming with Python and JavaScript.

📹 `Youtube:` ...TBD

### Overview:
A social media site for making posts, following users, and `hooting` out to the world!

-----

### Specifications:
Built with `Javascript`, `Python`, `Django`, `HTML/CSS`, `Bootstrap`, and `SQLite`. 

The site makes use of [Django's](https://docs.djangoproject.com/en/4.1/ref/contrib/humanize/) `humanize` template filters via `naturaltime` as well as [pagination](https://docs.djangoproject.com/en/4.1/topics/pagination/): displaying 10 posts per page. If there are more than ten posts, `“Next”` takes the user to the next page of posts. If not on the first page, `“Back”` takes the user to the previous page; additionally uses Django's [File uploads](https://docs.djangoproject.com/en/4.1/topics/http/file-uploads/) feature for creating a profile image.

-----

### To Run:
1. Pip install `Django`
2. In the terminal, cd into the project4 directory.
3. Run `python3 manage.py makemigrations network` to make migrations for the network app.
4. Run `python3 manage.py migrate` to apply migrations to the database.
5. Run `python3 manage.py runserver` to start the Django web server and visit the website in the browser.

## Login/Register
Users can `Register` an account with a specified password and `Login`.

<img width="1200" alt="Screen Shot 2023-02-18 at 11 12 51 PM" src="https://user-images.githubusercontent.com/105305546/219921840-2386bb05-9c16-41b8-9288-519405ff54e0.png">

## Hoots!
Users can create text-based posts, in this case `HOOTS!`, users can `like` and `edit` [their own] hoots. The user can view all hoots under the `All Posts` tab.

To `like`: users click the :heart: icon and the page is updated via `JavaScript` asynchronously.

To `edit`: users click `“Edit”` on their own posts, make specified changes, and click `"Save"`.

## Following
Users can follow other users, and view only users they are following under the `following` tab.

## Profile
Users have a profile page, clicking on `Profile` takes a user to the specified user's profile displaying: number of `posts`, `followers` and `following` of the specified user. 

## Data Models
