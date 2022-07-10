# Druid Computers

## Introduction

Druid Computers is a website built on Django using Python, JavaScript, HTML and CSS. The site is a full B2C ecommerce website for a fictional business based in Tramore, Ireland. The business sells PC watercooling components and parts along with other related computer parts. Users of the site can search for products via manual keyword search, filter by category or browse through all products available. They can select differing quantities of products for purchase and add them to their shopping cart, and proceed through a purchase process designed to be simple and with minimal steps. Registered users can add their favourite products to their wishlist, store multiple addresses on the site for easy selection when it is time to checkout, and provide reviews on products they have purchased for other users. The business owner and employees can add, edit and remove products from the site without accessing the admin interface. They can also add, edit and remove blog posts to inform site users of new products or provide how to guides and other useful information. The business owner or employees can also respond to reviews that users have left on the site should they deem necessary, or they can delete the review if necessary.

This is the fifth project for the Code Institute Diploma in Software Development with eCommerce.

The site provides role based permissions for users to interact with a central dataset. It includes user authentication, email validation, Full CRUD functionality for approved users for Products, Categories, Blog Posts and Categories along with Reviews and Responses.

![Screenshot of homepage](/static/docs/img/responsive-site-image.png)

[View the live website on Heroku](https://druid-computers.herokuapp.com/)

Please note: To open any links in this document in a new browser tab, please press CTRL + Click.

## Table of Contents
- [Druid Computers](#druid-computers)
  * [Introduction](#introduction)
  * [Table of Contents](#table-of-contents)
  * [UX](#ux)
    + [Overall Goals](#overall-goals)
    + [The Strategy Plane](#the-strategy-plane)
    + [The Sites Ideal User](#the-sites-ideal-user)
    + [Site Goals](#site-goals)
    + [Epics](#epics)
    + [User Stories](#user-stories)
    + [The Scope Plane](#the-scope-plane)
    + [The Structure Plane](#the-structure-plane)
    + [The Skeleton Plane](#the-skeleton-plane)
      + [Wireframe mock-ups](#wireframe-mock-ups)
      + [Database Schema](#database-schema)
      + [SEO Considerations](#seo-considerations)
  * [The Surface Plane](#the-surface-plane)
  * [Features](#features)
  * [Future Enhancements](#future-enhancements)
  * [Social Media](#social-media-marketing)
  * [Testing](#testing)
  * [Deployment](#deployment)
  * [Credits](#credits)
  * [Acknowledgements](#acknowledgements)

## UX

### Overall Goals
* To provide an ecommerce solution for a small business selling computer products to consumers - B2C
* To enable business employees to maintain and update the site content in line with their needs easily.
* To provide the business owner/manager a degree of control over the site.
* To provide users with a simple product selection and purchase experience.

<br>

### The Strategy Plane
* Druid Computers is a business to consumer B2C ecommerce site for users (consumers browsing products and making purchases) to find and purchase selected products, read reviews and blog posts, whilst for business employees they are able to manage the site content to ensure it is kept upto date with the business needs. The overall design of the site is intended to provide users with a clean and easy to navigate environment whilst providing the level of detail required for the different types of products.

### The Sites Ideal User
* Tech enthusiast searching for new products
* Someone looking to buy a new product for their personal PC build
* Someone looking for inspiration for new things they could add to their PC build

### Site Goals

* To provide users with a place to purchase their watercooling products
* To promote the product range of Druid Computers
* To promote Druid Computers as the preferred site for users to purchase their watercooling products
* To increase the standing of Druid Computers within the watercooling industry and community.

### Epics
13 Epics were created which were then further developed into 49 User Stories. The details on each epic, along with the user stories linked to each one can be found in the project kanban board [here](https://github.com/MattBCoding/druid-pp5/projects/1)

1. Initial Django setup [#1](https://github.com/MattBCoding/druid-pp5/issues/1)
    As a **Developer**, I can **setup the Django Environment**, so that **I can initialise the development environment**
    #### Potential User Stories
        1.	Create Django Project
        2.	Install required packages
        3.	Create first app
        4.	Early Deployment – Late deployment

2. Overall Site Purpose [#2](https://github.com/MattBCoding/druid-pp5/issues/2)
    As a **Site Owner**, I would like **the site to fulfil its purpose**, so that **it is easy to use for users and provides business benefits**
    #### Potential User Stories
        1.	Site structure – SEO, sitemap
        2.	Information sections – About Us, Expertise, Blog Posts, News Stories
        3.	Contact Form
        4.	Accessibility
       5.	Colour Scheme – light/dark mode
       6.	Location Map?
3. User Profile [#3](https://github.com/MattBCoding/druid-pp5/issues/3)
    As a **User**, I would like **to be able to create and maintain an account**, so that **I can order products quickly and easily without having to enter information each time**
    #### Potential User Stories
        1.	Create User Profile / Account
        2.	Edit User Profile / Account
        3.	View User Profile / Account
        4.	Delete User Profile / Account
        5.	Create account using social media login’s
4. User Login / Logout [#4](https://github.com/MattBCoding/druid-pp5/issues/4)
    As a **User**, I would like **to be able to log in and log out of my account**, so that **I can keep my account secure**.
    #### Potential User Stories
        1.	User Login
        2.	User Logout
        3.	Social media Login
5. Product Management [#5](https://github.com/MattBCoding/druid-pp5/issues/5)
    As an **Site Owner**, I would like **employees to be able to manage the products on the site easily**, so that **it is easy to keep the site upto date**
    #### Potential User Stories
        1.	Add products
        2.	Edit Products
        3.	Delete Products
        4.	Order Status Changes
6. Stock System [#6](https://github.com/MattBCoding/druid-pp5/issues/6)
    As a **Site Owner**, I would like **employees to be able to control the stock levels displayed on the site**, so that **customers can see if products are in stock, or when they will be back in stock to encourage orders**
    #### Potential User Stories
        1.	Add stock levels
        2.	Edit stock levels
7. Product Viewing [#7](https://github.com/MattBCoding/druid-pp5/issues/7)
    As a **User**, I would like **to be able to view different levels of product information**, so that **I can select which amount of detail I want**
    #### Potential User Stories
        1.	View full product details
        2.	View small product card with summary information
        3.	Search for a product
        4.	View products by category
        5.	View multiple images of a product
8. Product Wishlist [#8](https://github.com/MattBCoding/druid-pp5/issues/8)
    As a **User**, I would like **to have a wishlist of products**, so that **I can quickly access them in the future when I want to purchase them**
    #### Potential User Stories
        1.	Add product to wishlist
        2.	Remove product from wishlist
        3.	View wishlist
        4.	Delete wishlist
        5.	View product details from wishlist
9. Shopping Cart [#9](https://github.com/MattBCoding/druid-pp5/issues/9)
    As a **User**, I would like **to be able to add/remove products to my shopping cart**, so that **I can control the list products I am going to purchase**
    #### Potential User Stories
        1.	Add product to cart
        2.	Edit products in cart
        3.	View the products in my cart
        4.	Proceed to checkout
        5.	Save cart for later
10. Checkout [#10](https://github.com/MattBCoding/druid-pp5/issues/10)
    As a **User**, I would like  **to be able to purchase the items I have selected**, so that **I may place my order**
    #### Potential User Stories
        1.	Capture delivery and billing address
        2.	Save address to profile
        3.	Create account for unregistered users
        4.	Login if registered and return to cart 
        5.	Capture payment details
        6.	Authorise payment
        7.	Order confirmation email
        8.	Order confirmation page
        9.	Order number generation
11. Order Status [#11](https://github.com/MattBCoding/druid-pp5/issues/11)
    As a **User**, I would like **to check on the status of my order**, so that **I know when it has shipped or will be arriving**
    #### Potential User Stories
        1.	Users can access order status from their order-number
        2.	Registered users can access from their account
12. Product Reviews [#12](https://github.com/MattBCoding/druid-pp5/issues/12)
    As a **User**, I would like ** to read, add, edit, delete reviews for products that I have purchased**, so that **I can provide feedback to the company, and other users**
    #### Potential User Stories
        1.	Create a product review
        2.	Edit a product review
        3.	Read product reviews
        4.	Delete product reviews
        5.	Respond to product review
13. Web Marketing [#13](https://github.com/MattBCoding/druid-pp5/issues/13)
    As a **User**, I would like **to subscribe to a newsletter**, so that **I can stay up to date with the company easily**
    #### Potential User Stories
        1.	Email Newsletter sign up
        2.	Ability to unsubscribe from newsletter


### User Stories

|User Stories| | |49|
|----|----|----|----|
|Must Have's| | | 94pts |
|Should Have's| | | 56pts |
|Could Have's| | | 70pts |
|**Total Story Pts**| | |**220 pts**|

|Completed Pts| | |Uncompleted Pts|
|----|----|----|----|
|172| | | 48|

From the Epics, 49 User stories were developed. Each story was assigned a classification of Must-Have, Should-Have, Could-Have or Won't Have. Each story was also assigned user story points, based on my best estimation for the time/difficulty of completing each story. A combination of being new to story estimation, inexperience with Django and time constraints during development left me completing 172 story points from the initial total of 220. From the initial 220 points, 70 were for Could Have stories. A number of these stories were created based on an ideal scenario of building out the project whilst I knew in the time available it would be unlikely I would complete those stories. I will however revisit those left incomplete at a later time for future development of the project. The full list of User Stories, seperated by those completed and those pushed to a future release is available on the project [kanban board](https://github.com/MattBCoding/druid-pp5/projects/1).

These are the user stories that were completed for the projects first release, by Epic.

1. Initial Django setup
    * [US#14](https://github.com/MattBCoding/druid-pp5/issues/14) - Initial Setup - As a Developer, I can setup Django and install the supporting libraries predicted to be needed, so that I am ready to start development
    * [US#15](https://github.com/MattBCoding/druid-pp5/issues/15) - Secure the Keys - As a Developer, I want to setup the Django environment to secure the secret keys, so that I do not expose the keys in an insecure way
    * [US#16](https://github.com/MattBCoding/druid-pp5/issues/16) - Deployment - As a Developer, I want to deploy the app to Heroku, so that I can confirm everything works before development of the site and to enable continuous testing within the production environment

<br>

2. Overall Site Purpose
    * [US#17](https://github.com/MattBCoding/druid-pp5/issues/17) - SEO - As a Site Owner, I would like The site to have all the content needed to perform well in SEO, so that ultimately the site has the ability to perform well in search results and can be found
    * [US#18](https://github.com/MattBCoding/druid-pp5/issues/18) - Privacy Policy - As a Site Owner, I need to Provide a privacy policy, so that our site users know how we will protect and utilise their data
    * [US#19](https://github.com/MattBCoding/druid-pp5/issues/19) - Contact Us - As a User, I would like to be able to contact the company prior to making my purchase, so that I can ask them a question about one of the products
    * [US#59](https://github.com/MattBCoding/druid-pp5/issues/59) - Create Blog Post - As a Employee, I would like to be able to add a blog post to the site, so that we can easily add guides, or informative articles to the site
    * [US#60](https://github.com/MattBCoding/druid-pp5/issues/60) - Edit Blog Post - As an Employee, I would like to be able to edit blog posts already posted to the site, so that if any errors are made they can be corrected easily
    * [US#61](https://github.com/MattBCoding/druid-pp5/issues/61) - View Blog Post - As a User, I would like to be able to read blog posts full of useful information, so that I can keep upto date on the company and learn new information
    * [US#62](https://github.com/MattBCoding/druid-pp5/issues/62) - Delete Blog Post - As a Employee, I would like to be able to delete a blog post, so that in the event we need to remove one completely we can take it down from the site

<br>

3. User Profile
    * [US#20](https://github.com/MattBCoding/druid-pp5/issues/20) - Create Account - As a User, I would like to be able to create an account, so that I don’t have to enter my details every time I place an order
    * [US#21](https://github.com/MattBCoding/druid-pp5/issues/21) - Edit Account - As a User, I would like to be able to edit the details/address stored on my account, so that If I move, or if I want to use more than one address, I can store them all
    * [US#22](https://github.com/MattBCoding/druid-pp5/issues/22) - View Account - As a User, I would like to be able to view the details stored on my account, so that I can review what is stored
    * [US#23](https://github.com/MattBCoding/druid-pp5/issues/23) - Delete Account - As a User, I would like to be able to delete my account, so that I have full control over the information that is stored about me

<br>

4. User Login / Logout
    * [US#25](https://github.com/MattBCoding/druid-pp5/issues/25) - Account Login - As a User, I would like to be able to login to my account, so that I can access the advantages of having an account
    * [US#26](https://github.com/MattBCoding/druid-pp5/issues/26) - Account Logout - As a User, I would like to be able to log out of my account, so that I can keep my account secure

<br>

5. Product Management
    * [US#28](https://github.com/MattBCoding/druid-pp5/issues/28) - Add Products - As an Store Owner, I would like employees to be able to add new products to the site easily, so that the site can be kept upto date
    * [US#29](https://github.com/MattBCoding/druid-pp5/issues/29) - Edit Products - As a Store Owner, I would like employees to be able to edit product details on the site easily, so that any corrections needed can be carried out when required
    * [US#31](https://github.com/MattBCoding/druid-pp5/issues/31) - Order Update - As a Site Owner, I would like employees to be able to update customer orders, so that customers are kept informed as to the status of their order

<br>

6. Stock System

<br>

7. Product Viewing
    * [US#35](https://github.com/MattBCoding/druid-pp5/issues/35) - View Product Details - As a User, I would like to be able to view the full details for a product, so that I can make an informed purchase decision
    * [US#36](https://github.com/MattBCoding/druid-pp5/issues/36) - Product Cards - As a User, I would like to be able to view summary details of a product, so that I can quickly narrow down the products that I am interested in
    * [US#37](https://github.com/MattBCoding/druid-pp5/issues/37) - Product Search - As a User, I would like to be able to search for products, so that I can find the product I am looking for easily
    * [US#38](https://github.com/MattBCoding/druid-pp5/issues/38) - View Products by Category - As a User, I would like to be able to view all products belonging to a set category, so that I can compare those products easily with each other and see what options are available
    * [US#39](https://github.com/MattBCoding/druid-pp5/issues/39) - Product Images - As a User, I would like to look at images of products from multiple angles, so that I have a good idea of what the product will look like on delivery

<br>

8. Product Wishlist
    * [US#40](https://github.com/MattBCoding/druid-pp5/issues/40) - Add Product to Wishlist - As a User, I would like to be able to add products I want to buy in the future to a wishlist, so that I can quickly access the products at a later date
    * [US#41](https://github.com/MattBCoding/druid-pp5/issues/41) - Remove product from wishlist - As a User, I would like to be able to remove products from my wishlist, so that I can remove products that I no longer wish to purchase in the future
    * [US#42](https://github.com/MattBCoding/druid-pp5/issues/42) - Access products from wishlist - As a User, I would like to be able to access product details from my wishlist, so that I can easily purchase them when wanted

<br>

9. Shopping Cart
    * [US#43](https://github.com/MattBCoding/druid-pp5/issues/43) - Add to Cart - As a User, I would like to be able to add products that I want to buy to my shopping cart, so that I can proceed to purchase them
    * [US#44](https://github.com/MattBCoding/druid-pp5/issues/44) - Edit Card Contents - As a User, I would like to be able to adjust quantity of items in my cart, so that I can only proceed with the correct amount of products that I want to buy
    * [US#45](https://github.com/MattBCoding/druid-pp5/issues/45) - View Cart - As a User, I would like to be able to view the contents of my shopping cart, so that I can confirm the details prior to proceeding to purchase
    * [US#47](https://github.com/MattBCoding/druid-pp5/issues/47) - Proceed to Checkout - As a User, I would like to be able to progress to purchasing my items, so that I can complete my transaction

<br>

10. Checkout
    * [US#48](https://github.com/MattBCoding/druid-pp5/issues/48) - Fill out address details for checkout - As a User, I would like to be able to provide my details, so that I can complete my order
    * [US#50](https://github.com/MattBCoding/druid-pp5/issues/50) - Payment - As a User, I would like to be able to use my credit card to make the purchase, so that I can pay for the purchase easily
    * [US#51](https://github.com/MattBCoding/druid-pp5/issues/51) - Order Confirmation - As a User, I want to be taken to a confirmation page when my order is completed, so that it is clear my order has gone through

<br>

11. Order Status
    * [US#52](https://github.com/MattBCoding/druid-pp5/issues/52) - Check Order Status - As a User, I would like to be able to check on the status of my order, so that I know when it has shipped or when it will be arriving

<br>

12. Product Reviews
    * [US#53](https://github.com/MattBCoding/druid-pp5/issues/53) - Create Product Review - As a User, I would like to create a review for a product that I have purchased, so that I can share my opinion with other buyers and the company
    * [US#54](https://github.com/MattBCoding/druid-pp5/issues/54) - Edit Product Review - As a User, I would like to be able to edit a review I have written, so that I can correct any mistakes that I may have made
    * [US#55](https://github.com/MattBCoding/druid-pp5/issues/55) - Read Reviews - As a User, I would like to be able to read other people’s reviews of a product prior to making a purchase decision, so that I can make an informed decision
    * [US#56](https://github.com/MattBCoding/druid-pp5/issues/56) - Delete Review - As a User, I want to be able to delete my review of a product, so that I have the option to remove it should I so choose
    * [US#57](https://github.com/MattBCoding/druid-pp5/issues/57) - Respond to Review - As an Employee, I want to be able to respond to a user’s review, so that where appropriate, concerns or compliments can be responded to.    
                               
<br>

13. Web Marketing
    * [US#58](https://github.com/MattBCoding/druid-pp5/issues/58) - Email Capture - As a Site Owner, I would like to capture user emails, so that I can use them for marketing newsletters to promote new products

### The Scope Plane

<br>

#### Opportunities
Arising from user stories
| Opportunities | Importance | Viability / Feasibility
| ------ | :------: | :------: |
| **Provide users the ability to create an account** | 5 | 5 |
| **Provide users the ability to save address information for easier checkout** | 5 | 5 |
| **Provide users the ability to edit their account** | 5 | 5 |
| **Provide users the ability to delete their account** | 5 | 5 |
| **Provide users the ability to login to their account** | 5 | 5 |
| **Provide users the ability to logout from their account** | 5 | 5 |
| **Provide users the ability to use a social media account to create their account** | 3 | 5 |
| **Provide users the ability to login to their account using a social media account** | 3 | 5 |
| **Provide users the ability to view product summary information** | 5 | 5 |
| **Provide users the ability to view product detailed information** | 5 | 5 |
| **Provide users the ability to add products to their cart** | 5 | 5 |
| **Provide users the ability to edit the quantity of products in their cart** | 5 | 5 |
| **Provide users the ability to remove products from their cart** | 5 | 5 |
| **Provide users the ability to save their cart for future access** | 3 | 5 |
| **Provide users the ability to progress to checkout** | 5 | 5 |
| **Provide users the ability to enter their information to checkout** | 5 | 5 |
| **Provide users the ability to check the status of their order** | 5 | 5 |
| **Provide employees the ability to update the status of an order** | 5 | 5 |
| **Provide employees the ability to create product listings** | 5 | 5 |
| **Provide employees the ability to edit product listings** | 5 | 5 |
| **Provide employees the ability to remove product listings** | 5 | 5 |
| **Provide employees the ability to create informative blog posts** | 5 | 5 |
| **Provide employees the ability to create categories for blog posts** | 5 | 5 |
| **Provide employees the ability to edit blog posts** | 5 | 5 |
| **Provide employees the ability to delete blog posts** | 5 | 5 |
| **Provide users the ability to read informative blog posts** | 5 | 5 |
| **Provide users the ability to create reviews** | 5 | 5 |
| **Provide users the ability to edit reviews** | 5 | 5 |
| **Provide users the ability to view reviews** | 5 | 5 |
| **Provide users the ability to delete reviews** | 5 | 5 |
| **Provide employees the ability to respond to reviews** | 5 | 5 |
| **Provide employees the ability to edit review responses** | 5 | 5 |
| **Provide employees the ability to remove reviews** | 5 | 5 |
| **Provide employees the ability to add stock for a product** | 3 | 5 |
| **Provide employees the ability to edit stock levels** | 3 | 5 |
| **Provide employees the ability to view stock levels** | 3 | 5 |
| **Provide users the ability to rate a product** | 3 | 5 |
| **Provide users the ability to save a product to their wishlist** | 3 | 5 |
| **Provide users the ability to remove a product from their wishlist** | 3 | 5 |
| **Provide users the ability to search the site for products** | 4 | 5 |
| **Provide users the ability to access the site on any device** | 5 | 5 |

**Features planned:**
* User Profile - Create, Read, Update and Delete
* User Address - Create, Read, Update and Delete
* User Wishlist - Create, Read, Update and Delete
* Users can login to their account, change their password, email address and delivery address
* Users can reset their password if they forget it
* Users can logout of their account
* Products - Create, Read, Update and Delete
* Product Search - by category and keyword
* Products - View product details or summary information
* Shopping Cart - Add, Update and Remove products from the shopping cart
* Checkout - Enter delivery information and payment information
* Payment Processing - Successfully process payment information and confirm orders
* Order Confirmation - Confirm order information on payment success
* Order Tracking - Users can track order status for individual orders
* Blog - Create, Read, Update and Delete
* Reviews - Create, Read, Update and Delete
* Review responses - Create, Read, Update and Delete
* Users need to be registered and logged in to access product wishlist, saving addresses, prior order information and the ability to provide reviews.
* Email newsletter subscription - Ability to subscribe to a company newsletter for marketing purposes.
* Contact Us - Ability for all users to contact the company directly.
* Responsive Design - the site needs to be fully responsive to cover the wide variety of devices users may use to access it
<br>
<br>

### The Structure Plane

<br>
<details>
<summary>
US#14 - Initial Setup - As a Developer, I can setup Django and install the supporting libraries predicted to be needed, so that I am ready to start development
</summary>
<br>
<h4>Implementation:</h4>
<br>
<ul>
<li>Install Django</li>
<li>Install required libraries, external and internal packages</li>
<li>Create requirements file to track dependencies</li>
<li>Create the first app</li>
</ul>
</details>

<br>

<details>
<summary>
US#15 - Secure the Keys - As a Developer, I want to setup the Django environment to secure the secret keys, so that I do not expose the keys in an insecure way
</summary>
<br>
<h4>Implementation:</h4>
<br>
<ul>
<li>Create an env.py file to store the environment variables</li>
<li>Amend Django to point to the new location for the secret keys</li>
<li>Add the env.py file to the .gitignore file so that it does not get pushed to GitHub</li>
</ul>
</details>

<br>

<details>
<summary>
US#16 - Deployment - As a Developer, I want to deploy the app to Heroku, so that I can confirm everything works before development of the site and to enable continuous testing within the production environment
</summary>
<br>
<h4>Implementation:</h4>
<br>
<ul>
<li>Create a new Heroku app</li>
<li>Add the database to the app resources</li>
<li>Add the secret key's to the Heroku config vars</li>
<li>Configure the settings.py file to point at the correct env.py file in development, the os in deployment and adjust the database section to point at the correct database url from Heroku in deployment</li>
<li>Add the Amazon AWS S3 bucket details to the env.py file and to the Heroku config vars. Access Key and Secret Access Key.</li>
<li>Add the email user details and password to the env.py file and to the Heroku config vars</li>
<li>Add the stripe details to the env.py file and to the Heroku config vars. Public key, secret key and wh-secret</li>
</ul>
</details>

<br>

<details>
<summary>
US#17 - SEO - As a Site Owner, I would like The site to have all the content needed to perform well in SEO, so that ultimately the site has the ability to perform well in search results and can be found
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that the site is deployed, When the spiders visit the site, then there is a sitemap to guide them.</li>
<li>Given that content is written for the site, When it is written, then the keyword research is utilised to ensure relevant information is included</li>
</ul>
<br>
<h4>Implementation:</h4>
<br>
<ul>
<li>Conduct Keyword Research prior to planning out the site</li>
<li>From keyword research plan content requirements for the site</li>
<li>From keyword research plan site content</li>
<li>Create sitemap.xml file utilising www.xml-sitemaps.com</li>
<li>Place sitemap.xml file in the root directory</li>
<li>Create robots.txt file</li>
</ul>
</details>

<br>

<details>
<summary>
US#18 - Privacy Policy - As a Site Owner, I need to Provide a privacy policy, so that our site users know how we will protect and utilise their data
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that the site is ready for deployment, When we collect data on our users, Then we need to protect that data in line with GDPR requirements And, inform our users how we are using their data</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Generate a privacy policy for the site</li>
<li>Include the privacy policy within the site</li>
</ul>
</details>

<br>

<details>
<summary>
US#19 - Contact Us - As a User, I would like to be able to contact the company prior to making my purchase, so that I can ask them a question about one of the products
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am a user on the website, When I want to contact the company to ask a question, Then there is an easily accessible method for me to do so</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop a contact form for users to get in touch with the company</li>
<li>Link the form submission with an email system so that messages sent will arrive at the company and can be responded to</li>
</ul>
</details>

<br>

<details>
<summary>
US#59 - Create Blog Post - As a Employee, I would like to be able to add a blog post to the site, so that we can easily add guides, or informative articles to the site
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I have an employee account, When I am logged into my account, Then I have the ability to create a new blog post</li>
<li>Given that I am logged into my employee account, When I navigate to create a new blog post, Then I have a form to fill out to create my blog post</li>
<li>Given that I am a logged in employee, When I successfully complete the blog post form and submit it, Then a new blog post is created and published to the site</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Create blog post model</li>
<li>Create blog post form for employees to add blog posts to the site</li>
<li>Develop validation to ensure that the blog post is completed correctly</li>
<li>Restrict access to blog post form page to employees</li>
<li>Develop backend processes to process the form and publish it to the site</li>
</ul>
</details>

<br>

<details>
<summary>
US#60 - Edit Blog Post - As an Employee, I would like to be able to edit blog posts already posted to the site, so that if any errors are made they can be corrected easily
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am logged in employee, When I view a blog post, Then I have the option to edit it</li>
<li>Given that I am a logged in employee, When I select the option to edit a blog post, Then I am taken to a form with the blog post information in it so I can edit the section I want</li>
<li>Given that I am a logged in employee, When I edit a blog post, Then on submitting the edited form the blog post is updated</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop the option for employees to edit blog posts</li>
<li>Develop a form for employees to edit the blog post</li>
<li>Develop validation for the form to ensure blog post information is complete</li>
</ul>
</details>

<br>

<details>
<summary>
US#61 - View Blog Post - As a User, I would like to be able to read blog posts full of useful information, so that I can keep upto date on the company and learn new information
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am a user on the site, When I navigate to the blog post page, Then I am presented with all the blog posts that are available</li>
<li>Given that I am a user on the blog posts page, When I click on a blog post, Then I am taken to the full post details</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop a blog post page to display all the blog posts</li>
<li>Develop blog post cards to display a summary of each post</li>
<li>Develop a blog post detail page to display the full post</li>
<li>Link the blog card to the detail page for each blog post</li>
<li>Display the blog posts in date order, most recent first</li>
</ul>
</details>

<br>

<details>
<summary>
US#62 - Delete Blog Post - As a Employee, I would like to be able to delete a blog post, so that in the event we need to remove one completely we can take it down from the site
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am a logged in employee, When I navigate to a blog post, Then I have the option to remove the post</li>
<li>Given that I am a logged in employee, When I select the remove option on a blog post, Then the post is removed from the site</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop an option in the blog post edit page to delete the post</li>
<li>Develop the functionality to delete the post from the database</li>
<li>Restrict access to the functionality to employee users</li>
</ul>
</details>

<br>

<details>
<summary>
US#20 - Create Account - As a User, I would like to be able to create an account, so that I don’t have to enter my details every time I place an order
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am an unregistered user, And, I am on the user registration page, When I enter my email address and password, And, I click on the register button, Then the system creates me an account, And, it tells me that my account has been created</li>
<li>Given that I have an account, And, I have items in my cart, When I navigate to checkout, Then I have my address information ready to be used</li>
<li>Given that I have an account, And, I try to navigate to the register page, When I enter my email address and password, And, I click on the register button, Then the site tells me that I already have an account</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop the ability for users to register for an account</li>
<li>Develop ability for users to save details to their account such as address</li>
<li>Prevent multiple accounts being created for the same email address</li>
</ul>
</details>

<br>

<details>
<summary>
US#21 - Edit Account - As a User, I would like to be able to edit the details/address stored on my account, so that If I move, or if I want to use more than one address, I can store them all
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I have a user profile, And, I am logged into my profile, When I navigate to my profile, Then I have the ability to add different addresses on my account</li>
<li>Given that I have a user profile, And I am logged in, When I navigate to my profile, And, I have more than one address stored, Then I can select one to be the default address</li>
<li>Given that I have a user profile, And, I am logged into my profile, When I navigate to my profile, Then I have the ability to edit the addresses</li>
<li>Given that I have a user profile, And, I am logged into my profile, When I navigate to my profile, Then I have the option to delete the addresses</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop the ability for users to save addresses to their profile</li>
<li>Develop the ability for users to store more than one address on their profile</li>
<li>Develop the ability for users to set one address as default</li>
<li>Develop the ability for users to edit the addresses on their profile</li>
<li>Develop the ability for users to delete the addresses on their profile</li>
</ul>
</details>

<br>

<details>
<summary>
US#22 - View Account - As a User, I would like to be able to view the details stored on my account, so that I can review what is stored
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I have a user account, When I am logged into my account, Then I have an option to view my account</li>
<li>Given that I have a user account, And, I am logged in, When I navigate to view my details, Then everything that is stored within my account is available to be viewed</li>
<li>Given that I have a user account, When I navigate to the url to view my account whilst not logged in, Then I am redirected to the login page and i'm unable to view the details without being logged in</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop a link in the menu that takes logged in users to their profile</li>
<li>Develop a link within the user profile page that they can use to view all other information associated with the account - previous orders, wishlist items</li>
<li>Restrict access to account details to logged in users - specifically the user whose details they are</li>
</ul>
</details>

<br>

<details>
<summary>
US#23 - Delete Account - As a User, I would like to be able to delete my account, so that I have full control over the information that is stored about me
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I have a user account, When I view my account details whilst logged in, Then I have the option to delete my account</li>
<li>Given that I have a user account, And, I am on my account details page, When I select to delete my account, And, I confirm the deletion request, Then my account is deleted</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>On the user profile page provide an option to delete account</li>
<li>Require a second confirmation for account deletion</li>
<li>Develop a method to delete the account when the user requests it to be deleted - will need to keep order history seperate for company records</li>
</ul>
</details>

<br>

<details>
<summary>
US#25 - Account Login - As a User, I would like to be able to login to my account, so that I can access the advantages of having an account
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am a registered user, When I navigate to the login page, Then I can enter my details to login to my account</li>
<li>Given that I am a registered user, When I navigate to the login page and enter my details, And, I click login, Then I am logged into my account and I am able to see a visual confirmation that I am now logged in</li>
<li>Given that I am a registered user, And, I try to log into my account, When I enter the wrong information, Then the site informs me that the information was incorrect and prevents my logging in</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop a link to a login page</li>
<li>Develop a login form for users to confirm their login details</li>
<li>Develop form validation to ensure the data is entered correctly</li>
<li>Develop a method to validate the data entered matches a user account</li>
<li>Develop a redirect so unlogged in users are redirected to the login page when trying to access pages that require the user to be logged in</li>
</ul>
</details>

<br>

<details>
<summary>
US#26 - Account Logout - As a User, I would like to be able to log out of my account, so that I can keep my account secure
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am logged into my account, When I click on the logout link, Then I am asked to confirm to logout</li>
<li>Given that I am a logged in user who has clicked logout, When I confirm I want to logout, Then I am logged out of my account</li>
<li>Given that I am a registered user, who has signed out of my account, When I use the browser navigation buttons such as back button, Then I cannot access information which requires me to be signed in</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop link for users to access logout functionality</li>
<li>Develop logout confirmation form to log users out</li>
<li>Develop a redirect so if a user signs out whilst on a page requiring a user to be logged in, it redirects them appropriately</li>
</ul>
</details>

<br>

<details>
<summary>
US#28 - Add Products - As an Store Owner, I would like employees to be able to add new products to the site easily, so that the site can be kept upto date
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am an employee, When I log into the site, Then I should have additional stock management options available</li>
<li>Given that I am a logged in employee, When I select add product, Then I should be directed to a form that allows me to add a new product to the site</li>
<li>Given that I am a logged in employee, And, I have completed the form to add a product, When I submit the form, Then the new product should appear on the site.</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop a separate navigation bar for employee users to allow access to other site areas</li>
<li>Develop a form for employees to add products to the site</li>
<li>Develop validation to ensure that product information is completed correctly</li>
<li>Develop the backend to process the form data and create a new product file/page to be added to the site</li>
</ul>
</details>

<br>

<details>
<summary>
US#29 - Edit Products - As a Store Owner, I would like employees to be able to edit product details on the site easily, so that any corrections needed can be carried out when required
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am an employee, When I log into the site, Then I should have the option to edit a product</li>
<li>Given that I am a logged in employee, When I select edit product, Then I have the ability to choose which product to edit</li>
<li>Given that I am a logged in employee, When I select which product to edit, Then I am directed to a form from which I can edit the existing product data</li>
<li>Given that I am a logged in employee, When I edit product details within the form and submit the changes, Then the changes I made appear on the site</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop the option for employees to edit products</li>
<li>Develop a page for employees to select which product to edit</li>
<li>Develop a form for employees to edit the product data</li>
<li>Develop validation for the form to ensure product information is complete</li>
</ul>
</details>

<br>

<details>
<summary>
US#31 - Order Update - As a Site Owner, I would like employees to be able to update customer orders, so that customers are kept informed as to the status of their order
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am an employee who is logged in, When I am on the site, I can access customer orders, Then I can select an order to update the status</li>
<li>Given that I am an employee who is logged in, And, I have selected an order to update its status, When I am on the order details I have the new status options available, Then when I select one, the status updates</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop the option for employees to update order status</li>
<li>Develop the display of orders for employees to filter through</li>
<li>Develop filtering capability to ease accessing the correct order for employees</li>
<li>Develop an order status update form for employees to update the order status</li>
<li>Develop validation for the order status form</li>
<li>Restrict access to the order status screens to employees</li>
</ul>
</details>

<br>

<details>
<summary>
US#35 - View Product Details - As a User, I would like to be able to view the full details for a product, so that I can make an informed purchase decision
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am a user on the site, When I navigate to a product listing, Then the full details of the product are available</li>
<li>Given that I am a user on the all products page, When I click on a product summary card, Then I am taken to a page with the full details on the product</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop a product full details page template</li>
<li>Develop product card template</li>
<li>Link product card with product detail page</li>
</ul>
</details>

<br>

<details>
<summary>
US#36 - Product Cards - As a User, I would like to be able to view summary details of a product, so that I can quickly narrow down the products that I am interested in
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am a user, When I search for a product, Then the products are displayed in a summary format</li>
<li>Given that I am a user, When I view the search results or product listing page, Then all products matching the query, or all are visible</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop product summary details page template</li>
<li>Develop pagination so that product summary page doesn't get too large in the future</li>
<li>Develop user controlled filter to allow for more or less products to appear on each page</li>
</ul>
</details>

<br>

<details>
<summary>
US#37 - Product Search - As a User, I would like to be able to search for products, so that I can find the product I am looking for easily
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am a User, When I am on the site, Then I have easy access to search functionality</li>
<li>Given that I am a user, When I search for a product by name, Then the product appears in the search results</li>
<li>Given that I am a user, When I search for a product by category, Then all the products in that category appear</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop search bar functionality that is easy to access on every page</li>
<li>Develop search query filter to search by product name</li>
<li>Develop search query filter to search by category</li>
</ul>
</details>

<br>

<details>
<summary>
US#38 - View Products by Category - As a User, I would like to be able to view all products belonging to a set category, so that I can compare those products easily with each other and see what options are available
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am a user, When I want to quickly look at all products in a given category, Then there is a link in the navigation bar to quickly access them</li>
<li>Given that I am a user, When I click on the category link, Then all the products related to that category are displayed</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop navigation links for each category of product</li>
<li>Develop query for each link to automatically apply filter to product results for each category to be used for the nav links</li>
</ul>
</details>

<br>

<details>
<summary>
US#39 - Product Images - As a User, I would like to look at images of products from multiple angles, so that I have a good idea of what the product will look like on delivery
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am a user, When I view a products full detail page, Then I have multiple images to view</li>
<li>Given that I am a user, When I view the products details page on a mobile device, Then it is easy to scroll through the images available</li>
<li>Given that I am a user, When I select another image to view, Then the image becomes large enough to see</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop an image carousel or alternative image scroller to allow multiple images to appear for each product</li>
<li>Include image carousel on products that have more than one image available</li>
<li>Image carousel needs to be accessible via a touch device</li>
<li>Image carousel needs to be accessible via a keyboard</li>
<li>Develop control for user to select which image displays</li>
</ul>
</details>

<br>

<details>
<summary>
US#40 - Add Product to Wishlist - As a User, I would like to be able to add products I want to buy in the future to a wishlist, so that I can quickly access the products at a later date
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am a registered user, When I view a product, Then I have the option to add the product to my wishlist</li>
<li>Given that I am an unregistered user, When I view a product, And, I try to add the product to my wishlist, Then I receive a message telling me to login/register to save products to your wishlist</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop a wishlist model linked to user</li>
<li>Develop a simple button that adds products to users wishlist</li>
<li>Develop a message to unregistered users to inform them that the wishlist is available to registered/logged in users</li>
<li>Develop a visual indicator to users to inform them that the product is on their wishlist</li>
</ul>
</details>

<br>

<details>
<summary>
US#41 - Remove product from wishlist - As a User, I would like to be able to remove products from my wishlist, so that I can remove products that I no longer wish to purchase in the future
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am a registered user, When I navigate to my wishlist, Then I can remove products from my wishlist</li>
<li>Given that I am a registered user, When I navigate to a product that is on my wishlist, Then I can remove it from my wishlist</li>
<li>Given that I am a registered user, When I want to access my wishlist, Then there is a convenient link easily located to access it</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop a wishlist page template to display user saved items</li>
<li>Develop ability for users to remove products from the wishlist on the wishlist page</li>
<li>Develop ability for user to remove products from the product page</li>
<li>Develop link for users to access wishlist page easily</li>
<li>Develop ability for users to easily remove products from wishlist that they have purchased</li>
</ul>
</details>

<br>

<details>
<summary>
US#42 - Access products from wishlist - As a User, I would like to be able to access product details from my wishlist, so that I can easily purchase them when wanted
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am a registered user, And, I have products on my wishlist, When I visit my wishlist, And, I click on one of the products, Then I am redirected to the product information page for that product</li>

</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop link from product details on user wishlist template to product detail page for that product</li>

</ul>
</details>

<br>

<details>
<summary>
US#43 - Add to Cart - As a User, I would like to be able to add products that I want to buy to my shopping cart, so that I can proceed to purchase them
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am an unregistered user, When I find a product I want to purchase, And, I click on add to cart, Then the product is added to my shopping cart, ready for me to purchase</li>
<li>Given that I am a registered logged in user, When I find a product I want to purchase, and click add to cart, Then the product is added to my shopping cart, ready for me to purchase</li>
<li>Given that I am a user, When I click add to cart on a product I have previously added to my cart, Then the quantity of that product in my cart increases by the amount I just added</li>
<li>Given that I am a registered user who is not logged in, When I add products to my cart, And, then log in to my account, Then the products I added remain in my cart ready for me to purchase</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop a shopping cart functionality to track products users want to purchase</li>
<li>Enable the cart to be utilised when a user is logged in or not</li>
<li>Develop check on add to cart functionality for product already existing in cart - if product exists, increase quantity appropriately</li>
<li>Develop ability for logged out user to login without losing cart contents</li>
</ul>
</details>

<br>

<details>
<summary>
US#44 - Edit Card Contents - As a User, I would like to be able to adjust quantity of items in my cart, so that I can only proceed with the correct amount of products that I want to buy
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am a User, And, I have added products to my cart, When I view the cart, Then I can adjust the quantity of each item individually</li>
<li>Given that I am a user, When I view the items in my cart, Then I have the ability to remove an item completely</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop the ability to adjust the item quantity within the shopping cart</li>
<li>Develop the ability to remove items from the shopping cart</li>
</ul>
</details>

<br>

<details>
<summary>
US#45 - View Cart - As a User, I would like to be able to view the contents of my shopping cart, so that I can confirm the details prior to proceeding to purchase
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am a User, When I click on my shopping cart, Then I am taken to a page with the details of all the products I have within my cart</li>
<li>Given that I am a user, When I add a product to my cart, Then I have a visual confirmation that the product is now in my cart</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop template page for viewing the shopping cart</li>
<li>Develop temporary preview of shopping cart to display when adding products to the cart</li>
</ul>
</details>

<br>

<details>
<summary>
US#47 - Proceed to Checkout - As a User, I would like to be able to progress to purchasing my items, so that I can complete my transaction
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am a user, When I have reviewed my shopping cart, Then I have the option to proceed to purchase them</li>
<li>Given that I am a user, When I have added products to my shopping cart, Then I have the option to proceed to purchase, without having to confirm the details of the products within my cart</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop checkout link on shopping cart page</li>
<li>Develop checkout link on shopping cart preview</li>
</ul>
</details>

<br>

<details>
<summary>
US#48 - Fill out address details for checkout - As a User, I would like to be able to provide my details, so that I can complete my order
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am a user, When I proceed to checkout, Then I am asked to enter my delivery and billing address</li>
<li>Given that I am a user, When I enter my billing address, Then I can use the same address for delivery without having to fill it out twice</li>
<li>Given that I am a logged in user, When I enter my address details, Then I have the option to save the details I entered to my account</li>
<li>Given that I am a logged in user, When I get to the enter billing and delivery address screen, Then I have the option to use previously saved address details</li>
<li>Given that I am a registered user, not logged in, when I progress to enter the address information - I have the ability to login then return to the same screen and use previously saved address details</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop checkout page to collect billing and delivery address details</li>
<li>Enable option to use billing address for delivery address</li>
<li>Enable option for users to save address details to their account</li>
<li>Enable link to login which redirects back to checkout page</li>
<li>Enable logged in users to select previously saved addresses instead of manual completion of the form</li>
</ul>
</details>

<br>

<details>
<summary>
US#50 - Payment - As a User, I would like to be able to use my credit card to make the purchase, so that I can pay for the purchase easily
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am a user, When purchasing my items, Then I have the ability to enter my credit card details on a secure form</li>
<li>Given that I am a user, When I enter my card details to pay for the transaction, Then the system will process the payment</li>
<li>Given that I am a user, When I process the payment using my card details, Then I am kept informed as to the status as it progresses</li>
<li>Given that I am a user, When my payment fails, Then I am returned to the checkout page without losing all the inputted information</li>
<li>Given that I am a user, When I checkout and my payment is successful, Then I am taken to a confirmation page</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop secure form to capture credit card details</li>
<li>Develop link to payment processor</li>
<li>Develop message system to keep customer informed on processing status</li>
<li>Develop redirect to appropriate page depending on payment outcome</li>
</ul>
</details>

<br>

<details>
<summary>
US#51 - Order Confirmation - As a User, I want to be taken to a confirmation page when my order is completed, so that it is clear my order has gone through
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am a user, When I complete a checkout form and my payment is processed, Then I can see confirmation of my order details</li>
<li>Given that I am a user, When I complete a checkout form and my payment is processed, Then I receive an email with the confirmation details</li>
<li>Given that I am a user, When I complete a checkout form and my payment is processed, Then an order number is generated with which I can retrieve the order details</li>
<li>Given that I am a registered user, logged in when I placed my order, When I have successfully completed my order, Then the order appears in my orders of my account</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop an order confirmation page that the user redirects to on order completion</li>
<li>Develop automated email confirming order - email to include link to order details page for that order and order number</li>
<li>Develop order finder which can bring up the order details from the order number - possible data restriction here - might not be able to display the customer details</li>
<li>Develop linking new order to user orders so that it is visible within their order history on their account</li>
<li>Develop order number generator so each number has a unique identifier</li>
</ul>
</details>

<br>

<details>
<summary>
US#52 - Check Order Status - As a User, I would like to be able to check on the status of my order, so that I know when it has shipped or when it will be arriving
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am a user, When I want to check on the status of my order, Then there is a location where I can enter my order number to bring up its current status</li>
<li>Given that I am logged in user, When I want to be able to check on a previous order, Then there is a list of all my previous orders that will take me to the order status results</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop an order status system that returns the current status of an order</li>
<li>Develop employee ability to update order status</li>
<li>Develop link on user account to view order status for prior orders</li>
</ul>
</details>

<br>

<details>
<summary>
US#53 - Create Product Review - As a User, I would like to create a review for a product that I have purchased, so that I can share my opinion with other buyers and the company
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am a user, When I have purchased a product, Then I can write a review for that product</li>
<li>Given that I am a logged in user, When I write a review, Then I can choose whether to display my name with the review</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop method for logged in users to add a review of a product they have previously purchased</li>
<li>Develop method for non registered users to add a review of a product they have previously purchased - alternatively - non registered users need to register in order to leave a review.</li>
</ul>
</details>

<br>

<details>
<summary>
US#54 - Edit Product Review - As a User, I would like to be able to edit a review I have written, so that I can correct any mistakes that I may have made
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am a user, who has left a review, When I navigate to the page where my review is located, Then I have the option to edit my review</li>
<li>Given that I am a user, who has left a review, When I navigate to the page where my review is located, Then I am unable to edit the other reviews</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop option for review author to edit the review</li>
<li>Prevent users from editing other user's reviews</li>
</ul>
</details>

<br>

<details>
<summary>
US#55 - Read Reviews - As a User, I would like to be able to read other people’s reviews of a product prior to making a purchase decision, so that I can make an informed decision
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am a user, When I navigate to a product detail page, Then the reviews are available to be read</li>
<li>Given that I am a user, When I navigate to a product detail page, Then the reviews are easily accessible</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop product detail template to include user generated reviews</li>
<li>Develop page layout so that the reviews are easily identified</li>
</ul>
</details>

<br>

<details>
<summary>
US#56 - Delete Review - As a User, I want to be able to delete my review of a product, so that I have the option to remove it should I so choose
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am a user, When I am viewing a review that I have written, Then I have the option to delete the review</li>
<li>Given that I am a user, When I am viewing a review that I have written, And, I select the option to delete that review, Then the review is deleted.</li>
<li>Given that I am an Employee User, When a review that is deemed inappropriate is posted to the site, Then I have the ability to remove it</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop the ability for a review author to delete their review</li>
<li>Develop the ability for an employee to delete a review</li>
</ul>
</details>

<br>

<details>
<summary>
US#57 - Respond to Review - As an Employee, I want to be able to respond to a user’s review, so that where appropriate, concerns or compliments can be responded to.
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that a user posts a review on a product, When an employee views the review, Then they have the option to leave a response</li>
<li>Given that an employee posts a response to a review, When other users view that review, Then they can read the response</li>
<li>Given that an employee posts a response to a review, When that employee, or other employees view the response, Then they have the ability to edit or delete it.</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop a method for employees to respond to a review left on the site</li>
<li>Develop a method for employees to edit or delete responses left on the site</li>
<li>Develop the ability for all users to view the response from the company</li>
</ul>
</details>

<br>

<details>
<summary>
US#58 - Email Capture - As a Site Owner, I would like to capture user emails, so that I can use them for marketing newsletters to promote new products
</summary>
<br>
<h4>Acceptance Criteria</h4>
<br>
<ul>
<li>Given that I am a user who wants to subscribe to a newsletter, When I complete the newsletter sign up form, Then my email address is added to the newsletter distribution list</li>
<li>Given that I am the site owner, When I want to send a newsletter out, then I have a platform from which to do so to the database of emails collected</li>
</ul>
<br>
<h4>Implementation</h4>
<br>
<ul>
<li>Develop email sign up form to subscribe to newsletter</li>
<li>Link email sign up form with mailchimp to collect email addresses</li>
<li>Identify logged in users - replace form with checkbox or alternative solution to subscribe to newsletter</li>
</ul>
</details>
<br>
<br>

## The Skeleton Plane
### Wireframe mock-ups
Wireframes were produced for the majority of pages, with the exception of pages that were likely to only include a form such as the add product page. A pdf document with the full set of wireframes produced is available [here](/static/docs/wireframes.pdf).

Attention was paid to the elements that would be present on each page such as the header and the footer.
The header allows for multiple levels of navigation providing the user with shortcuts to account information, whilst clearly being seperated from the main navigation options. On mobile or tablet devices, the two are seperated by a horizontal bar within the main menu, whilst on the desktop view the secondary account navigation links appear above the main site navigation.
<br>
Desktop Nav Bar Wireframe
<br>
![Nav Bar](/static/docs/img/wireframes/navbar-desktop.png)
<br>
Mobile/Tablet Nav Bar Wireframe
<br>
![Nav Bar Mobile](/static/docs/img/wireframes/navbar-mobile.png)
<br>
Desktop Footer Wireframe
<br>
![Desktop Footer Wireframe](/static/docs/img/wireframes/footer-desktop.png)
<br>
Mobile/Tablet Footer Wireframe
<br>
![Mobile Footer Wireframe](/static/docs/img/wireframes/footer-mobile.png)
<br>
Home page: The home page provides the user with a clear understanding as to the purpose of the site The welcome message is clearly visable to the user when they first arrive at the site regardless of the device they are using. There is a clear navigation area located at the top of the screen, with a search icon clearly visible within the header. There are large call to action buttons linking users to search results for popular categories of products for easy access.
<br>
[Home Page Mobile Wireframe](/static/docs/img/wireframes/homepage-mobile.png)
<br>
[Home Page All Wireframes](/static/docs/img/wireframes/Home%20page.png)
<br>
All Products Page: For a page that shows all the products available it was deemed important to enable users to browse the range easily, therefore presenting the individual products in a summary fashion which enables the user to navigate to access more information if required or just add the products that they want to their cart
<br>
[All Products Page](/static/docs/img/wireframes/All%20Products.png)
<br>
Individual Product Page: For each individual product three distinct sections were planned to enable product information to be presented clearly to users. An image carousel to allow multiple images to be displayed allows users to see the product from multiple angles. Whilst users can access the overall description and add to cart functionality quickly and easily at the top of the page.
<br>
[Individual Product Page Wireframe](/static/docs/img/wireframes/Individual%20Product.png)
<br>
Shopping Cart: For the shopping cart functionality wireframes were produced for both the page and the preview/confirmation message when a user adds a product to the shopping cart. For the shopping cart it is important to allow users to adjust the items in the cart, increase or decrease individual items quantity or remove items completely.
<br>
[Shopping Cart Wireframe](/static/docs/img/wireframes/Shopping%20Cart.png)
<br>
Checkout: For the checkout page the user will be required to enter, or confirm their billing/delivery address. The intention from the wireframe design is to include a summary of the users shopping cart along with the form for them to confirm their details. In the lower portion of the page users will be able to enter their payment information which will be based on a payment form provided by Stripe. As it is a page where the user can be charged for the goods, it is important for a good user experience that the total cost is clear to the user.
<br>
[Checkout Page](/static/docs/img/wireframes/Checkout.png)
<br>
Order Confirmation: Provided the users payment is processed successfully, they will be taken to the order confirmation screen which will provide the user with a summary of the entire order as it has been recorded along with their order number. The order number will need to be unique for each order. If the user is a registered user and logged in at the time of order, they should be able to access the order details again at a later date. Non registered users should be able to access their orders status by entering the order number somewhere else on the site.
<br>
[Order Confirmation page](/static/docs/img/wireframes/Order%20Confirm.png)
<br>
All Blog Posts Page: The blog posts page is a key page within the site. From a user experience persepective, the blog provides an opportunity for the company to directly communicate with its customers, or prospective customers. This communication can be in the form of guides, product reviews, or any other type of communication that they believe their customers might find useful. The content the company can produce for this section of the site is important for SEO purposes also and can assist in their overall marketing efforts. Ideally therefore, users should be able to access the blog section of the site easily, and also be able to quickly assess which blog posts they are interested in.
<br>
[All Blog Posts Page](/static/docs/img/wireframes/All%20Blog%20Posts.png)
<br>
Individual Blog Post: For the individual blog post page the full details of the post are available. The layout is a clean simple design with an image at the top followed by the main content of the post.
<br>
[Individual Blog Post Page](/static/docs/img/wireframes/Individual%20Blog%20Post.png)
<br>
User Account Page: The user account page is a central location from which users can manage their entire account. All potential options need to be easily accessible from this one page. A short menu of available options is located at the top of the page followed by the ability for users to add addresses, or change their default address to another saved address. Finally the option to delete their account is clearly available. By providing the option clearly and not hidden away it promotes trust with the user that they are in full control of their account.
<br>
[User Account Page](/static/docs/img/wireframes/My%20account.png)
<br>
<br>

### Database Schema

<br>

![Database Schema Diagram](/static/docs/img/database/database-schema.png)

<br>
Several custom models were predicted to be required when building the site. To plan out the models they were sketched out in Figma. Figma was chosen due to the limitations of the free tiers for the online apps available which restrict the field choices available, therefore allowing the fields to be defined correctly whilst planning. The intention to utilise AllAuth for the user authentication system, which utilises the built in Django User Model removed the need to build a custom User model for user authentication, however some custom information is required, therefore a custom user model to override the allauth model is required. In order for users to be able to save multiple addresses to their account, an address model was created with the required fields. A boolean field that records whether it is the default address for the user was also added to aid the checkout process. 
<br>

![User and Address Models](/static/docs/img/database/user-schema.png)

<br>
For the products a custom model based on the boutique ado walkthrough project was created. This model was adapted by adding the additional fields required for the additional product information expected for this site, whilst several fields were removed as unnecessary given the type of products offered. A seperate image model was created so that additional images for each product could be stored. This allows in theory an unlimited number of images to be stored for each product. Whilst the intention is that each product will have three images in total, one main image associated with the product itself, and two additional images stored in the image model, it would be possible to adjust the site to accomodate many more images per product. By seperating the additional images from the main product model it enables products to be added to the site with only one image. A third product related model to define the product category was created. Based on the model from boutique ado also, the category model contains two fields a name and a friendly name field. No other fields were deemed necessary for the model to customise it further.
<br>

![Product, image and category models](/static/docs/img/database/product-schema.png)

<br>
The order process is controlled with the use of two models, an Order model and a OrderLineItem model. Both models were based on the models from boutique ado with the changes required for the purposes of this site. Given the information that is required to be sent to Stripe for processing the payments and would be required for business purposes the structure of the models makes sense to be utilised. The changes made include the addition of a status field to enable the recording of the order status and future updates to provide users with additional information.
<br>

![Order process models](/static/docs/img/database/order-schema.png)

<br>
Two models relating to users creating reviews of products were created, one to record the users review and another to record an employees response to that review.
<br>

![Review and Response Models](/static/docs/img/database/review-schema.png)

<br>
The final model created records user messages to the company through the contact us page.
<br>

![Contact Message Model](/static/docs/img/database/contact-schema.png)

<br>

### SEO Considerations

<br>

#### Keyword Research
Research was conducted to discover the appropriate keywords to utilise given the target customer markets and product range to be carried. This research was based on Google's SEO tools which provides details of common search terms users are search for and allows you to search these terms by target market. The UK, Ireland and the USA markets were used for example purposes.

<br>

[PC Case Keyword Research - Ireland](/static/docs/img/seo/custom-pc-case-ireland.png)

<br>

[PC Case Keyword Research - UK](/static/docs/img/seo/custom-pc-case-uk.png)

<br>

[PC Case Keyword Research - USA](/static/docs/img/seo/custom-pc-case-usa.png)

<br>

[Watercooling Keyword Research - Ireland](/static/docs/img/seo/watercooling-ireland.png)

<br>

[Watercooling Keyword Research - UK](/static/docs/img/seo/watercooling-uk.png)

<br>

[Watercooling Keyword Research - USA](/static/docs/img/seo/watercooling-usa.png)

<br>

From this research a refined keyword list was cultivated for use with the short-tail keywords within the head meta tags and for content through out the site. However this only formed a small part of the overall strategy for the sites SEO strategy.

#### Content Strategy
The main foundation for the sites SEO strategy was to provide a platform for the company from which they can provide users with informative and relevant information. Product pages were designed to include more details that the average product page - which enables the company to configure the descriptions in a manner that maximises the SEO value. The blog section of the site enables the company to write informative articles that can answer commonly searched for questions. This will enable the company to increase their authoritativeness on relevant topics that their users are searching for. Three articles were provided with content acquired from other relevant websites. There articles were edited to incorporate the keywords discovered from the earlier research.


## The Surface Plane

### Design

Once I was happy with the overall structure of the site, and the layout of the wireframes, I selected a colour scheme based on a desire for a simple and clean aesthetic. The site incorporates two main colours, blue and white, although specific shades were selected for various different areas, they all remained within the blue family. Blue was chosen due to the fictional business base location and the county colours are blue and white. The white or off white shades are tinted with a little blue to maintain consistency. The colour scheme was referenced using the [contrast grid](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23FFFFFF%2C%20White%0D%0A%23000000%2C%20Black%0D%0A%2303045E%2C%20Primary%0D%0A%23f2f4f8%2C%20Primary-text%0D%0A%23c7ccdb%2C%20Secondary%0D%0A%23f7c59f%2C%20Accent%0D%0A%2370ae6e%2C%20Success%0D%0A%23ef626c%2C%20Error%0D%0A%231188a0%2C%20Info%0D%0A%23f3c178%2C%20Warning&es-color-form__tile-size=compact&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18) which provides a grid of colour contrasts to ensure only those which would easily pass the AAA standard were selected to maximise accessibility for users.
<br>

![Colour Contrast Grid](/static/docs/img/contrast-grid.png)

<br>

### Typography 
Three different fonts were utilised for the site. The main heading font of Orbitron and the smaller subheading font of Economica were selected for their futuristic almost technical feeling whilst Montserrat was chosen as a complimentary font which allowed users the ability to read the text easily and clearly.

##### Images
Background images were acquired from free image sites [Pexels](https://www.pexels.com/) and [Unsplash](https://unsplash.com/), product photos were found on manufacturer media pages.


## Features

### Navigation
The main navigation is split into two sections. The first section contains the main navigation for the sites main sections of interest. The second section contains the links for user account management or employee site management. JavaScript was utilised to move the second navigation section into place depending on the size of the screen. On the desktop view the secondary navigation bar appears on the top right of the screen, whilst in the mobile/tablet menu it appears below the main navigation options.
<br>

![Navigation desktop view](/static/docs/img/features/nav-desktop.png)

<br>

![Navigation mobile menu](/static/docs/img/features/mobile-menu.png)

<br>

### Footer
There are also navigation links within the footer from which users can access areas of the site, this includes areas that are not listed in the main navigation such as the privacy policy or social media links. Also included in the footer is a newsletter sign up to a mailchimp controlled email database. The mailchimp supplied sign up form was styled to match the remainder of the site.

<br>

![Footer Desktop View](/static/docs/img/features/footer-desktop.png)

<br>

### Homepage
The home page greets users with a welcome message overlaid on a close up image of cooling pipes inside a computer system. This provides a welcome to all users whilst indiciating the sites purpose. The clear links within the navigation bar indicate that the site is a shop whilst the call to action cards below the welcome/hero section direct users to specific product categories quickly and easily.

<br>

![Homepage View](/static/docs/img/features/home-desktop.png)

<br>

![Home page mobile view](/static/docs/img/features/home-mobile.png)

<br>

### All Products
The all products page displays summary cards for each product, with a maximum of five products per page pagination was utilised to create multiple pages making up the full list of products.

<br>

![All Products Page](/static/docs/img/features/all-products-desktop.png)

<br>

### Product Search
Users can search the site for different products through the search bar which is activated by clicking on the search icon located within the main header.

<br>

![Search Bar Activated](/static/docs/img/features/search-bar-desktop.png)

<br>

When a search is completed by the user, the results will display in summary card format. Pagination is utilised for scenarios where the search results are too large for display on one page. The search criteria is displayed at the top left of the screen for users as a indication that they have filtered the results.

<br>

![Search Results](/static/docs/img/features/search-results-desktop.png)

<br>

The individual summary card for each product links the user to the full product details. For ease of use, users have the ability to add the product to their shopping cart without accessing the full product details. A quantity selector is also included for those users who wish to purchase in multiples. The summary cards contain the basic information users may require for each product, the product name, the sale price, if it is available, a category indicator and the shopping controls.

<br>

![Product Card](/static/docs/img/features/product-card.png)

<br>

### Add to Bag
When a user adds a product to their shopping cart they receive a confirmation message that it has successfully been added. The icon for the shopping cart, also gains an indicator that shows the quantity of products they have within the cart as an additional level of confirmation.

<br>

![Add to cart confirmation](/static/docs/img/features/add-product-message-desktop.png)

<br>

### Shopping Cart
When the user is happy with their selections they can proceed to the shopping cart to confirm the quantity and selections. The user has the ability within this page to adjust the quantity of the products selected, or to remove products entirely before proceeding to the checkout process.

<br>

![Shopping Cart Page](/static/docs/img/features/shopping-bag-desktop.png)

<br>

### Checkout
When the user is ready to purchase the products that they have selected, they proceed to the checkout page, here they can enter their billing and delivery information. Registered users can save the information they have entered and create a new address record. If they already have address records saved, they have the option to select one of them to use for this purchase. If they have a default address set the form will be prefilled with the default address information. The final part of the form is the payment details, this is taken directly from Stripe - or inserted by Stripe for the purposes of capturing the payment card information. As the Stripe payment system is not fully activated only the test card information can currently be utilised.

The page also includes summary information about the items being purchased so that it is clear to users what they are purchasing. A message also appears next to the complete order button informing the user of the total amount they are agreeing to be charged.

<br>

![Checkout page Desktop](/static/docs/img/features/checkout-desktop.png)

<br>

### Order Confirmation
When users have successfully processed their payment, they are taken to the order confirmation page which provides the user with a summary of the information their order contains. This page also provides the user with their order number.

<br>

![Order Confirmation](/static/docs/img/features/order-confirmation-desktop.png)

<br>

At the same time as the user is redirected to the order confirmation page, an email is sent to the email address they provided during the checkout process. This email provides the user with the same details as the order confirmation page, with the full address details summarised as the town and country only.

<br>

![Order Confirmation Email](/static/docs/img/features/order-confirmation-email.png)

<br>

### Order Status
Registered users can access the status of all previous orders through the order status page. Here they are able to filter and search through their prior orders. Results are presented in the form of summary cards showing the order number, the items ordered, total order value, date of order and its current status.

<br>

![My Order History](/static/docs/img/features/order-history.png)

<br>

Employees are able to access an update order status page which allows them to update the status of an order. Several predefined options are available covering all common order status stages. When an employee updates an orders status it is then reflected back on the users record with the new status. To access the update order status screen employees have an order management option within their employee actions navigation menu. This page is similar to the My Order History page above, and provides the employee the ability to filter and search through the current orders on the system to find the correct order to update.

<br>

![Update Order Status](/static/docs/img/features/update-order-status.png)

<br>

### User Account Management
Registered users can access controls for their account through the My profile option in the account menu. In the profile page they have access to options to change their email address, name, password or delete their account entirely. They can also make adjustments to the addresses that are stored with their account, accessing add, edit, delete and make default functionality.

<br>

![User Profile Page](/static/docs/img/features/profile.png)

<br>

### User Wishlist
Registered users can also save products to their wishlist by clicking on the heart icon within the product details. Once they have added a product to their wishlist they are informed by the heart icon becoming filled in colour. They will also see the product listed on the My Wishlist page. Here users can add the products to their cart without having to search for them, select the quantity to be added. Remove the product from their wishlist, or follow the link to the full product details.

<br>

![My Wishlist Page](/static/docs/img/features/wishlist.png)

<br>

### Blog
Users have access to view blog post articles written by the company. These articles will form part of the company SEO and web marketing strategies and allows them to include information on topics that will be interesting to their users. Clever use of the blog post section of the site will allow the company to incorporate both short tail keywords and long tail keywords, providing answers to target users questions. This will improve their overall search engine ranking performance whilst providing users with beneficial information and improving their overall experience and trust within the company.
Users are able to select which blog post to read through the summary list provided on the main blog page.

<br>

![Blog Post Page](/static/docs/img/features/blog-posts-desktop.png)

<br>

The blog detail page provides the user with the full blog post content

<br>

![Blog post detail page](/static/docs/img/features/blog-detail-desktop.png)

<br>

Whilst employees will have access to additional options in order to access areas of the site that allow them to add, edit, delete blog posts. They also have access to blog post category management options that allow them to add, edit and delete categories for blog posts.

<br>

![Employee view of blog posts](/static/docs/img/features/blog-category-management.png)

<br>

### Product Reviews
Users who have purchased a product from the site are provided access to add a review for that product and a rating. The option exists on the main product detail page for each product. Users are only able to add one review per product, and the employees have the ability to respond to the review directly.
Other users will be able to read other users reviews of a product to aid in their purchase decision making.

<br>

![Add a product review](/static/docs/img/features/add-review.png)

<br>

Once a user has added a review to a product, they will have the option to edit or delete their review. Employee's get the option to respond to the post or to delete the review. The screenshot below shows all options as the review was added by the logged in employee.

<br>

![View a product review](/static/docs/img/features/product-review.png)

<br>

### Contact Us
Users have the ability to send a message to the company directly through a contact form provided on the site. When a user sends a message through the website they will also receive a copy of the message to the email address that they provided. The message that the user sends is also delivered via email to the company designated account so that it can be followed up on and answered.

<br>

![Contact Page](/static/docs/img/features/contact-page-desktop.png)

<br>

## Future Enhancements
There are several items of functionality that I would like to add in the future. I have left the original user stories that were developed in the project kanban board as future enhancement opportunities.
The key areas I would like to add to the site in the future are:
* A stock management system to enable the product sales to record and update stock level information
* A wider product range - the world of PC parts is varied even without looking at the hardware. This would require more advanced product filters being added which allows the user to refine their selection in more detail. PC components are varied, one case to the next can be vastly different in size and users should have the ability to filter by exact requirements to ensure they are looking at products that are suitable for their intended use case.
* The ability for users to login via social networks such as google or facebook
* Product ratings - users are able to leave a review of a product along with a rating. Currently, the rating is only recorded, it does not update an average statistic, however this can easily be incorporated in the future.

Some of the functionality above is provided by allauth which is already installed into the site, and therefore only has to be setup in order for it to function. Others would need to be developed completely. The stock system was an nice to have option in the development, there are references to its potential inclusion within the code however they do not currently update for example each product shows an instock pill on the product details.

## Social Media Marketing
For the purposes of the assessment a Facebook page was created for the company. As a key foundation for any ecommerce website's marketing strategy social media would form a key part of the businesses marketing strategy. The page included links to the main website to drive traffic from the social network to the site. Content for the page was based on the blog posts created for the site, whilst at the same time incorporating information that might be useful for users in smaller formats such as a back in stock notice.

<br>

![Druid Facebook Page](/static/docs/img/seo/facebook-page-2.png)

<br>

## Testing

### Testing Strategy
I utilised an automated and manual testing strategy for the development of the site. A full detailed breakdown of the testing procedures and methodology can be found in the testing.md file [here](TESTING.md).
Seperate to the functionality testing of the site, and the testing of the code, User Story tests were implemented to ensure that the acceptance criteria of the user stories listed above were met. The commit at which the functionality requirements for each user story were met is listed in the issues section of the repo. It was applied to each issue before it was closed and marked as completed.

#### Testing Overview

Testing was divided into different sections to ensure everything was tested individually with test cases developed for each area.

[Testing Schedule Overview](/static/docs/testing-schedule.pdf)

A full detailed breakdown of the testing procedures and methodology can be found in the testing.md file [here](TESTING.md)

#### Validator Testing
All code files were validated using suitable validators for the specific language. The full details can be found in the testing.md file.
All code passed the validation, with only code generated by other parties producing errors or warnings.
* Django built in code within the settings file produced five line length errors. 
* Bootstrap code produced 260 warnings in the CSS validation. 
* Fontawesome cdn produced 6 HTML validation errors relating to css variables within the cdn css code. 
* The HTMX library that is inserted into the HTML template by django produces a warning stating that the link does not need to have the javascript file type declared.

#### Automated Testing
Automated tests were written for the blog and profile apps, along with the product forms. A total of 45 different tests were written to test the urls, views and forms and demonstrate my understanding of the testing procedures. In order to run the tests, you will need to clone the repo. In the settings for the project the database is set to point at the specified database when a database url is present within the config variables. Provided that you do not include a database url in the config variables django will run the tests on a test database utilising sqlite3. Django will not run the tests on the postgresql database from a heroku application, therefore you will need to ensure not to include the database url in the config variables.

<br>

![Automated testing results](/static/docs/img/features/tests.png)

<br>

#### Lighthouse Testing
Google's lighthouse testing was utilised to gain an overall assessment of the performance of the site. Whilst all the areas of the test return a green score above 90, the overall performance figure fluctuates depending on the speed of the internet connection when the test is performed, having returned scores as low as 92 and as high as 100 whilst running the test multiple times. The accessibility score suffered a couple of points due to utilising headings in a non sequential order through out the site. The best practice score is impacted by the mailchimp and stripe included javascript files along with the use of the bootstrap and jquery libraries. The SEO score returned a perfect 100.

<br>

![Google Lighthouse Results](/static/docs/img/features/lighthouse.png)

<br>

#### Notable Bugs

* Whilst validating the HTML it reported an error that I had included a placeholder for a checkbox field which is not allowed. To fix this error I removed the placeholder from the list within the forms.py file for the relevant address form. Thinking that will sort the error out and its only a placeholder so doesn't affect anything else. It did fix the HTML validation error straight away, however, it created a bug within another part of the code where the fields were checked whether they were required or not. If a field was required it adds '*' to signify it to users, if it is not, it inserts the placeholder. However, now I had removed the placeholder, anytime the form was requested it would return a 500 error. Whilst I appreciated the ability to test the custom 500 error page worked correctly on the production site it was a bug that took me a little while to track down the route cause and fix. The fix was simple enough and achieved by including the default field of the model within the if statement and excluding it from the placeholder assignment.

* Within the blog post page employee view, there is a category management section that can be activated. This section allows an employee to edit, delete and create categories for blog posts. Forms are inserted via htmx into the html on demand to allow the employee to carry out the task required. As the forms are inserted via htmx, it was possible to insert multiple forms at the same time into the page and edit multiple categories at once, and have the add category form open as well. If the user did this, a HTML validation error would occur as the form is duplicated it contains duplicate ID's. To overcome the HTML validation error possibility, JavaScript was utilised to prevent the user from opening multiple forms at the same time, this was achieved by disabling the other buttons when a user clicks on one of the edit buttons or add buttons, until either the user cancels their action or has completed their task.

* Order Status updates. Within the order management section of the site, employees have the ability to update the status of an order. To help with finding the correct order, multiple filters are available for them to search the orders within the database. One of these filters allows for searching the previous days orders. This works as designed during normal working hours, however when testing the functionality it was discovered that during the first hour of the day, so the time period between midnight and 1am the filter would bring back the previous day plus one's orders, not the previous days. This resolves itself as soon as the time clicks past 1am. As the only time that this will be triggered is in the middle of the night, it was deemed acceptable to leave as it currently is and not attempt to edit the library utilised to include the filters. Should the business operate 24 hours a day and require the functionality to pull the previous days orders during that one hour window it would obviously need to be resolved.

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
* The Code Institute reference material was used as a general reference for things that I had previously done during the course.
* All other resources used are referenced where appropriate.


## Deployment

The site was deployed via Heroku, and the live link can be found here - [Druid](https://druid-computers.herokuapp.com/)

### Project Deployment - needs adapting for AWS and Stripe

To deploy the project through Heroku I followed these steps:
* Sign up / Log in to [Heroku](https://www.heroku.com/)
* From the main Heroku Dashboard page select 'New' and then 'Create New App'
* Give the project a name - I entered Druid-Computers and select a suitable region, then select create app. The name for the app must be unique.
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
* Navigate in a browser to Amazon AWS, log in, or create an account and log in. 
* Create a new S3 bucket for the site and create a static directory and media directory within the bucket.
* From the dashboard - copy the bucket details into the settings file.
    * you will require the following:
        - Storage Bucket Name
        - Storage Bucket Region Name
        - Access Key ID
        - Secret Access Key
    * configure these settings in the settings file
* in the env.py file created earlier 
    - add os.environ["AWS_ACCESS_KEY_ID"] = "paste in your access key"
    - add os.environ["AWS_SECRET_ACCESS_KEY"] = "paste in your secret access key"
* In Heroku, add the keys and values copied to the clipboard to the config vars
* Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars
* this key value pair must be removed prior to final deployment
* Using the requirements.txt file install all of the required packages
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
* This project utilises Stripe as a payment platform provider - You can create a stripe account at www.stripe.com you will need a developer account to gain access to the api keys required to run the payment processes.
* Once you have successfully created your stripe account, insert the stripe public key, stripe secret key and stripe webhook key into the env.py file and the heroku config vars. Configure the settings file to point at the variables required. Stripe provide documentation on how to setup stripe within django which is easy to follow. It is available within the stripe developer site.

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

### Credits
* Product images, descriptions and technical data was acquired from the corresponding manufacturers website where available or from [Watercooling UK](https://www.watercoolinguk.co.uk/)
* Other images were acquired under license from [Pexels](https://www.pexels.com/) or from [Unsplash](https://unsplash.com/)
* Blog articles based on blog posts on [EKWB](https://www.ekwb.com/)


### Acknowledgements

I'd like to thank the following:
* Daisy McGirr for all her help during this project.
* Sean, Ed and Alex at CI Tutor support for their patience and pointing me in the right direction when I went off course.