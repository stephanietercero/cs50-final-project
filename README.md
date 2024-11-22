# STEPH’S RECS
# Video Demo: <https://youtu.be/uBLT_6AEzes>
# Project Description
## **Project Goal**
My goal for this final project was to create a website (accessible by anyone in possession of the link) that is a consolidation of my personal collection of travel recommendations and wish lists (ie. restaurants, bars, cultural visits) from cities around the world that I have visited or wish to visit; a one-stop-shop if you will. My goals were to create a visually friendly search environment that I will want to use, and I also want to be able to send the link of this website to friends and family so they will have access to a visually friendly search tool at their fingertips that they can use autonomously, when looking for restaurant and travel recommendations.

## Problem I am Solving Part I
Even before starting the CS50 course, I had exported my personal database of addresses from the “Mapstr” app I had been using because I did not like the UX (user experience).  I had no use for the app anymore because every address showed up as a dot on a map, there was no list element, and I did not picture myself clicking on each map dot individually to find what I was looking for. It was simlply not a fluid experience, and it was taking so much time.


## Problem I am Solving Part II
I have friends and family ask all of the time for restaurant and museum recommendations and I was getting tired of going through my addresses one by one from Mapstr by clicking on each one, manually searching each address on Google and/or social media and then copying information into a Google document which would serve as a personalized travel recommendation list, not necessarily reusable. This has been extremely time consuming for me and I wanted to find a way to save myself time, while still being able to share my addresses with friends and family because my list represents many years of curiosity and adventures.

## Ideal Use Case
**Scenario I:** I am searching for an Italian restaurant in Paris and I can go onto my own website, navigate to “France” and filter by "Paris" and then “Italian.” I find in just a matter of seconds some trusted dining options.

**Scenario II:** A friend or family member asks me for recommendations. I send a single link and they can navigate my website autonomously to find recommendations that suit their taste and upcoming travel. Or even a local spot if they are living in one of the cities with addresses available.


## How Users Will Interact With the Website
- Ideally I want the user to be able to go on the website without need for authentification, and be able to see the destinations available from a drop down menu on the navigation bar, (ie. Asia, Africa, Europe etc.) click on a destination, and be shown the countries (in a visually pleasing manner) that have available addresses in that destination.
- I want this page of “Countries” to be dynamically loaded. Each country is a button, which is also an image with defining features of that country.
- For example when a user clicks on “Africa” they will see the “Morocco” and “South Africa” as images which are also buttons.
- If the user clicks on South Africa, they will see a table of all addresses available in South Africa, listed in rows.
- The table will show the address on very left column, and as the columns advance to the right, users will have access to even more information about each address such as the corresponding region, city, category, sub-category and so on.
- Each column can be searchable so if a user wants to find an address in the “Essaouira” in Morocco, they will be able to search this name either in the city-specific column or the principal search bar at the head of the table, and they will see corresponding addresses.
- Users will be able to create their own pared-down list if they desire and they can also visualize the complete list for the country.
- Users have the option to **copy the list to their clipboard** or to **export as an Excel document** and users have buttons above the table to proceed to these actions.
- Users can navigate to the “Resources” page of the website to get an understanding of how the categories have been set up, the travel resources and inspiration Steph interacts with in her daily life, and the names of all photographers and videographers who have images and/or videos displayed on the website. Each name will be linked to a personal photography/videography page.
- All images were taken from [unsplash.com](unsplash.com) and [pexels.com](pexels.com), both websites allowing for image use without licenses necessary. I of course, am only using images and videos with no “License” requirement. These websites allow downloads of beautiful stock photos, which I found more than perfect for my website.
- Users will also navigate to the “About” page to get a short and sweet global understanding of the origins and inspiration of the website.




## What Each Project File Contains and Why
## Project Structure

#### Project
1. instance
   - project.db
2. static
   - images
     - images saved as jpg
   - videos
     - video saved as mp4
   - styles.css
3. templates
   - about.html
   - index.html
   - layout.html
   - resources.html
   - selection.html
4. address.csv
5. app.py
6. destination.csv
7. README.me
8. requirements.txt
9. run.py

### Project
My **project folder** is comprised of the following folders: **instance, static and templates.** Directly in my project folder (not having any sub-folders) are the following documents: **address.csv, app.py, destination.csv, README.me, requirements.txt and run.py.** (Numbers 4 - 9 above)

#####
**Address.csv:** this is one of my two database tables. This table is comprised of all of my **1,665** addresses (restaurant, hotels, visits…) with corresponding categories. The columns in this table are: _address_id, destination_id, address_name, principal_category, sub_category_1, sub_category_2 and sub_category_3._

#####
**Destination.csv:** This is my second database table I have for the website, with information solely concerning destinations I have for the website. This table has the following columns: _id, city, region, country, destination._

#####
**App.py:** App.py serves as the main entry point and is the main script for running a Flask web application. Here is what I have imported:
`from flask import Flask, render_template, request, jsonify`
`from flask_sqlalchemy import SQLAlchemy`
`import pandas as pd`
`from sqlalchemy import text`
`import os`

Here is how the app is initialized: `app = Flask(__name__)`

In app.py I define the models (databases) by column and in app.py I have my program read the CSV files.
The different routes in app.py are the following:

1. `@app.route('/', methods=["GET"])` which renders the **index.html** template, which is the default, or home page of my website. My home page has eye-catching dynamic visual content with a nice text overlay and a navigation bar at the top of the page boasting a drop-down menu.

2. `@app.route('/selection/<selection_type>/<selection_value>', methods=["GET"])`
Which renders **selection.html**, the file that creates the logic for when a user interacts with the website. **Selection.html** is the most complex route I have for this website as I have the program conditionally render content based on the step variable that I define. JavaScript is very present in this html document as the logic implemented is based off of user interaction with the website.

3. `@app.route('/resources', methods=["GET"])`
This route renders **resources.html** which is where you can find information about the categories on the website, personal travel resources which inspired me, and photo and video credits, with links to each photographer and videographer’s page.

4. `@app.route('/about', methods=["GET"])`
This route renders the **about.html** page which is a page where you can find a global overview of the website, its inspirations and origins.

#####
**Requirements.txt:**  this file specifies the Python packages my project depends on.

#####
**Run.py:** this file is used to start the Flask web application. It imports the Flask app instance from app.py and runs it but only when the script is executed directly.

#####
**README.me:** this file contains multiple sections, explaining the project in detail.

### Instance
**Project.db:** is the database my website is interacting with (I describe the two csv files just above). When I click into project.db I am able to access phpLiteAdmin which is where I can visualize my two database tables.

### Static
In the **static folder,** I have the following sub-folders: **images, videos, and styles.css.**

####
**Images:** This is where I have saved ALL images I use on the website in **jpg** format, and all lowercase letters, with clear descriptions of what the images are. Before uploading images into this folder, I compressed them to speed up their loading time when they are displayed.

####
**Videos:** This is where I have saved in **mp4** format, the video (a collection of smaller videos I merged together) I used on the home page of the website, my home page, or default route “/”.

#####
**Styles.css:** This is where all style elements of my website are located.

### Templates

######
**About.html:** This route renders the about.html page which is a page where you can find a global overview of the website, its inspirations and origins. Here you will find Jinja and HTML.

######
**Index.html:** This is the template of the default, or home page of my website. My home page has eye-catching dynamic visual content with a nice text overlay and a navigation bar at the top of the page boasting a drop-down menu. Here you will find Jinja, HTML and JavaScript.

######
**Layout.html:** This serves as a template for other HTML files, containing elements that are shared across multiple pages. Here you will find Jinja, HTML and JavaScript.

######
**Resources.html:**  Resources.html is where you can find information about the categories on the website, personal travel resources which inspired me, and photo and video credits, with links to each photographer and videographer’s page. Here you will find Jinja and HTML.

######
**Selection.html:** This is the file that creates the logic for when a user interacts with the website. Selection.html is the most complex route I have for this website as I have the program conditionally render content based on the step variable that I define. JavaScript is very present in this html document as the logic implemented is based off of user interaction with the website. Here you will find Jinja, HTML and JavaScript.

## Design-Choice Debates
I debated one major design choice which impacted the main functionality of my website. Having a table of addresses displayed for each country, once a country button/image was clicked on was not the original plan. In fact I originally wanted the user to click through to countries, and then to regions, and then to cities the same way they click into “countries” so by having an image be the button. I wanted the user to then click on a button for each category and sub-category. As I was designing and implementing I realized it made the most sense for users, once having reached a country, to be able to visualize the entire list but with ways to filter based on region, city, principal category and all sub-categories. I made sure to include buttons so users can **export** and/or **copy** the list and are able to use as they please. I felt this way of implementation gave even more **flexibility** to the users, and more freedom on how they could use the website to achieve their goals.

### Steps
1. **Database / Category Creation**
   - I individually went over 2,000 addresses in my Google Sheet (exported from Mapstr) and checked if the places were still in existence.
   - I created categories that were detailed enough, but could be used multiple times in my database, in order for lists and sub-lists to be created
   - I decided to organize my database into two tables: “Destination” and “Address”
   - In the “Destination” table I organized each “destination” into countries, regions and cities. For example - Europe - Italy  Puglia - Brindisi
   - In the “address” table I organized into “principal category”, “sub category 1”, “sub category 2” and “sub category 3”. For example - Eat & Drink - Eat - Casual/Take Away - Burger
2. **Set Up Coding Environment on vs code in my CS50 Codespace**
3. **Design My Website**
   - A lot of drawings by hand, looking for inspiration in magazines, on websites and travel apps and blogs to understand what user flow I appreciate as well as understanding my own personal preferences, and what is current vocabulary used (or not used) by travel-forward websites
4. **Implement Basic Features**
   - Integrate Database - used PHP Lite Admin which I was familiar with a bit from the Finance Problem
   - Back end development - Python, Flask, figuring out what I needed to import based off of my goals for the website, setting up routes, figuring out what templates the routes needed to render…(details of each file mentioned above)
   - Front end develmopment - Creation of templates using HTML, Jinja, JavaScript, CSS…(details of each file mentioned above)
5. **Test and Iterate**

# Conclusion
The database portion of my website was definitely one of the most time-consuming, aside of course from the back-and and front-end development which were without a doubt, challenging. I learned an incredible amount from diving into this project. This project has solved a problem for me, will serve my personal use but most importantly can be used by others. I was able to implement concepts learned in this course. I know I learned a lot throughout CS50 because I knew what types of questions to ask myself in the creation and development processes. I have the goal of keeping this website alive so it outlives this course. I aim to continue to nourish my database, while making my website accessible to others all the while. **Thank you to the incredible CS50 staff!**
