![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome USER_NAME,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!

# Druid Computers

## Introduction


This is the fifth project for the Code Institute Diploma in Software Development with eCommerce.



![Screenshot of homepage]()

[View the live website on Heroku](https://druid-computers.herokuapp.com/)

Please note: To open any links in this document in a new browser tab, please press CTRL + Click.

## Table of Contents
* [User Experience Design (UX)](#UX)
    * [The Strategy Plane](#The-Strategy-Plane)
        * [Site Goals](#Site-Goals)
        * [Epics](#Epics)
        * [User Stories](#User-Stories)
    * [The Scope Plane](#The-Scope-Plane)
    * [The Structure Plane](#The-Structure-Plane)
        * [Opportunities](#Opportunities)
    * [The Skeleton Plane](#The-Skeleton-Plane)
        * [Wireframes](#Wireframe-mockups)
        * [Database Schema](#Database-Schema)
    * [The Surface Plane](#The-Surface-Plane)
* [Features](#features)
* [Future Enhancements](#future-enhancements)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## UX
##### Update with project details
### The Strategy Plane
*  The Pantry is intended to be a friendly community site for users to create and share their own recipes with others. Users will also be able to find recipes created by other users from around the world. The graphical elements and overall design of the site provide the user with a fun and enjoyable environment.

##### The Sites Ideal User
* Food lover looking to share their favourite recipes with others
* Someone looking to expand their recipe knowledge
* Someone looking for inspiration for new things to try
* Someone looking build their cooking social media following

#### Site Goals

* To provide users with a place to find recipes
* To provide users with a place to share their own recipes
* To provide users with a place to discover new meals

#### Epics
#### update with project details
10 Epics were created which were then further developed into 38 User Stories. The details on each epic, along with the user stories linked to each one can be found in the project kanban board [here](https://github.com/MattBCoding/druid-pp5/projects/1)

1. Initial Django setup [#1](https://github.com/MattBCoding/druid-pp5/issues/1)


### User Stories
#### update with project stats
From the Epics, 38 User stories were developed. Each story was assigned a classification of Must-Have, Should-Have, Could-Have or Won't Have. Each story was also assigned user story points, based on my best estimation for the time/difficulty of completing each story. A combination of being new to story estimation, inexperience with Django and time constraints during development left me completing 61 story points from the initial total of 131. From the initial 131 points, 82 were for Could Have stories. A number of these stories were created based on an ideal scenario of building out the project whilst I knew in the time available it would be unlikely I would complete those stories. I will however revisit them at a later time for a redevelopment of the project. The full list of User Stories, seperated by those completed and those pushed to a future release is available on the project [kanban board](https://github.com/MattBCoding/pp4-the-pantry/projects/1).


#### list out the epics and what they included - in following format:
These are the user stories that were completed within the projects first release, by Epic.

1. Initial Django setup
	* US#10 - Django Setup - As a Developer, I want to setup Django and install the supporting libraries predicted to be needed, so that I am ready to start development
	* US#11 - Django secure the secret key's - As a Developer, I want to set up the Django environment to secure the secret keys, so that I do not expose the keys in an insecure way
	* US#12 - Early Deployment to Heroku - As a Developer, I want to deploy the app to heroku, so that I can confirm everything works before development of the site and to enable continuous testing within the production environment



### The Scope Plane
#### include overview of the features planned from the notes from the UX phase of the development process
**Features planned:**
* User Profile - Create, Read, Update and Delete
* Recipes - Users can create, read, update and delete their own recipes
* Other Users Recipes - Users can read, like, save other users recipes
* Profiles - Users can read other users profiles
* Users can login to their account, change their password or their email
* Users can reset their password if they forget it
* Users can logout of their account
* Users need to be registered and logged in to access recipe creation, like, save functionality and access other users profiles.
* Responsive Design - the site needs to be fully responsive to cover the wide variety of devices users may use to access a recipe site
* Alternative colour modes available



### The Structure Plane

#### provide details of the user stories in the following format:

User Story:

> US#13 - Create a User Account - As a User, I would like to be able to create an account, so that I can create and save recipes

Acceptance Criteria:
* Given that I am an unregistered user, When I am on the homepage, Then I can see a button to sign up, And, When I click on the button, Then I am taken to the user registration page
* Given that I am an unregistered user, And, I am on the user registration page, When I enter my username, email address and password, And, I click on the register button, Then The system creates me an account, And, signs me in.
* Given that I have an account, And, I am signed into the account, When I have an option to create a recipe, And, when I click on that option, Then I am taken to a page where I can provide the details of my recipe
* Given that I am a registered user, When I am signed into my account, Then I do not see the register button

Implementation:
* Clearly accessible call to action on homepage to register for an account
* Clearly accessible link to login or register within main navigation bar
* Easy to use User registration process
* Clear UX design, prevent unnecessary links to register as a user, if user is already logged in.



#### Opportunities
#### insert updated OIVF table 
Arising from user stories
| Opportunities | Importance | Viability / Feasibility
| ------ | :------: | :------: |
| ** Provide users the ability to create an account ** | 5 | 5 |
| ** Provide users the ability to create recipes ** | 5 | 5 |
| ** Provide users the ability to edit recipes ** | 5 | 5 |
| ** Provide users the ability to view recipes ** | 5 | 5 |
| ** Provide users the ability to delete recipes ** | 5 | 5 |
| ** Provide users the ability to edit their account ** | 5 | 5 |
| ** Provide users the ability to view other accounts ** | 5 | 5 |
| ** Provide users the ability to delete their account ** | 5 | 5 |
| ** Provide users the ability to change the colour scheme ** | 2 | 5 |
| ** Provide users the ability to save a recipe ** | 3 | 5 |
| ** Provide users the ability to rate a recipe ** | 3 | 5 |
| ** Provide users the ability to access the site on any device ** | 5 | 5 |
| ** Provide users the ability to search the site for recipes ** | 4 | 5 |


### The Skeleton Plane
#### Wireframe mock-ups

Home page: The home page provides the user with a clear understanding as to the purpose of the site. There is a clear call to action for the user to search for a recipe with the inclusion of a search bar at the top of the home page. The welcome message is clearly visable to the user when they first arrive at the site regardless of the device they are using.

![Home Page Wireframe]()



![Product search page with results desktop wireframe]()

Users will have the ability to search for products

![Product search page with results desktop wireframe]()

Wireframes were also produced for each major page for both mobile and tablet devices. With the intention of the site being fully responsive so that no matter the device size the user is viewing the site on, it will display accordingly.

#### include wireframes - possibly in another file or linked to seperate files given the number of them

* [Home page mobile wireframe]()

#### Database Schema - needs updating

Several custom models were predicted to be required when building the site. The intention to utilise AllAuth for the user authentication system, which utilises the built in Django User Model removed the need to build a custom User model, however a custom User Profile was required. In order for the users to create Recipes a custom recipe model was required, which would be linked to the User Profile through using the profile as a foreign key. As each recipe could have a different number of ingredients or steps to it, it was decided to seperate out the ingredients and steps into their own model, and link them to the recipe through a foreign key. The database schema was planned using [DrawSQL app](https://drawsql.app/). Limitations of the app prevented labelling the field types correctly, it did not include the option to override the types available and did not include textarea, cloudinary fields or url fields. The models in the app reflect the true field choice.
##### insert database schema
![Database Schema Diagram]()

### The Surface Plane

#### Design

Once I was happy with the overall structure of the site, and the layout of the wireframes, I selected a colour scheme based on a desire for a simple and clean aesthetic. The site incorporates two main colours, blue and white, although specific shades were selected for various different areas, they all remained within the blue family. The white or off white shades are tinted with a little blue to maintain consistency. The colour scheme was referenced using the [contrast grid](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23FFFFFF%2C%20White%0D%0A%23F2F2F2%0D%0A%23DDDDDD%0D%0A%23CCCCCC%0D%0A%23888888%0D%0A%23404040%2C%20Charcoal%0D%0A%23000000%2C%20Black%0D%0A%232F78C5%2C%20Effective%20on%20Extremes%0D%0A%230F60B6%2C%20Effective%20on%20Lights%0D%0A%23398EEA%2C%20Ineffective%0D%0A&es-color-form__tile-size=compact&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp) which provides a grid of colour contrasts to ensure only those which would easily pass the AAA standard were selected to maximise accessibility for users.

##### Typography 
Three different fonts were utilised for the site. The main heading font of ........... and the smaller subheading font of ............. were selected for their futuristic almost technical feeling whilst Montserrat was chosen as a complimentary font which allowed users the ability to read the text easily and clearly.

##### Images
Several cartoon chef characters were accessed from [Vecteezy.com](https://www.vecteezy.com/members/heriyusuf/uploads). The artist Heriyusuf is responsible for the artwork for each cartoon chef. The artwork is available on a free license from [Vecteezy.com](https://www.vecteezy.com).
Images were acquired from free image sites [Pexels](https://www.pexels.com/) and [Unsplash](https://unsplash.com/), product photos were found on manufacturer media pages.


## Features
#### Include screen shots for each main feature page and a description


## Future Enhancements
There are several items of functionality that I would like to add in the future. I have left the original user stories that were developed in the project kanban board as future enhancement opportunities.
The key areas I would like to add to the site in the future are:
* A stock management system to enable the product sales to record and update stock level information
* A wider product range - the world of PC parts is varied even without looking at the hardware.
* The ability for users to login via social networks such as google or facebook
* Product ratings - users are able to leave a review of a product along with a rating. Currently, the rating is only recorded, it does not update an average statistic, however this can easily be incorporated in the future.

Some of the functionality above is provided by allauth which is already installed into the site, and therefore only has to be setup in order for it to function. Others would need to be developed completely. The stock system was an nice to have option in the development, there are references to its potential inclusion within the code however they do not currently update for example each product shows an instock pill on the product details.

## Testing

### Testing Strategy
I utilised an automated and manual testing strategy for the development of the site. A full detailed breakdown of the testing procedures and methodology can be found in the testing.md file [here](TESTING.md).
Seperate to the functionality testing of the site, and the testing of the code, User Story tests were implemented to ensure that the acceptance criteria of the user stories listed above were met. The commit at which the functionality requirements for each user story were met is listed in the issues section of the repo. It was applied to each issue before it was closed and marked as completed.


#### Testing Overview

Testing was divided into different sections to ensure everything was tested individually with test cases developed for each area.
#### insert testing schedule and correct path
[Testing Schedule Overview](/assets/testing/test-schedule.pdf)

A full detailed breakdown of the testing procedures and methodology can be found in the testing.md file [here](TESTING.md)

#### Validator Testing
All code files were validated using suitable validators for the specific language. The full details can be found in the testing.md file.
All code passed the validation, with only code generated by other parties producing errors or warnings.
* Django built in code within the settings file produced five line length errors. 
* Bootstrap code produced 260 warnings in the CSS validation. 
* Fontawesome cdn produced 6 HTML validation errors relating to css variables within the cdn css code. 
* The HTMX library that is inserted into the HTML template by django produces a warning stating that the link does not need to have the javascript file type declared.

#### Notable Bugs



#### Technologies Used

* Python
    * The following python modules were used on this project:
        * asgiref==3.5.2
        * bleach==5.0.0
        * boto3==1.24.18
        * botocore==1.27.18
        * certifi==2022.5.18.1
        * cffi==1.15.0
        * charset-normalizer==2.0.12
        * crispy-bootstrap5==0.6
        * cryptography==37.0.2
        * defusedxml==0.7.1
        * dj-database-url==0.5.0
        * Django==3.2
        * django-allauth==0.50.0
        * django-countries==7.3.2
        * django-crispy-forms==1.14.0
        * django-filter==22.1
        * django-htmx==1.12.0
        * django-storages==1.12.3
        * django-summernote==0.8.20.0
        * gunicorn==20.1.0
        * idna==3.3
        * jmespath==1.0.1
        * oauthlib==3.2.0
        * Pillow==9.1.1
        * psycopg2==2.9.3
        * pycparser==2.21
        * PyJWT==2.4.0
        * python-dateutil==2.8.2
        * python3-openid==3.2.0
        * pytz==2022.1
        * requests==2.27.1
        * requests-oauthlib==1.3.1
        * s3transfer==0.6.0
        * six==1.16.0
        * sqlparse==0.4.2
        * stripe==3.2.0
        * typing_extensions==4.2.0
        * urllib3==1.26.9
        * webencodings==0.5.1

* Django
    * Django was used as the main python framework in the development of this project
    * Django AllAuth was utilised to provide enhanced user account management functionality.
* Heroku
    * Was used as the cloud based platform to deploy the site on
* Heroku PostgreSQL
    * Heroku PostgreSQL was used as the database for this project during development and in production.
* HTMX
    * HTMX is a JavaScript library that enables forms to be submitted and data to be retrieved from the backend without refreshing the entire page. It was used extensively for pages that included form submission such as the creation of the recipes where creating ingredients in another model, and creating steps in a third model was required. This package provided a simpler approach to using multiple formsets and custom JavaScript.
* JavaScript
    * Custom JavaScript was utilised to enable the colour scheme functionality, the mobile menu, the enabling and disabling of buttons on forms to prevent users inadvertantly causing errors when trying to submit multiple forms at the same time, and to display the current image in the form rather than a hyperlink to the image itself.
* Bootstrap 5.2
    * Bootstrap was used for general layout and spacing requirements for the site.
* Font Awesome
    * Was used for access to several icons for different sections where icons were appropriate.
* CSS
    * Custom css was written for a large number of areas on the site to implement custom styling and escape a bootstrap look and feel to the site.
* Jinja/Django Templating
    * Jinja/Django templating language was utilised to insert data from the database into the sites pages. It was also utilised to perform queries on different datasets.
* HTML
    * HTML was used as the base language for the templates created for the site.

#### Packages Used

* VS Code was used to develop the site
* Git was utilised for version control and transferring files between the code editor and the repository
* GitHub was utilised for storing the files for this project
* Balsamiq was utilised to develop wireframes for the site from which the design was based
* Adobe Illustrator was used to adapt images for use within the site.
* Figma was used to develop the database schema during development - I used this instead of a DB app due to the ease with which to document the actual field types rather than some of the online apps which don't include fields that are available.

#### Resources Used

* The Django documentation was used extensively during development of this project
* The HTMX documentation was used as a reference source for the development of the HTMX features
* The Django AllAuth documentation was used as a reference and a guide for implementing the package and its features.
* The Cloudinary documentation was used extensively during development to setup the configuration between django and the cloudinary apis
* The Code Institute reference material was used as a general reference for things that I had previously done during the course.
* All other resources used are referenced where appropriate.


##### Other Libraries Used

## Deployment

The site was deployed via Heroku, and the live link can be found here - [Druid](https://druid-computers.herokuapp.com/)

### Project Deployment - needs adapting for AWS and Stripe

To deploy the project through Heroku I followed these steps:
* Sign up / Log in to [Heroku](https://www.heroku.com/)
* From the main Heroku Dashboard page select 'New' and then 'Create New App'
* Give the project a name - I entered The-Pantry and select a suitable region, then select create app. The name for the app must be unique.
* This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the resources tab.
* Add the database to the app, in the add-ons section search for 'Heroku Postgres', select the package that appears and add 'Heroku Postgres' as the database
* Navigate to the setting tab, within the config vars section copy the DATABASE_URL to the clipboard for use in the Django configuration.
* Within the django app repository create a new file called env.py - within this file import the os library and set the environment variable for the DATABASE_URL pasting in the address copied from Heroku. The line should appear as os.environ["DATABASE_URL"]= "Paste the link in here"
* Add a secret key to the app using os.environ["SECRET_KEY"] = "your secret key goes here"
* Add the secret key just created to the Heroku Config Vars as SECRET_KEY for the KEY value and the secret key value you created as the VALUE
* In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
* insert the line if os.path.isfile("env.py"): import env
* remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
* replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} ensure the correct indentation for python is used.
* In the terminal migrate the models over to the new database connection
* Navigate in a browser to cloudinary, log in, or create an account and log in. 
* From the dashboard - copy the CLOUDINARY_URL to the clipboard
* in the env.py file created earlier - add os.environ["CLOUDINARY_URL"] = "paste in the Url copied to the clipboard here"
* In Heroku, add the CLOUDINARY_URL and value copied to the clipboard to the config vars
* Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars
* this key value pair must be removed prior to final deployment
* Add the cloudinary libraries to the list of installed apps, the order they are inserted is important, 'cloudinary_storage' goes above 'django.contrib.staitcfiles' and 'cloudinary' goes below it.
* in the Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
* Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
* Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
* Add Heroku to the ALLOWED_HOSTS list the format will be the app name given in Heroku when creating the app followed by .herokuapp.com
* In your code editor, create three new top level folders, media, static, templates
* Create a new file on the top level directory - Procfile
* Within the Procfile add the code - web: guincorn PROJECT_NAME.wsgi
* In the terminal, add the changed files, commit and push to GitHub
* In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors.
* Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

#### Forking the repository
By forking the GitHub Repository you can make a copy of the original repository to view or change without it effecting the original repository
This can be done by
    * Log into GitHub or create an account.
    * Locate the repository at https://github.com/MattBCoding/druid-pp5 .
    * At the top of the repository, on the right side of the page, select "Fork" from the buttons available.
    * A copy of the repository should now be created in your own repository.

#### Create a clone of this repository
Creating a clone enables you to make a copy of the repository at that point in time - this lets you run a copy of the project locally:
This can be done by:
* Navigate to https://github.com/MattBCoding/druid-pp5
* click on the arrow on the green code button at the top of the list of files
* select the clone by https option and copy the URL it provides to the clipboard
* navigate to your code editor of choice and within the terminal change the directory to the location you want to clone the repository to.
* type 'git clone' and paste the https link you copied from github
* press enter and git will clone the repository to your local machine

### Acknowledgements

I'd like to thank the following:
* Daisy McGirr for all her help during this project.
* Sean, Ed and Alex at CI Tutor support for their patience and pointing me in the right direction when I went off course.