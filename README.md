# Krisztian's Online Cookbook
Milestone project #3: Data Centric Development - Code Institute

This project is an online cookbook. No authentication needed to read, search, create recipes. 

Link to the live site on Heroku: [here](https://ci-ms3-krisztians-cook-book.herokuapp.com/)

<img src="https://raw.githubusercontent.com/milka77/ms3_cookbook/master/static/images/responsive.png"/>
---

## User Experience (UX)

- ### User Stories
    - #### First Time Visitors Goals
        1. As a First Time Visitor, I want to easily understand the main purpose of the site.
        2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.
        3. As a First Time Visitor, I want to easily find social media links, so I can gather more information about the site and site owner. 

    - #### Returning Visitor Goals
        1. As a Returning Visitor, I want to find recipes with a specified ingredient or name.
        2. As a Returning Visitor, I want to edit, delete recipes.
        3. As a Returning Visitor, I want to find the best way to get in contact with the site owner with my questions, ideas. 
        4. As a Returning Visitor, I want to find community links.
    
    - #### Frequent User Goals
        1. As a Frequent User, I want to see if there any new recipe added. 
        2. As a Frequent User, I want to see information on the kitchen appliances.

- ### Design
    - #### Colour Scheme
        - The main colour used is the very light grey background (#d4d4d4) and for the dark grey (#343a40) mainly for the buttons and the footer and white for the recipe cards.
    - #### Typography
        - The main font is Roboto which is used at the whole site with a Sans Serif as a fallback font. 
- ### Wireframes
    - Index Page Wireframe [view](https://github.com/milka77/ms3_cookbook/tree/master/static/images/wireframes/landingpage.png)
    - Recipes Page Wireframe [view](https://github.com/milka77/ms3_cookbook/tree/master/static/images/wireframes/recipes.png)
    - Add New Recipe Page Wireframe [view](https://github.com/milka77/ms3_cookbook/tree/master/static/images/wireframes/addnewrecipe.png)
    - Contact Us Page Wireframe [view](https://github.com/milka77/ms3_cookbook/tree/master/static/images/wireframes/contactus.png)
    - Our Brand Page Wireframe [view](https://github.com/milka77/ms3_cookbook/tree/master/static/images/wireframes/ourbrand.png)
    - Mobile Wireframe [view](https://github.com/milka77/ms3_cookbook/tree/master/static/images/wireframes/mobile.png)


## Features
- Responsive on all device sizes
- Interactive elements, contact form sent an acknowledgement


### Existing Features
- #### Landing page 
    - When the site will be loaded the users should find themselves on the landing page, where they can see the header picture with a navigation bar and a welcome message and a short description about the page. Under the description, they are able to see an information bar which is displaying how many total recipes are in the database. Followed by 4 random sample recipes from the collection and under the sample recipes they can find a button which takes the user to see all the recipes. At the bottom of the page, they should be able to see the footer with copyright information and with the social media links on the right. These links are changing the colour and size when the user moves her/his mouse over them. 
- #### Navigation bar
    - The user should see a brand name on the left side followed by four links recipes, new recipe, our brand and contact us and finally a search bar and button on the right side. When the page has more content and the user will scroll down to see the content the header image moving out from the visual area the navigation bar colour will change to white for better visibility and will stick to the top. 
        * __*Brand name:*__ If they click on the brand name the landing page will be loaded, returning "home" from everywhere on the page.
        * __*Recipes:*__ By clicking the recipes link the users should see all the recipes which the site has in the database with a 10 recipe per page pagination.
        * __*New Recipe:*__ By clicking the new recipe link users will see a form. With this form, they can add new recipes to the database. 
        * __*Our Brand:*__ By clicking our brand link the users will see our brand page. 
        * __*Contact Us:*__ By clicking the contact us link the contact form will be displayed where users are able to send messages to the site owner(s).
        * __*Search:*__ Users are able to search in between our recipes.
- #### Recipes
    - On the recipes page, the users should see all the recipes. At one page the site is displaying only 10 recipes at the time. Firstly at the top left corner they can find the pagination information gives information about which recipes are displayed on the current page and how many total recipes are in the database. Under the pagination information in two columns displayed the 10 recipes with a picture on the left, name and short information with a direct link button on the right side of the recipe card. Under the recipes, the users can find the pagination links, which is displaying how many pages are available and highlighted the current page. At both sides of the pagination links, they see an arrow to reach the previous and next pages easily. On the bottom of the page, there is an __"Add new recipe"__ button to add new recipes to the site.
- #### Show recipe
    - By clicking the direct link at the recipe card, the users will see a detailed page which will show all information from the recipe. The name, a short description, dietary type, difficulty, cooking time, serving size, ingredients, preparation and cooking instructions, is there any electrical kitchen appliances required to the recipe and a picture. Under this informations, the users can find the update and delete recipe buttons. 
- #### New recipe
    - At the New recipe page, the users are able to create new recipes and add them to the database by filling out the new recipe form and submit. At the form, the users should see at every required field a little red asterisk. 
- #### Modify, update recipe
    - Users can edit, the existing recipes by clicking on the update recipe button under the detailed recipe view. This will load the update recipe form with already filled input fields from the existing recipe. They can change, modify any of the details with a few easy step. After all de necessary changes are made with a simple click on the update recipe button the recipe is updated, edited and the users will be returned to the recipes page. If the user changes her/his mind they can anytime abort the update function by clicking the cancel button and they will be returned to the recipes page. 
- #### Delete recipe
    - At the detailed recipe page, the users can find the delete recipe button. By pressing this button the recipe will be deleted from the database. 
- #### Search
    - At the right side of the navigation bar, the users can find the search bar with a button. They can search for anything in our recipe database between the recipe names, ingredients and dietary fields. The users need to type the word which they want to search and press enter or click on the search button. The search result will be displayed in the same way as the recipes are displayed in two columns. By clicking the __View recipe__ button they can see the detailed page from the recipe. If the search has no-hit, and an error message will be displayed.
- #### Our Brand
    - The "Our Brand" page will show to the users a variety of kitchen appliances which will make the user's life easier in the kitchen.  They can find a picture and some key information, description form the products. 
- #### Contact us
    - Users can fill out the contact form with their name, email, message and click on the __Send message__ button. If the message was sent successfully an acknowledgement will be displayed with a green background that the message was sent. If there was an error and de message was not sent, an error message will be displayed with a red background. 

---
## Technologies Used
### Programming Languages Used
* HTML
* CSS
* JavaScript
* Python
### Programs, Frameworks and  Libraries Used
* [MongoDB](https://www.mongodb.com/)
* [Google Fonts](https://fonts.google.com/)
* [Bootstrap 4](https://getbootstrap.com/)
* [Font Awesome](https://fontawesome.com/)
* [GitHub Desktop](https://desktop.github.com/)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Favicon generator](https://favicon.io)
* [Heroku](https://heroku.com)
* [GIMP - GNU Image Manipulation Program](https://www.gimp.org/)
---

## Testing
### Responsiveness 
The site was tested with multiple browsers(Opera, Firefox, Chrome, MS Edge) and devices(desktop PC, iPad mini, iPhone SE 2020 and iPhone 6), and with all the options from Chrome Development tools. The pictures and the design were responsive and displayed as they should be. I asked few friends and family members to test the site on their device. 

### Code Validation
* Validated the HTML code with [W3C](https://validator.w3.org/#validate_by_input) and no error found.
* Validated the CSS code with [W3C](https://jigsaw.w3.org/css-validator/#validate_by_input) and no error found.
* Validated the Python code with [PEP8online](http://pep8online.com/) and no error found.
* Validated the JavaScript code with [JSHint](https://jshint.com/) and no error found. 

### Testing User Stories from User Experience (UX) Section
- #### First Time Visitor Goals
    - As a First Time Visitor, I want to easily understand the main purpose of the site.
        1. When entering the site, users are greeted with a welcome message and a big header image with the header text which explaining the site purpose. 
        1. Under the header image comes a clean and easy to use navigation bar with all the site's functions.
    - As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.
        1. The user can find the navigation bar at the bottom of the header image. When the page is scrolled down the header image scrolling up and the navigation bar sticks to the top and changing the background colour so it will be always visible for the users.  
        1. The users easily can choose one of the options from the navigation bar which are: __Home__, __Recipes__, __New Recipe__, __Our Brand__, __Contact Us__ and a __Search bar__.
        1. When a new recipe will be submitted the user will be returned to the *recipes* page where all the recipes are displayed.
    - As a First Time Visitor, I want to easily find social media links, so I can gather more information about the site and site owner.
        1. The footer is visible all the time on the bottom of the site with the social media links. 
        1. When the user using these social media links they will open in a new tab, so they will not loose where they were on the site.
- #### Returning Visitor Goals
    - As a Returning Visitor, I want to find recipes with a specified ingredient or name.
        1. Users just need to type the ingredient name or recipe name which they are looking for in the search bar and press the search button. If the search got any hit it will be displayed every one on the results page.
        1. From there they can visit the detailed recipe page with a single click on the __View recipe__ button. 
        1. If there was nothing found in the database the users will receive an error message.
    - As a Returning Visitor, I want to edit, delete recipes.
        1. On the detailed recipe page at the bottom, they can find the __Update Recipe__ button. 
        1. By clicking this button the edit recipe page will be displayed where the users easily can change, add or remove any ingredients or preparation, cooking instruction.
        1. To save the changes they need to press the __Update Recipe__ button on the bottom of the form, which will update the recipe and return the user to the recipes page.
        1. If the user changes her/his mind they can abort the changes with the __Cancel__ button. 
    - As a Returning Visitor, I want to find the best way to get in contact with the site owner with my questions, ideas.
        1. The navigation bar highlights the Contact Us page.
        1. They can fill out the contact form with their *Name*, *email* and their *message*.
        1. To send the message they need to press the __Send Message__ button. 
        1. A message will be displayed to the user that the message was sent successfully or failed.
    - As a Returning Visitor, I want to find community links.
        1. In the footer, they can find social media links anytime.
- #### Frequent User Goals
    - As a Frequent User, I want to see if there any new recipe added.
        1. On the landing page are displayed the total numbers of recipes in the database.
        1. They can visit the landing page from anywhere just clicked the Brand name in the navigation bar.
    - As a Frequent User, I want to see information on the kitchen appliances.
        1. The information from the kitchen appliances is on the Our Brand page.
        1. Users can easily reach this page from the navigation bar or they can find a red "advertisement" stripe on the top of each recipes detailed view. 

### Manual Testing
- #### Navbar, Footer and all other links 
    - Tested all the links in the navigation bar and in the footer manually.
    - All the social media links are using the `target="_blank"` attribute and they opening in a new tab of the browser.
    - No broken links found during the testing. All the links are pointing on the correct section of the site. 
- #### Recipes and detailed recipe page
    When clicked on the __Recipes__ link all the recipes will be displayed with a 10 recipe per page pagination. The recipe cards will be displayed in two columns on large screens and in a single column on small screen size devices. When the __View Recipe__ link clicked the detailed recipe page will be loaded. The pagination link under the recipe cards shows how many page is available and highlight the current page. 
- #### New Recipe form
    If I leave any of the required fields empty the form will not let me submit it, an error message will be displayed which field is required and will be highlighted. I added a few recipes during the development to test the functionality. The image placeholder was tested and working well when no image is added to the recipe. 
- ####  Update/Edit Recipe
    When I clicked on the __Update Recipe__ link on the detailed recipe page the *Edit Recipe* page will be loaded with pre-filled information from the existing recipe. If I was removed some required fields and tried to submit it, an error message will be displayed that one of the required fields is not filled out and will be highlighted.
- #### Contact Us form
    Tried to submit a form when not all of the required fields was filled out. An error message was displayed that one of the required filed is empty and will be highlighted. At the __Email__ field if it's filled out with not a valid email form, by the submitting will display that the __Email__ field is not containing a @ symbol. After every field is filled out with the correct way and the message submitted, a message displayed as an acknowledgement that the message sent successfully or not.
- #### Search bar
    I typed in the search bar a few ingredient names and pressed enter. All the recipes were displayed which containing the searched ingredient. If there was nothing found in the database an error message was displayed that the search was not found matching data in the recipes.

### Known Bugs
- Update function will remove the image if the image not added again to the file input before sumbitting. (Unfortunatly because of the short project submit deadline don't have time to fix this bug. Will do it later)

---
## Deployment
- #### Heroku Deployment
The following steps are required to deploy the project to [Heroku](https://heroku.com)
1. Login to the Heroku website and create a new Heroku app. Need to choose a unique name for your app and your region.
1. You need to create a __*requirements.txt*__ file, with the following command in the terminal: `pip3 freeze --local > requirements.txt`, which will contain the dependencies list.
1. You need to create a __*Procfile*__, to tell Heroku what is the type of your project and how to run it. The Procfile name must start with a capital "P" and should not have any extension. Use the following command in the terminal: `echo web: python app.py > Procfile`
1. You need to add your remote repository with `git remote add heroku <yourHerokuAppGitLinkHere>`.
1. You need to add, commit and push the newly added 2 files to GitHub. With the following commands in the terminal: `git add <filename>`, `git commit -m "Added Procfile and requirements.txt"` and `git push origin master`
1. Login to Heroku from your terminal use `heroku login` and follow the instructions. 
1. After a successful log in you need to push your project to Heroku with `git push heroku master` command. You should see the message that the push was successfully deployed to Heroku.
1. Need to start a web process with `heroku ps:scale web=1`.
1. At the Heroku dashboard's settings you need to set the following Config Vars:
    - IP : 0.0.0.0
    - PORT : 5000
    - SECRET_KEY: <YourSecretKey> - *must match with ones you entered in .env.py file*
    - MONGO_URI: <LinkToYourDatabase> - *must match with ones you entered in .env.py file*
    - DEBUG: FALSE
1. After these steps are done you app is ready to run. Click on the "Open App" button to view the app.

- #### Local Deployment
1. On the GitHub page you can click the "Clone or Download" button then click on the "Download Zip" button. After the download finished you need to extract the files to your selected folder. Or you can enter the following command into your terminal window to clone the repository: `git clone https://github.com/milka77/ms3_cookbook.git`
1. You need to install or sign up [MongoDB](https://www.mongodb.com/) and create a new Database with the name: "cook_book".
1. In the "cook_book" database you need to create the following collections: 
    - categories
       ``` 
       _id: <ObjectId>
       category_name: <String>
       ```
    - difficulty
        ```
        _id: <ObjectId>
        recipe_difficulty: <String>
        ```
    - recipes
        ```
        _id: <ObjectId>
        recipe_name: <String>
        recipe_info: <String>
        cooking_time: <String>
        category_name: <String>
        servings_size: <String>
        recipe_difficulty: <String>
        ingredients: <Array>
        instructions: <Array>
        you_will_need: <Array>
        recipe_image_name: <String>
       ```
1. You need to install all the requirements with entering the following code to the terminal: 

    `pip3 install -r requirements.txt`
1. You need to create the environment variables with the following steps: 
    - Create a .env.py file in your root directory with these lines: 
        ```
        import os

        os.environ["SECRET_KEY"] = <enterYourSecretKey>
        os.environ["MONGO_URI"] = <enterYourMongoDBURI>
        ```
    - Add the following line to the `app.py` file after the imports
        
        ``` 
        import env as config 
        ```
1. Finally, you can run the app type in the terminal `python3 app.py`
---
## Media / pictures
- The page header image is from [Free Web Headers](https://www.freewebheaders.com/)
- The placeholder image was created with GiMP