# Test Cases and Execution Report

To navigate back to the main README click [here](README.md)

The full testing spreadsheet containing all the tests performed during the testing phase of development can be found [here](/static/docs/testing-schedule.pdf)

Testing was performed with a desktop computer, ipad and iphone.
The following browsers were tested:
Google Chrome,
Microsoft Edge
iOS Safari

## Test Case 001

### Python Validation
The Python code was checked using the pep8 validator available at [pep8online.com](https://pep8online.com). No errors were reported by the validator in the files I created. The settings.py file did however contain five line too long errors. Each of these errors related to Django default code pointing to password validation paths or from the summernote configuration settings pointing to custom css or js files and could not be shortend.

* Screenshots of the validator reports are here:
    * Druid Folder
        * [asgi.py file](/static/docs/img/validation/druid-asgi-py.png) 
        * [settings.py file](/static/docs/img/validation/druid-settings-py.png) 
        * [urls.py file](/static/docs/img/validation/druid-urls-py.png) 
        * [wsgi.py file](/static/docs/img/validation/druid-wsgi-py.png)
    * Bag Folder
        * [apps.py file](/static/docs/img/validation/bag-apps-py.png)
        * [contexts.py file](/static/docs/img/validation/druid-contexts-py.png)
        * [urls.py file](/static/docs/img/validation/bag-urls-py.png)
        * [views.py file](/static/docs/img/validation/bag-views-py.png)
    * Blog Folder
        * tests sub folder
            * [test_forms.py file](/static/docs/img/validation/blog-tests-test-forms-py.png)
            * [test_views.py file](/static/docs/img/validation/blog-tests-test-views-py.png)
        * [admin.py file](/static/docs/img/validation/blog-admin-py.png)
        * [apps.py file](/static/docs/img/validation/blog-apps-py.png)
        * [forms.py file](/static/docs/img/validation/blog-forms-py.png)
        * [models.py file](/static/docs/img/validation/blog-models-py.png)
        * [urls.py file](/static/docs/img/validation/blog-urls-py.png)
        * [views.py file](/static/docs/img/validation/blog-views-py.png)
        * [widgets.py file](/static/docs/img/validation/blog-widgets-py.png)
    * Checkout Folder
        * [admin.py file](/static/docs/img/validation/checkout-admin-py.png)
        * [apps.py file](/static/docs/img/validation/checkout-apps-py.png)
        * [filters.py file](/static/docs/img/validation/checkout-filters-py.png)
        * [forms.py file](/static/docs/img/validation/checkout-forms-py.png)
        * [models.py file](/static/docs/img/validation/checkout-models-py.png)
        * [signals.py file](/static/docs/img/validation/checkout-signals-py.png)
        * [urls.py file](/static/docs/img/validation/checkout-urls-py.png)
        * [views.py file](/static/docs/img/validation/checkout-views-py.png)
        * [webhook_handler.py file](/static/docs/img/validation/checkout-webhook-handler-py.png)
        * [webhooks.py file](/static/docs/img/validation/checkout-webhooks-py.png)
    * Home Folder
        * [admin.py file](/static/docs/img/validation/home-admin-py.png)
        * [apps.py file](/static/docs/img/validation/home-apps-py.png)
        * [forms.py file](/static/docs/img/validation/home-forms-py.png)
        * [models.py file](/static/docs/img/validation/home-models-py.png)
        * [urls.py file](/static/docs/img/validation/home-urls-py.png)
        * [views.py file](/static/docs/img/validation/home-views-py.png)
    * Products Folder
        * tests sub folder
            * [test_forms.py file](/static/docs/img/validation/products-tests-test-forms-py.png)
        * [admin.py file](/static/docs/img/validation/products-admin-py.png)
        * [apps.py file](/static/docs/img/validation/products-apps-py.png)
        * [forms.py file](/static/docs/img/validation/products-forms-py.png)
        * [models.py file](/static/docs/img/validation/products-models-py.png)
        * [urls.py file](/static/docs/img/validation/products-urls-py.png)
        * [utils.py file](/static/docs/img/validation/products-utils-py.png)
        * [views.py file](/static/docs/img/validation/product-views-py.png)
    * Profiles Folder
        * tests sub folder
            * [test_forms.py file](/static/docs/img/validation/profiles-tests-test-forms-py.png)
            * [test_views.py file](/static/docs/img/validation/profiles-tests-test-views-py.png)
        * [admin.py file](/static/docs/img/validation/profiles-admin-py.png)
        * [apps.py file](/static/docs/img/validation/profiles-apps-py.png)
        * [forms.py file](/static/docs/img/validation/profiles-forms-py.png)
        * [models.py file](/static/docs/img/validation/profile-models-py.png)
        * [urls.py file](/static/docs/img/validation/profiles-urls-py.png)
        * [utils.py file](/static/docs/img/validation/profiles-utils-py.png)
        * [views.py file](/static/docs/img/validation/profiles-views-py.png)
    * Root directory
        * [custom_storages.py file](/static/docs/img/validation/custom-storages-py.png)
        * [manage.py file](/static/docs/img/validation/root-manage-py.png)

## Test Case 001a

### JavaScript Validation
The JavaScript code was checked using the jshint.com validator available at [jshint.com](https://jshint.com/). No errors were detected within the files I created. 

* Screenshot of the validator report is available here:
    * JavaScript
        * [htmx.js file](/static/docs/img/validation/htmx-validator-results.png)
        * [quantity_input file](/static/docs/img/validation/quantity-input-script.png)
        * [script.js file](/static/docs/img/validation/script-validator-results.png)
        * [stripe.js file](/static/docs/img/validation/stripe-js-validator-results.png)
        * [summernote.js file](/static/docs/img/validation/summernote-js-results.png)

## Test Case 001b

### CSS Validation

The full CSS Validator report is available here on the [CSS Validator Site](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fdruid-computers.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) . When validating by url it discovers a total of 301 warnings relating to the Mailchimp newsletter imported css and the bootstrap code. The validator reports three warnings for the main style.css file, the warnings only relate to the use of css variables which the validator does not check and can be ignored. When validating by direct input the validator also reports a warning about the imported style sheet - or the google font import, the warning only states that it does not check the imported style sheet in direct input mode and can be ignored.

* [CSS Validator Report - style.css](/static/docs/img/validation/css-validator-results.png)
* [Checkout CSS file results](/static/docs/img/validation/checkout-css-validator-results.png)
* [Summernote CSS file results](/static/docs/img/validation/summernote-css-validator-results.png)

## Test Case 001c

### HTML Validation
Due to the way Django templates include Django template code in them, and extend other templates, it is not possible to copy the code for each page out of the source html files. Therefore, in order to validate the code correctly, I navigated to the site and accessed the rendered html code through the developer tools of the browser I used during development, Google Chrome. I then pasted the code into the HTML validator site available at [W3C Markup Validation Service](https://validator.w3.org/). When validating the pages accessible by url - those that do not require a login - the validator returns three warnings relating to the type attribute being unnecessary for javascript resources. All of these warnings are generated by imported files, mailchimp, bootstrap and fontawesome, as the script declaration is not within the html code but in resources being inserted via the cdn links these warnings can not be removed and are therefore ignored. There were no errors returned from the HTML produced from the templates themselves. When copying and pasting the code from the brower into the direct input option within the validator, it shows a total of 10 errors. Six (6) errors are produced by the code inserted from fontawesome and relate to CSS code it inserts for animations, whilst the remaining four (4) errors are created by the Stripe JS file and relate to the use of a name attribute and CSS styling on an iframe that it inserts. These errors and warnings can not be removed as they are inserted by the Fontawesome and Stripe cdn files. They do not interfere with the functionality of the site and have therefore been ignored.

Pages with a Summernote text editor will return six (6) HTML validation errors. These errors are generated by the iframe code the summernote editor inserts. One appears to be related to the summernote code having a hidden text area input - whilst the others are related to styling rules that are being applied to the summernote editor field. As they are inserted by the summernote editor they have been ignored.

A full list of the errors and warnings that are generated by the cdn links or third party packages can be seen [here](/static/docs/img/validation/full-list-of-html-validator-errors-warnings.png).

Given that there is logic utilised within the templates to display some elements under different conditions,  test cases were developed to cover the different variations of logic available within the sites pages. Each is detailed in the full testing file available from the link at the top of this page, or in the screenshots at the top of this section.

* [Bag page - empty bag](/static/docs/img/validation/bag-empty.png)
* [Bag page - products in bag](/static/docs/img/validation/bag-with-products-fixed.png)
* [Blog - add blog page](/static/docs/img/validation/blog-add-blog-post.png)
* [Blog - all posts page](/static/docs/img/validation/blog-all-posts-page.png)
* [Blog - all posts with categories page](/static/docs/img/validation/blog-all-posts-with-category-form.png)
* [Blog - Blog Post Detail page](/static/docs/img/validation/blog-blog-post-detail.png)
* [Blog - Multiple category forms opens](/static/docs/img/validation/blog-category-forms-all-open-at-same-time.png) this shows the validation errors that were fixed using javascript - details in the notable bugs section of the main README file.
* [Blog - Edit blog post](/static/docs/img/validation/blog-edit-blog-post.png)
* [Checkout - checkout success](/static/docs/img/validation/checkout-checkout-success.png)
* [Checkout - My Orders page](/static/docs/img/validation/checkout-my-orders-logged-in.png)
* [Checkout - Order Management Page](/static/docs/img/validation/checkout-order-management-page.png)
* [Checkout - Order Status non logged in user](/static/docs/img/validation/checkout-order-status-non-logged-in.png)
* [Checkout - Update Order Status - employee view](/static/docs/img/validation/checkout-update-order-status.png)
* [Home - Home page](/static/docs/img/validation/home-home.png)
* [Home - About page](/static/docs/img/validation/home-about.png)
* [Home - Contact page](/static/docs/img/validation/home-contact.png)
* [Privacy Policy Page](/static/docs/img/validation/privacy-policy-page.png)
* [Products - add products page](/static/docs/img/validation/products-add-product.png)
* [Products - all products page](/static/docs/img/validation/products-all-products.png)
* [Products - edit product page](/static/docs/img/validation/products-edit-product.png)
* [Products - product management page](/static/docs/img/validation/products-management.png)
* [Products - product details page](/static/docs/img/validation/products-product-detail-page.png)
* [Products - product details page with a review](/static/docs/img/validation/products-product-detail-page-with-review.png)
* [Products - product details page with a review and response](/static/docs/img/validation/products-product-detail-page-with-review-and-response.png)
* [Products - product details page with review form](/static/docs/img/validation/products-product-detail-review-form-showing.png)
* [Products - product details page with a review and response form showing](/static/docs/img/validation/products-product-detail-with-response-form-showing.png)
* [Products - Search Results page](/static/docs/img/validation/products-search-results.png)
* [Profiles - Delete Address](/static/docs/img/validation/profile-delete-address.png)
* [Profiles - Edit Address](/static/docs/img/validation/profile-edit-address.png)
* [Profiles - edit details](/static/docs/img/validation/profile-edit-details.png)
* [Profiles - wishlist page](/static/docs/img/validation/profile-wishlist-page.png)

## Test Case 002

![Test Case 002](/static/docs/img/testing/tc002.png)

### Unregistered User Testing - General Site Navigation
The overall site navigation was testing fully to ensure all links directed the user to the correct page. Given that users will receive slightly differing navigation bars depending on if they are logged in or not, this was first tested fully for users who are not logged into the site. All links were tested for correct functioning.

## Test Case 003

![Test Case 003](/static/docs/img/testing/tc003.png)

### Unregistered User Testing - General Site Navigation - Product Pages
The product pages were tested in detail to ensure all links and functionality worked as required. This included detailed testing of the pagination controls, product card add to bag and quantity selectors, product detail pages and product detail page add to bag and quantity selectors. For the purposes of assessment the pagination was set to 5 products per page. this was to ensure that the pagination controls would activate given the number of products currently listed.

## Test Case 004

![Test Case 004](/static/docs/img/testing/tc004.png)

### Unregistered User Testing - Blog Page
The blog pades were tested for functionality for unregistered users to ensure all links worked correctly and everything displayed correctly.

## Test Case 005

![Test Case 005](/static/docs/img/testing/tc005.png)

#### Registered Employee Testing - Blog Page
For employees when they access the blog pages they will have additional options and functionality. Therefore it was important to test this additional functionality to ensure everything worked correctly. Seperate tests were conducted to ensure that all necessary buttons were present and working, the edit blog post process worked correctly, the add blog post process worked correctly, and the delete blog post process worked correctly.

## Test Case 006

![Test Case 006](/static/docs/img/testing/tc006.png)

### Unregistered User Testing - Purchase Process - with Successful payment
Given that there are a number of steps a user would go through to purchase products on the site, it was important to test the full functionality. The full process was documented to ensure each possible step was tested fully including all site functionality and backend processes such as email confirmations.

## Test Case 007

![Test case 007](/static/docs/img/testing/tc007.png)

### Unregistered User Testing - Purchase Process - with failed payment
Similar tests were conducted with the failed payment test cards to ensure a failed payment did not adversely affect any functionality.

## Test Case 008

![Test Case 008](/static/docs/img/testing/tc008.png)

### Registered User Testing - Purchase Process -Successful payment
Registered users gain a few additional features during the purchase process, therefore it was necessary to ensure those features worked correctly. The features were broken up over multiple test cases to ensure they were tested fully. The first case included a complete run through the purchase process with a successful payment to ensure all base functionality worked correctly when a user is logged in.

## Test Case 009

![Test Case 009](/static/docs/img/testing/tc009.png)

### Registered User Testing - Purchase Process - Unsuccessful payment
The registered user purchase process was tested to ensure that all base functionality worked correctly when a user payment fails.

## Test Case 010

![Test Case 010](/static/docs/img/testing/tc010.png)

### Registered User Testing - Purchase Process - Successful payment with saving the address
One of the final options a registered user has is to save the address that they are providing within the checkout form. It was necessary to test the form both with the option selected and unselected to ensure that it did not affect any other functionality. When the option is selected it was necessary to ensure that the address the user entered was successfully saved and associated with their account. This was achieved via both the admin panel and registered user accessible pages on the site that list all the addresses they have saved.

## Test Case 011

![Test Case 011](/static/docs/img/testing/tc011.png)

### Registered User Testing - Add Address Process
Registered Users can add an address to their account without having to do it during the purchase process. To ensure this worked correctly tests were conducted to ensure that the when a user completes the add address form and requests it to be saved the address is added to their account successfully. Form validation tests were performed to ensure that the address form notified the user on which fields were required for an address to be saved.

## Test Case 012

![Test Case 012](/static/docs/img/testing/tc012.png)

### Registered User Testing - Edit Address Process
Once a registered user has created an address record, they may wish to edit it. Therefore it was necessary to provide the associated functionality to the user and test the process to ensure it works correctly. The address created in previous test cases was edited successfully through two different tests.

## Test Case 013

![Test Case 013](/static/docs/img/testing/tc013.png)

### Registered User Testing - Make Address Default Process
Registered users can set one of the addresses that they have saved to their account as the default address. This speeds up the checkout process by prefilling the checkout form with the details from the default address. To ensure that this process worked correctly the process for setting an address as the default address was tested before moving on to test that the functionality within the checkout process in a different test case.

## Test Case 014

![Test Case 014](/static/docs/img/testing/tc014.png)

### Registered User Testing - Purchase Process - Select Address from Saved Addresses
The address selection functionality was tested along with the default address functionality within the checkout process. The default address prepopulates the checkout form for registered users. They have the option to select an address from the addresses that they have saved. All functionality worked as expected.

## Test Case 015

![Test Case 015](/static/docs/img/testing/tc015.png)

### Registered User Testing - Delete Address Process
Registered users may want to delete an address record from their account at any point. Therefore the option to delete an address was provided. Tests were conducted to ensure that the when a user requests an address to be deleted that it is deleted correctly.

## Test Case 016

![Test Case 016](/static/docs/img/testing/tc016.png)

### Registered User Testing - Purchase Process - Adding Review to product purchased
When registered users purchase a product, they have the option to write a review for it. The full process was tested to ensure that it works correctly including the triggering of the add review option, the form functionality and the submission of the review.

## Test Case 017

![Test Case 017](/static/docs/img/testing/tc017.png)

### Registered User Testing - Purchase Process - Edit Review
As a registered user has the option to add a review for purchased products, they will also require the ability to edit the review. This functionality was tested to ensure that it works correctly.

## Test Case 018

![Test Case 018](/static/docs/img/testing/tc018.png)

### Employee User Testing - Adding Response to User Review
The employee ability to add a response to a user review was tested. The process was tested to ensure that the form is available when required, that the employee users only have the ability to access it, that the response gets added correctly and that it displays correctly when added.

## Test Case 019

![Test Case 019](/static/docs/img/testing/tc019.png)

### Employee User Testing - Editing Response to User Review
Once a response has been created it is important that for whatever reason employee users have the ability to edit it. Typo's or spelling mistakes do not create a good impression for potential customers after all. Therefore the functionality was included in the response options. The functionality was tested to ensure that when the employee requested the functionality the edit form was loaded with the correct response content, and that when the user requested the response be saved the updates were saved correctly.

## Test Case 020

![Test Case 020](/static/docs/img/testing/tc020.png)

### Employee User Testing - Deleting User Review
The ability to delete a review is shared between the registered user who authored the review and employee users. I tested the original authors ability to delete a review to ensure they could remove it if they wanted to. I also tested other users to ensure that they did not have access to delete the review. Employee access was tested to ensure that if required they could delete the review as well. This enables the employees to manage the content on the site to ensure it remains appropriate for the site.


## Test Case 021

![Test Case 021](/static/docs/img/testing/tc021.png)

### Unregistered User Testing - Contact Form Submission
The contact form on the contact page provides any user with the ability to send a message to the company. Under pinning the functionality is an email system. When a user completes the form and submits their message it is saved into the database and an email is generated to the company with the details. The original message is also sent to the user as part of a thank you message to let them know that it was received ok. The full functionality was tested to ensure that the message was saved, emails were sent to the user and the company email and that the form validation worked correctly.


## Test Case 022

![Test Case 022](/static/docs/img/testing/tc022.png)

### Unregistered User Testing - User Registration Process
The user registration process is underpinned by the Django AllAuth library. This provides a number of functionalities, these were tested individually to ensure everything worked correctly. The first part to test was the user registration process to ensure that the registration forms worked correctly, the email validation was sent correctly and the validation confirmation system worked correctly.


## Test Case 023

![Test Case 023](/static/docs/img/testing/tc023.png)

### Registered User Testing - Login Process
As part of the AllAuth testing process, the login system was tested to ensure that only users who are registered and who attempt to login by providing the correct information are able to do so. 

## Test Case 024

![Test Case 024](/static/docs/img/testing/tc024.png)

### Registered User Testing - Logout process
As part of the AllAuth testing process, the logout system was tested to ensure that users could logout successfully. It was also tested to ensure that if a user logs out then they can not through using the back button or direct url entry access a page that required them to be logged in.

## Test Case 025

![Test Case 025](/static/docs/img/testing/tc025.png)

### Registered User Testing - My Wishlist Process
Registered users have the ability to add products to their wishlist where they can effectively save them for quick access at a later time. This functionality was tested to ensure that when a user attempts to add a product to their wishlist the process works as expected. It was also tested to ensure they a user can remove the product from the wishlist when they attempt to, either through the product detail or wishlist pages. The wishlist page itself was also tested to ensure that the add to bag and quantity selectors functionality worked correctly. The product links within the wishlist were also confirmed to be working as expected. Finally the wishlist page was tested to ensure that the message informing users they have no items in the wishlist when it is empty displays correctly.

## Test Case 026

![Test Case 026](/static/docs/img/testing/tc026.png)

### Registered User Testing - Update Details Process
As part of the AllAuth testing the user has the ability to update their details. The link to the update form was tested to be working, whilst the content was confirmed to be present within the form correctly. The changes made saved correctly on request confirming that the process works as expected.

## Test Case 027

![Test Case 027](/static/docs/img/testing/tc027.png)

### Registered User Testing - Update Email Process
As part of the AllAuth testing the user has the ability to update their email address. The link to the email update page was tested, along with the links within the email update page. Whilst the templates are customised versions of the allauth templates, the links within them were tested to ensure that allauth was configured correctly.


## Test Case 028

![Test Case 028](/static/docs/img/testing/tc028.png)

### Registered User Testing - Update Password Process
As part of the AllAuth testing the user has the ability to update their password. The functionality was tested to ensure that changes made by the user were applied correctly.


## Test Case 029

![Test Case 029](/static/docs/img/testing/tc029.png)

### Registered User Testing - Delete Account Process
Deleting a user account is an important functionality, especially given EU GDPR regulations. The functionality was tested to ensure that it works correctly and that it only worked when completed correctly.


## Test Case 030

![Test Case 030](/static/docs/img/testing/tc030.png)

### Newsletter Sign Up Process
Mailchimp has been utilised to provide the newsletter sign up functionality. This includes a mailchimp provided code snippet within the footer that allows the user to sign up for a newsletter subscription. To aid assessment I have included screenshots of the completed process to prove its functionality.

<br>

![newsletter signup](/static/docs/img/testing/newsletter-signup.png)

<br>

![mailchimp dashboard activity](/static/docs/img/testing/mailchimp-activity.png)

<br>

![mailchimp dashboard audience](/static/docs/img/testing/mailchimp-audience.png)

<br>

## Test Case 031

![Test Case 031](/static/docs/img/testing/tc031.png)

### Search Functionality
The full functionality of the search bar was tested to ensure that it works as designed. Search results were tested to ensure that the pagination worked correctly where more than five products were returned.

## Test Case 032

![Test Case 032](/static/docs/img/testing/tc032.png)

### Non logged in user -> Shopping process -> Log in prior to checkout
As users are able to login from the checkout form, the process was tested to ensure that should a user login from this link, they did not lose the products in their shopping cart or any other functionality.

## Test Case 033

![Test Case 033](/static/docs/img/testing/tc033.png)

### Employee User - Product Management - Add Product
The Add Product functionality was tested to ensure that it works correctly. It was tested for form validation errors and that when requested products are displayed on the site. The form validation works correctly, however the number of fields required has been kept deliberately light so that flexibility is maintained in the type of products that can be placed on the site. Currently only a description and a price are required fields. This is by design. Adding a product with no image was tested to ensure that the no image placeholder image displays correctly.

## Test Case 034

![Test Case 034](/static/docs/img/testing/tc034.png)

### Employee User - Product Management - Edit Product
The edit product process was tested to ensure that it works correctly. It was tested to ensure that products were not duplicated, and that the form loads the correct product information when an employee attempts to edit it. Normal form validation tests were performed as with the add product tests.

## Test Case 035

![Test Case 035](/static/docs/img/testing/tc035.png)

### Employee User - Product Management - Deactivate / Activate Product
To enable employees to control the products that are available on the site a field was added to the product model called is_active. This boolean field enables products to be toggled between active and inactive. Only active products should appear on the site. Inactive products, whilst not deleted, will not appear on the site. This functionality was tested to ensure that the process an employee follows works correctly and it does prevent inactive products from being shown on the site. The decision was made to provide this functionality rather than delete products as businesses such as this will likely need to maintain records of previous products, so whilst it is possible for products to be deleted, it was not a function built into the site itself.


## Test Case 036

![Test Case 036](/static/docs/img/testing/tc036.png)

### Employee User Testing - Order Management
Customer orders gain a status of confirmed when they first place their order and payment is successful. Therefore it is important that employee's or the site administration team can change the status as required for one of the other preset stages. The entire order management process was tested to ensure that access to the site, order location and status updates were all working as required. A small issue was discovered, that brought the wrong days orders back during testing the previous days orders when the time is between midnight and 1am. This is detailed in the README under the notable bugs section.

## Test Case 037

![Test Case 037](/static/docs/img/testing/tc037.png)

### JavaScript Functionality - Script.js - Navigation bar reorganisation based on screen size
The navigation bar within the main site header contains multiple sections. Depending on the screen size, some of these navigation elements will move into a mobile orientated mobile menu or into a dedicated navigation bar above the main navbar. This reorganisation requires the activation and deactivation of multiple elements depending on the screen size. To test that it worked correctly, other than testing the site on multiple devices, the google dev tools were utilised to ensure that the correct elements moved at the correct breakpoints.

## Test Case 038

![Test Case 038](/static/docs/img/testing/tc038.png)

### JavaScript Functionality - Script.js - Display Search Bar
JavaScript controls the display of the search bar modal when the user clicks on the search icon within the navigation menu. This functionality was tested to ensure that the search bar functionality work as desired on request. It was also tested to ensure that the user could close the search bar when wanted.

## Test Case 039

![Test Case 039](/static/docs/img/testing/tc039.png)

### JavaScript Functionality - Blog.js - Disable Other Buttons when one form is present
To resolve a bug within the HTML validation within the category management section some custom JavaScript was implemented to disable buttons. This prevents an employee user from creating multiple versions of the same form on the page at the same time. Whilst this resolved the HTML validation issue, it was important to test the functionality that was intended worked correctly.

<br>

## Additional Manual Testing

The test cases were performed multiple times during the development of the site with adjustments made to the code logic and functionality based on user feedback.


To navigate back to the main README click [here](README.md)