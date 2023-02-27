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

<img width="1116" alt="Screen Shot 2023-02-25 at 11 57 16 PM" src="https://user-images.githubusercontent.com/105305546/221393151-5b5ca0e9-884f-46e8-89d1-ad6d608245df.png">

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

## Profile
Clicking on the `Profile` tab takes a user to the specified profile displaying: number of `Hoots`, `Followers` and `Following`. 

<img width="1146" alt="Screen Shot 2023-02-27 at 5 27 14 PM" src="https://user-images.githubusercontent.com/105305546/221701004-caff47c4-609a-420c-ad16-6298326eb527.png">

Clicking either `Followers` or `Following` will display a Modal pop-up window displaying those users.

<img width="1146" alt="Screen Shot 2023-02-27 at 5 36 03 PM" src="https://user-images.githubusercontent.com/105305546/221701878-6d749d17-4fc0-4d88-874c-13686ce37795.png">

-----

## Following
Users can `follow` other users, and under the `following` tab, view `Hoots` only users they are following. Similarly, a user can `unfollow` a user via the `profile` page.

-----

## Data Models
Using SQLite, the models are rendered to the Django Admin andalphabetically as `Comments`, `Followers`, `Posts`, and `Users`.

<img width="1117" alt="Screen Shot 2023-02-25 at 11 52 13 PM" src="https://user-images.githubusercontent.com/105305546/221393006-408d2d34-590d-4c3e-a6e0-bb578d36fc96.png">
