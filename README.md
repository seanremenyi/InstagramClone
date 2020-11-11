# Photo Sharing Application (Instagram Clone)

## Purpose

This will be a photo sharing app, similar to Instagram. User's will be able to sign up, create a profile. Once signed up, User's will be able to post pictures.
These picture's can be tagged with keys to later search through. People can then scroll through other people's pictures, like and comment on them. 

## Installing

##### Using Ubuntu,

1. Clone git repo
2. Get into the directory
    1.`cd InstagramClone`
3. If not running python 3.8, run the following bash commands
    1. `sudo apt update`
    2. `sudo apt install python3.8`
4. Create a virtual enviornment
    1. `sudo apt-get install python3-pip`
    2. `sudo apt-get install python3-venv`
    3. `python3 -m venv venv`
    4. `source venv/bin/activate`
5. Install the modules in requirements.txt
    1. `cd instagram-clone`
    2. `pip install -r requirements.txt`

##### Setting up the Database using Postgres

For configuration steps for postgres refer to Colin's guide on how to set up (the final section)

[EC2 postgres sql guide](https://github.com/Ctrain68/EC2_postgres_sql_guide)

##### Setting up Flask

1. You'll need to set up the following environment variables
    1.`export FLASK_APP=main.py`
    2.`export FLASK_ENV=development`
    3.`flask run`

1. If using an EC2 instance you will eed to configure an inbound rule (refer to the guide above). However the rule will be for a custom TCP over port 8000 with ip address 0.0.0.0/0.
2. You will have to add the following environment variable
    1.`export FLASK_RUN_PORT=8000`
3. Run flask with the following command
    1.`-h 0.0.0.0`


## Layout
**Sign-in/Create Page**

The first page will be a sign in page. The User will be prompted to enter a username/password which will lead to their profile if entered correctly.

If the User doesn't have an account and would like to create one instead. They will be able to with the create profile button.

This will take the User to a new page where they can create a profile name (this must be unique and will be the primary identifier for users), a profile picture to upload, a short description of themselves and some contact info (this will be private however to other users).

Below are the wireframes for both the mobile and desktop versions.

![](docs/wireframes/Signin_Create.png)

**Profile Page**

Once signed or profile is created, the user will be brought to the user's profile page. This will include their picture, name, short description at the top. Underneath will be a counter for all the posts they have made, The amount of profiles they follow as well as the amount that follows them. Underneath that will be a small version of all the pictures they have posted.

On the User's Profile page there will be a link to update/edit their profile however when viewing another profile (which will have the same format) that button will be replaced by a follow button.

The overall layout for the pages will have a navigation bar listing what page the user is on out of Profile, Feed, Browse, Notification and post. With the current pge being highlighted. This navigation bar will be at the bottom of the screen for mobile and at the top for desktop.

Wireframes are shown below.

![](docs/wireframes/Profile.png)

**Edit Profile**

For the edit profile feature the User will be taken to a page similar to the create profile layout with links to edit the info. If these are clicked, the user will be take to a age with all the same headers over empty text boxes, these will be filled out and the changes will be updated.

On the edit page there will be an option to logout from the session which will lead to a page saying goodbye.

There will also be a delete profile option which the user can delete theyre profile. If clicked the user will be prompted to make sure this is what they want, if so the profile will be deleted and another page similar to the logout page will be shown with another goodbye message.

Wireframes are shown below.

![](docs/wireframes/EditProfile.png)

**Feed**

This page will show latest pictures of people you follow. The format for pictures to scroll through will have the name of the profile who posted with their picture, underneath is the picture itself with an option to like or comment and if the user wants to see the profile, they can click on the name or the picture of the other user's profile above the picture. Underneath all that is the amount of likes and comments the picture has. Underneath that will be the description of the picture, then the first comment and the last comment. In between the two will be an option to expand and show all comments on a picture but the default will just show the first and last comment. There will be an option to just click the picture itself and expand it.

The layout is also the same from ere on where the users profile picture and name will be shown at the top of the page.

Wireframes are shown below.

![](docs/wireframes/Feed.png)

**Browse**

This page will at first have some random pictures that the User can click on. There will also be a search bar. Once a search is made which will search keywords through the pictures and display pictures with the relevant keywords. This display format will greatly resemble the feed.

Wireframes are shown below.

![](docs/wireframes/Browse.png)

**Clicking on a Picture**

When clicking on a picture, The user will be take to a page that is just focused on the picture itself. This will include all the relevant buttons and descriptions described above. The Navigation will remain on the browse feature when on this page.

Wireframes are shown below.

![](docs/wireframes/ClickPicture.png)

**Post**

This page will be to upload a new picture. There will be all empty fields for the user to fill out and an option for the user to upload a pictures.

Wireframes are Shown below.

![](docs/wireframes/Post.png)

**Notification**

This page will list all notifications. This will show if one of the pictures received a like or a comment and if the profile is followed the user will see this in their notification page. This app doesn't send any sort of push notifications so this page wil be where all of this is shown.

Wireframes are shown below

![](docs/wireframes/Notifications.png)

## Entity Relationship Diagram

The database that the app will connect to will have 3 tables. One for the profile, one for pictures and one for comments.

The following diagram shows the breakown of each table with its contraints and relations to other tables.

![](docs/database/ERD.png)

## Trello Board

https://trello.com/b/s5ovBbBQ/instagram
