![BF logo](https://bee-fitness.s3.eu-west-2.amazonaws.com/media/bf-logo.png)

# Bee Fitness

## Milestone Project 4

The project can be found here: [Bee Fitness](https://bee-fitness.herokuapp.com/)

As part of the Code Institute Full Stack Development Diploma I have created this website using the technologies learnt throughout the course.

This website shows off Python Django knowledge recently learnt along with Javascript, HTML, Bootstrap and CSS previously learnt. These skills are used to make a fitness center website that allows users to sign up, pay for a subscription and then get access to the gym using the online membership card and get access to staff written personal training programs

## UX

The UX process was vital in creating an appealing site to entice members to join the fitness center. With a consistent yellow colour scheme throughout, and easy to use features, this website allows users easy access to join the fitness center, get their membership card for access to the center and keep up with their personal training plan.

I used trello to create user stories that are relevant to what each type of user expects and wants from this site.

### User stories

Writing user stories was an important step in understanding how my website should look and work. Thinking about it from the user's perspective gave me the opportunity to create something that everyone will enjoy using and gives the user what they expect.

* As a user, I want to be able to register for an account
* As a user and potential member, I want to find information about the gym
* As a user, I want to be able to get a subscription to the gym
* As a user and regular gym goer, I want to have a membership card to enter the gym
* As a user, I want to be able to update my personal details
* As a user, I want the pricing to be displayed
* As a user, I want to be able to pay using my debit or credit card
* As a user, I want to easily navigate the website
* As an admin and staff member at the gym, I want to be able to delete users whose subscriptions have expired with the click of a button
* As a gym user, I want to be able to get access to my personal training plan on the site

### Mockups

Mockups, created on Balsamiq, were the first stage of planning the website can be found [here](/mockups/bee-fitness-mockups.pdf)

I created a copy of the database structure that can be viewed [here](/mockups/database.png)

The styling has changed slightly from the mockups, some small changes, with buttons, images and text in different positions. There have been bigger changes too, with the implementation of the Exercise/Personal Training Plan in the members area. This is a change based on the user stories and more understanding of what the user wants from the site.

## Features

### Current Features

* The Bee Fitness header shown on navbar throughout site
* Navbar for mobile and larger screens, automatically adjusting dependant on device size. Listed view for larger screens and sidebar/dropdown for smaller screens
* Consistent colour scheme throughout
* Header image at the top of most pages with a clear title so the user knows where they are on the site at all times
* Home page allowing unsubscribed members to join and welcoming already signed up members back to the site depending on users status.
* Sign up and login using django allauth
* Further sign up screen to gather users information
* Stripe payment accepting credit/debit cards and google pay and apple pay
* About pages to learn about what Bee Fitness has to offer before subscribing
* Members page visible after subscribing
* Membership card on the members page with unique QR code for access to the gym
* Exercise plan on the members page that admin/gym staff can update with exercise plans for users to complete
* Profile page to update member information
* Button for staff/admin to delete expired members at the start of each day



### Future Features - to implement

* Automatic deletion of expired memberships

## Technologies Used

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Using Django, the python language was used for backend production of the website and allowed many frontend functions to be displayed.
* [Django](https://www.djangoproject.com/) - The back end to the project, including all models, urls and views were written with with Django
* [Bootstrap](https://getbootstrap.com/) - The framework that provides basic styling, and interactive items such as the mobile navbar. I built upon the basic styling to create a more unique site. Useful for creating a dynamic site that works on all screen sizes.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - Used to initialise and allow the stripe payments
* [JQuery](https://jquery.com/) - JQuery library was used to initialise all of the interactive bootstrap functions.
* [HTML](https://en.wikipedia.org/wiki/HTML) - HTML is used to make up the base of each web page. I created elements that used templating inside to create a more dynamic site
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - Styling for the whole site, from backgrounds to text fonts, sizes and colors.
* [Font Awesome](https://fontawesome.com/icons?d=gallery) - Used to display icons.
* [Google Fonts](https://fonts.google.com/) - Chose the fonts carefully from Google Fonts and embedded them to the CSS page and used them throughout the site.

## Testing

Testing was carried out on desktop and mobile during the building of each function for the site, making use of the debugger to find any faults in the code quickly.
I work on a mac using OS X and built the site on gitpod using Chrome. When I deployed the final version of the website it worked exactly as expected.
I tested throughout using iPhone X, Samsung Galaxy A40 and MacBook Pro. 

One issue I dealt with and was vital for correct functionality of the website was with the user info form not submitting to the database. This was remidied by adding a signals.py file to save the information and defining each user properly. This issue required thorough testing to ensure it was working as desired.
Tested the HTML pages, CSS, Python & Javascript on the [HTML validator website](https://validator.w3.org/), [CSS validator website](http://www.css-validator.org/), [Python validator website](http://pep8online.com) & [a Javascript validator website](https://jshint.com/).

#### HTML errors:

* Warnings and errors are all centered around the lack of "doctype" and the use of the templating throughout. The html files inherit the DOCTYPE and head tags including links to required sources (JS, CSS and CDNs) from the base.html page. These errors are acceptable as the validator does not recognise templating.

#### CSS errors:

* No errors found

#### Python errors:

* No errors found

#### JS errors:

* No errors found

### Testing across multiple devices and browsers on completion

Developed on a MacBook Pro using GitPod and checked throughout development on Chrome
Tested on the following devices:

* MacBook Pro 13" - Internet Explorer (using Safari developer tools), Safari, Chrome, Edge, Firefox, Opera
* iPhone X - Safari, Chrome, Edge, Firefox, Opera
* Samsung Galaxy A40 - Samsung Browser, Safari, Chrome, Edge, Firefox, Opera

Multiple screen sizes were tested using Chrome developer tools on the MacBook, including Moto G4, Galaxy S5, Pixel 2, iPhone 5/SE, iPhone 6/7/8, iPhone 6/7/8 Plus, iPhone X, iPad, iPad Pro, Desktop and 4K TV screens.

The site appeared and behaved as expected when testing on all different browser sizes

### Testing Process

Testing involved checking each function on the website across all devices and browsers.

* Navbar
    * The hamburger icon shows on a smaller screen and the links in the navbar show on larger screens

* Site wide
    * All buttons and links work as desired pointing to the correct urls

* Sign Up
    * Worked as expected

* Log in
    * The link to the sign up page works correctly
    * Log in works correctly and takes me to the members page

* Logout
    * Logout works correctly from each page

* Members
    * Membership card displays as expected on all screen sizes, requiring users on mobile to use landscape view
    * Exercise plan displays plans well, and if there are none to view it is clear

* Profile
    * Edit information form works as expected

* Stripe
    * Stripe payments work well and as expected using debit/credit card, apple pay and google pay

* Admin delete expired users
    * Only displays for admin and works as expected


### Testing User Stories

* As a user, I want to be able to register for an account
    * Registration is easy to reach from the main page and the my account nav dropdown. Email verification was tested when set up and works well.

* As a user and potential member, I want to find information about the gym
    * About pages are available for everyone to view, to learn about the gym before subscribing. Tested that that always appear no matter the login status of the user.

* As a user, I want to be able to get a subscription to the gym
    * Subscriptions are available to be bought from the payment page, only accessible for members when they have no subscription, which was tested thoroughly. Stripe payments work well and create a year long subscription.

* As a user and regular gym goer, I want to have a membership card to enter the gym
    * Once subscribed the members area unlocks and allows members to view their membership card with a unique qr code, which has been tested on all screen sizes and for multiple users.

* As a user, I want to be able to update my personal details
    * The profiles page allows users to update the information that they first submitted when signing up and paying.

* As a user, I want the pricing to be displayed
    * Pricing is displayed on the payment page, the stripe payment page and the about page for potential members to decide if they want to pay that amount.

* As a user, I want to be able to pay using my debit or credit card
    * Stripe payment function has been set up to accept credit/debit card payment and google and apple pay and has been tested multiple times using the stripe testing solution.

* As a user, I want to easily navigate the website
    * The navbar contains all links any user could need to access all parts of the site

* As an admin and staff member at the gym, I want to be able to delete users whose subscriptions have expired with the click of a button
    * This button is available on the my account section and payment page. Staff will be instructed to complete this action at the start of each day.

* As a gym user, I want to be able to get access to my personal training plan on the site
    * When signed up and subscription paid the user will have access to a personal training plan on the members page. The gym staff have to provide the notes for that. It has been tested well and displays well, and is easy to follow for the user to read during a workout.

### Bugs
#### Issues found on devices and browsers

Very few issues found across all devices, browsers and screen sizes. Images displayed as fixed dont show in that way on iPhone, but still display well so its not an issue. Apart from that minor issue it all looked as expected and intended.

## Deployment

I used GitPod to develop the site and Heroku linked to a GitHub repo to host the main structure of the website (HTML & Python files). AWS was used to host the static files (CSS & JS) and the images in the media file.

The website can be found on the link at the top of the page and here - [Bee Fitness](http://bee-fitness.herokuapp.com/). I deployed the project using Heroku. At the moment the deployed version uses the master branch, but if future updates are needed these can be done using a separate branch until all updates are tested thoroughly and can be deployed.

### Deployment using Heroku

1. Create a Github repository and open this in Gitpod or your choice of IDE
1. Go to the Heroku Dashboard and create a new app
2. Add PostgreSQL Database:
    * Click the resources tab.
    * Under Add-ons seach for Heroku Postgres and then click on it when it appears.
    * Select Plan name Hobby Dev - Free and then click Submit Order Form.
2. In the settings tab of the app click Reveal Config Vars and enter the values for these keys: 
    * AWS_ACCESS_KEY_ID
    * AWS_SECRET_ACCESS_KEY
    * DATABASE_URL
    * EMAIL_HOST_PASS
    * EMAIL_HOST_USER
    * SECRET_KEY
    * STRIPE_PRICE_ID
    * STRIPE_PUBLIC_KEY
    * STRIPE_SECRET_KEY
    * STRIPE_ENDPOINT_SECRET
    * USE_AWS
3. In Gitpod create a .gitignore file
4. Create a requirements.txt by using the command "pip freeze --local > requirements.txt", in order for Heroku to know which dependancies are required to run the app
5. Create a Procfile containing "web: gunicorn bee_fitness.wsgi:application"
6. Go to the Deploy tab on Heroku and navigate to the 'Deployment method' section
7. Select 'Connect to GitHub'
8. Make sure your GitHub profile is displayed and enter the repo name from step 1
9. Select search and once it loads click connect to connect to the app
10. Enable automatic deployment clicking the button below
11. Select the branch you want to deploy from in the 'Manual Deploy' section, mine is just the master branch, and select 'Deploy Branch'
12. Wait for a message saying 'Your app was successfully deployed". You can now select the 'View' button to see your deployed site
13. Once the steps above are completed whenever you push to GitHub, Heroku will automatically update

### Clone Bee Fitness

1. Go to the [repository](https://github.com/stefbez/bee-fitness)
2. Click on the green `Code` button that features a download icon
3. Copy the URL - (https://github.com/stefbez/bee-fitness.git)
4. Using the terminal in GitPod paste the code `git clone https://github.com/stefbez/bee-fitness.git`
5. The whole repository folder, including all files are now available for use
6. The user will be expected to create their own env.py file

## Credits

### Content

* [Stripe subscription tutorial](https://testdriven.io/blog/django-stripe-subscriptions/) was a big help with getting my subscription working

* [This project](https://github.com/Daisy-McG/ChatToTheMat/tree/main/checkout), particularly the checkout view helped with the set up of the stripe subscription and I believe the creator also used the above tutorial.

* The Code Institute [Boutique Ado Project](https://github.com/ckz8780/boutique_ado_v1) was used multiple times throughout this projects, including the styling for the crispy forms and understanding of how to set up the settings.py file correctly

* I used a [Django secret key generator](https://miniwebtool.com/django-secret-key-generator/) for a randomly generated secret key

* JQuery CDN was used directly from [JQuery](https://code.jquery.com/)

* [Font Awesome](https://fontawesome.com/icons?d=gallery) for icons

* Fonts were found and embedded from [Google Fonts](https://fonts.google.com/)

* When stuck, I turned to the Code Institute Slack channels for advice and ideas for how to solve issues, Tutor support from Code Institute and [Stack Overflow](https://stackoverflow.com/)

### Media

* Bee Fitness Logo was made on [Canva](https://www.canva.com/)

* All header images and home page image were sourced using [Pexels](https://www.pexels.com/search/gym/)
* [Treadmill](https://www.pexels.com/photo/an-on-treadmill-1954524/)
* [Stretch](https://www.pexels.com/photo/selective-focus-photography-of-woman-in-white-sports-brassiere-standing-near-woman-sitting-on-pink-yoga-mat-864939/)
* [cross-trainer](https://www.pexels.com/photo/young-female-athlete-training-alone-on-treadmill-in-modern-gym-3768916/)
* [Gym](https://www.pexels.com/collections/healthy-living-sport-food-u880qh7/)
* [Tennis](https://www.pexels.com/photo/selective-focus-close-up-photo-of-empty-red-and-green-tennis-court-with-view-of-tennis-net-2627310/)
* [Swimming](https://www.pexels.com/photo/person-swimming-on-body-of-water-863988/)
* [Tennis-2](https://www.pexels.com/photo/people-woman-ball-tennis-5069199/)
* [Arm press](https://www.pexels.com/photo/serious-sportsman-training-on-exercise-machine-in-modern-gym-3838937/)

### Acknowledgements

* I took inspiration for this from the Code Institute [Boutique Ado Project](https://github.com/ckz8780/boutique_ado_v1). Using ideas from that project and implementing my own ideas and code and learning a lot in the process

* I received support from the tutors at Code Institute with issues and bugs that were occurring

* I also received help with testing across numerous devices and different browsers from friends and family