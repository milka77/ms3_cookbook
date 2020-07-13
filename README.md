# Krisztian's Online Cookbook
Milestone project #3: Data Centric Development - Code Institute

This project is an online cookbook. No authentication needed to read, search, create recipes. 

Link to the live site on Heroku: [here](https://ci-ms3-krisztians-cook-book.herokuapp.com/)

Picture here >>> 
---

## User Experience (UX)

- ### User Stories
    - #### First Time Visitors Goals
        1. As a First Time Visitor, I want to easily understand the main purpose of the site.
        2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.
        3. As a First Time Visitor, I want to easily find the social media links, so I can gather more information about the site and site owner. 

    - #### Returning Visitor Goals
        1. As a Returning Visitor, I want to find recipes with specified ingredient or name.
        2. As a Returning Visitor, I want to edit, delete recipes.
        3. As a Returning Visitor, I want to find the best way to get in contact with the site owner with my questions, ideas. 
        4. As a Returning Visitor, I want to find community links.
    
    - #### Frequent User Goals
        1. As a Frequent User, I want to see if there any new recipe added. 
        2. As a Frequent User, I want to see information on the kithcen appliances.

- ### Design
    - #### Colour Scheme
        - The main colour used are the very light grey background (#d4d4d4) and for the dark grey (#343a40) mainly for the buttons and the footer and white for the recipe cards.
    - #### Typography
        - The main font is Roboto which is uses at the whole site with a Sans Serif as a fallback font. 
- ### Wireframes
    - Index Page Wireframe [view]()
    - Recipes Page Wireframe [view]()
    - Add New Recipe Page Wireframe [view]()
    - Contact Us Page Wireframe [view]()
    - Our Brand Page Wireframe [view]()
    - Mobile Wireframe [view]()


## Features
- Responsive on all device sizes
- Interactive elemenets, contact form sent acknowledgement


### Existing Features
- #### Navigation bar
    - The user should see a brand name on the left side followed by four links recipes, new recipe, our brand and contact us and finally a search bar and button on the right side. When the page has more content and the user will scroll down to see the content the header image moving out from the visual area the navigation bar colour will change to white for better visibility and will stick to the top . 
        * __*Brand name:*__ If they click on the brand name the landing page will be loaded, returning "home" from everywhere on the page.
        * __*Recipes:*__ By clicking the recipes link the users should see all the recipes which the site has in the database with a 10 recipe per page pagination.
        * __*New Recipe:*__ By clicking the new recipe link users will see a form. With this form they can add new recipes to the database. 
        * __*Our Brand:*__ By clicking the our brand link the users will see the our brand page. 
        * __*Contact Us:*__ By clicking the contact us link the contact form will be displayed where users are able to send messages to the site owner(s).
        * __*Search:*__ Users are able to search in between our recipes.

- #### Landing page 
    - When the site will be loaded the users should find themselfs on the landing page, where they can see the header picture with a navigation bar and a welcome message and a short description about the page. Under the description they are able to see an information bar which is displaying how many total recipes are in the database. Followed by 4 random sample recipes from the collection and under the sample recipes they can find a button which takes the user to see all the recipes. At the bottom of the page they should be able to see the footer with copyright informations and with the social media links on the right. These links are changing the color and size when the user moves her/his mouse over them. 

- #### Recipes
    - On the recipes page the users should see all the recipes. At one page the site is displaying only 10 recipes at the time. Firstly at the top left corner they can find the pagination information gives information about which recipes are displayed on the current page and how many total recipes are in the database. Under the pagination information in two columns displayed the 10 recipes with a picture on the left, name and short information with a direct link button on the right side of the recipe card. Under the recipes, the users can find the pagination links, which is displaying how many pages are available and highlighted the current page. At both sides of the pagination links, they see an arrow to reach the previous and next pages easily. On the bottom of the page, there is an __"Add new recipe"__ button to add new recipes to the site.
- #### Show recipe
    - By clicking the direct link at the recipe card, the users will see a detailed page which will show all information from the recipe. The name, a short description, dietary type, difficulty, cooking time, serving size, ingredients, preparation and cooking instructions, is there any electrical kitchen appliancer required to the recipe and a picture. Under this informations the users can find the update and delete recipe buttons. 
- #### New recipe
    - At the New recipe page the users are able to create new recipes and add them to the database with filling out the new recipe form and submit. At the form the users should see at every required field a little red asterisk. 
- #### Modify, update recipe
    - Users can edit, the existing recipes by clicking on the update recipe button under the detailed recipe view. This will load the update recipe form with already filled input fileds from the existing recipe. They can change, modify any of the details with with a few easy step. After all de necessarry changes are made with a simple click on the update recipe button the recipe is updated, edited and the users will be returned to the recipes page. If the user changes her/his mind they can anytime abort the update function by clicking the cancel button and they will be returned to the recipes page. 
- #### Delete recipe
    - At the detailed recipe page the users can find the delete recipe button. By pressing this button the recipe will be deleted from the database. 
- #### Search
    - At the right side of the navigation bar the users can find the search bar with a button. They can search anything in our recipe database between the recipe names, ingredients and dietary fields. The users need to type the word which they want to search and press enter or click on the search button. The search result will displayed at the same way like the recipes are diplayed in two columns. By clicking the __View recipe__ button they can see the detailed page from the recipe. If the search has no hit, and error message will be displayed. 
- #### Contact us
    - Users can fill out the contact form with their name, email, message and click on the __Send message__ button. If the message was sent successfuly an acknowledgement will be displayed with a green background that the message was sent. If there was an error and de message was not sent, an error message will be displayed with a red background. 

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
---

## Testing
### Navigation


### Testing the links
Tested all the links manually. No broken links found during the testing. All the social media links are using the `target="_blank"` attribute and they opening in a new tab of the browser.

### Code Validation
* Validated the HTML code with [W3C](https://validator.w3.org/#validate_by_input) and no error found.
* Validated the CSS code with [W3C](https://jigsaw.w3.org/css-validator/#validate_by_input) and no error found.

## Deployment


---
## Media / pictures
The page header image is from [Free Web Headers](https://www.freewebheaders.com/)