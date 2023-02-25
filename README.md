![owl-xtr-small](https://user-images.githubusercontent.com/105305546/220189533-c1352f2c-fece-4db7-8793-bfb18f840a35.png)

## Owlz! 
*"Create a Hoot!"*

Project 4 for Harvard's CS50w Web Programming with Python and JavaScript.

📹 `Youtube:` ...TBD

### Overview:
A social media site for making posts, following users and `hooting` out to the world!

-----

### Specifications:
Built with `Javascript`, `Python`, `Django`, `HTML/CSS`, `Bootstrap`, and `SQLite`. 

The site makes use of [Django's](https://docs.djangoproject.com/en/4.1/ref/contrib/humanize/) `humanize` template filters via `naturaltime` as well as [pagination](https://docs.djangoproject.com/en/4.1/topics/pagination/): displaying 10 posts per page. If there are more than ten posts, `“Next”` takes the user to the next page of posts. If not on the first page, `“Back”` takes the user to the previous page.

-----

### To Run:
1. Pip install `Django`
2. In the terminal, cd into the project4 directory.
3. Run `python3 manage.py makemigrations network` to make migrations for the network app.
4. Run `python3 manage.py migrate` to apply migrations to the database.
5. Run `python3 manage.py runserver` to start the Django web server and visit the website in the browser.

-----

## Login/Register
Users can `Register` an account with a specified `first name`, `last name`, `username`, and `password` to Login.

<img width="1200" alt="Screen Shot 2023-02-18 at 11 12 51 PM" src="https://user-images.githubusercontent.com/105305546/219921840-2386bb05-9c16-41b8-9288-519405ff54e0.png">

-----

## Hoots!
Users can create text-based posts, in this case `HOOTS!` up to `280 characters`. Users can `like`, `edit` [their own], and `bookmark` individual hoots.

To `Like`: users click the :heart: icon and the page is updated via `JavaScript` to showcase the number of likes per hoot.

To `Edit`: users click `“Edit”` [on their own posts], make specified changes, and click `"Save"`.

To `Bookmark`: users click the 🔖 icon to bookmark a hoot which can be viewed under the `Bookmarks` tab.

-----

## All Hoots!
Users can view all hoots posted by all users under the `All Posts` tab.

-----

## Following
Users can `follow` other users, and under the `following` tab, view only users they are following. Similarly, a user can `unfollow` on said user's `profile` page.

-----

## Profile
Users have a profile page, clicking on `Profile` takes a user to the specified user's profile displaying: number of `posts`, `followers` and `following` of the specified user. 

-----

## Data Models
