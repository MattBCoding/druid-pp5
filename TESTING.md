# Test Cases and Execution Report

To navigate back to the main README click [here](README.md)

The full testing spreadsheet containing all the tests performed during the testing phase of development can be found [here]()

## Test Case 001

![Test Case 001]()

### Python Validation
The Python code was checked using the pep8 validator available at [pep8online.com](https://pep8online.com). No errors were reported by the validator in the files I created. The settings.py file did however contain five line too long errors. Each of these errors related to Django default code pointing to password validation paths or from Cloudinary code pointing to the cloudinary storage service and could not be shortend.

* Screenshots of the validator reports are here:
    * Druid Folder
        * [asgi.py file](/static/docs/img/validation/druid-asgi-py.png) 
        * [settings.py file](/static/docs/img/validation/druid-settings-py.png) 
        * [urls.py file](/static/docs/img/validation/druid-urls-py.png) 
        * [wsgi.py file](/static/docs/img/validation/druid-wsgi-py.png)
    * Bag Folder
        * [apps.py file](/static/docs/img/validation/bag-apps-py.png)
        * [contexts.py file](/static/docs/img/validation/druid-contexts-py.png)


## Test Case 001a

![Test Case 001a](/assets/testing/test-case-0001a-b.png)

### JavaScript Validation
The JavaScript code was checked using the jshint.com validator available at [jshint.com](https://jshint.com/). No errors were detected within the files I created. Include details of results

* Screenshot of the validator report is available here:
    * JavaScript
        * [script.js file]()

## Test Case 001b

![Test Case 001b](/assets/testing/test-case-0001a-b.png)

### CSS Validation


The full CSS Validator report is available here on the [CSS Validator Site]()

![CSS Validator Report]()

## Test Case 001c

[Test Case 001c part 1]()
[Test Case 001c part 2]()
[Test Case 001c part 3]()

### HTML Validation
Due to the way Django templates include Django template code in them, and extend other templates, it is not possible to copy the code for each page out of the source html files. Therefore, in order to validate the code correctly, I navigated to the site and accessed the rendered html code through the developer tools of the browser I used during development, Google Chrome. I then pasted the code into the HTML validator site available at [W3C Markup Validation Service](https://validator.w3.org/). The validator returns . There were no errors returned from the HTML produced from the templates themselves.

Given that there is logic utilised within the templates to display some elements under different conditions,  test cases were developed to cover the different variations of logic available within the sites pages. Each is detailed in the full testing file available from the link at the top of this page, or in the screenshots at the top of this section. 

## Test Case 002

![Test Case 002]()

### Unregistered User Testing - General Site Navigation
The overall site navigation was testing fully to ensure all links directed the user to the correct page. Given that users will receive slightly differing navigation bars depending on if they are logged in or not, this was first tested fully for users who are not logged into the site. All links and the settings modal were tested for correct functioning.

## Test Case 003

![Test Case 003](/assets/testing/test-case-0003.png)

To navigate back to the main README click [here](README.md)

## Additional Manual Testing

The test cases were performed multiple times during the development of the site with adjustments made to the code logic and functionality based on user feedback.

## User Story Testing - By Epic - as per layout below

2. User Profile

	> US#13 - Create a User Account - As a User, I would like to be able to create an account, so that I can create and save recipes

* Acceptance Criteria 1
    * Given that I am an unregistered user When I am on the homepage Then I can see a button to sign up And, When I click on the button Then I am taken to the user registration page

This is achieved by the link in the standard navigation bar for login/register
![Standard Nav Bar]()

It is also achieved by the standard button in the member benefits section
![Standard Member Benefits]()

* Acceptance Criteria 2
    * Given that I am an unregistered user
And, I am on the user registration page
When I enter my username, email address and password
And, I click on the register button
Then The system creates me an account
And, signs me in

This is achieved - although the process includes email verification and the user has to sign in themselves due to the security settings chosen for the site

* Acceptance Criteria 3
    * Given that I have an account
And, I am signed into the account
When I have an option to create a recipe
And, when I click on that option
Then I am taken to a page where I can provide the details of my recipe

This is achieved, the option to add a recipe appears in the user menu as part of the main navigation bar
![Logged in Nav Bar User Menu Open]()

* Acceptance Criteria 4
    * Given that I am a registered user
When I am signed into my account
Then I do not see the register button

This is achieved - the login/register link within the standard navigation bar is replaced with a user menu for logged in users - see image on acceptance criteria 1.

