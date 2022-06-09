**_Games Review_**

WELCOME TO GAMES REVIEW

Being a gamer my self I wanted to create a website database where user’s have control on the content that can be added to the database. I having played a lot of games I wanted to create something where people can add their honest opinions about games. The website uses a number of different languages and is a combination of POSTGRESSQL and MONGODB.

So what language and technology’s  did I use for the creation of the database.

PostgreSQL and Mongo dB were used to create the database it is self, with python language used to create the routes for the database. I defiantly found tricky combining both database and the overall creation of the database it is self.

PostgreSQL part of the database includes the publishers titles and review sections of the database.  The Mongo dB side of the database handles the user’s login and registration which I have included a Werkzeug password hash to help protect users and included defensive programming for users as well. I originally wanted to have the user’s models created inside the PostgreSQL database, but I found creating the routes to difficult as there was no learning materials provided for this, so I decided to user mongo dB instead.

Html, CSS and JavaScript were used to create the front end of the website. For the design of the front end, I used Materialize templates which includes custom CSS and responsiveness for all devices included in the package. All images I have used in the website are all for educational purposes only.

My overall goal for this project was to keep the html JavaScript and CSS simple as I wanted to ensure that I added full CRUD functionality to all pages of the database with a flash message and a fully functioning register and login system with a logout capability. 

This project certainly tested me during it is development.


Game review <a href="https://gamesrevbeta.herokuapp.com/" target="_blank" rel="noopner">Game Review</a>



![Games Review responiveness](gamesreviewc/static/image/responisvems3.PNG)

# Contents

* [**User Experience UX**](<#user-experience-ux>)
   * [User Stories](<#user-stories>)
   * [**Wireframes**](<#wireframes>)
   * [**Design Choices**](<#design-choices>)
       * [Color Scheme](<#color-scheme>)
   * [**Features**](<#features>)
       * [Home](<#Home>)
       * [Game](<#Game>)
       * [Score](<#Score>)
       * [Publishers](<#Publishers>)
       * [Add-Publishers](<#Add Publishers>)
       * [Edit-Publishers](<#Edit Publishers>)
       * [Titles](<#Tiles>)
       * [Add-Games](<#Add Games>)
       * [Edit-Games](<#Edit Games>)
       * [Reviews](<#Reviews>)
       * [Add-Reviews](<#Add Reviews>)
       * [Edit-Reviews](<#Edit-Reviews>)
       * [Profile](<#Profile>)
       * [Logout](<#Logout>)
       * [Register](<#Register>)
       * [Login](<#Login>)
* [**Future Features**](<#future-features>)
* [**Technologies Used**](<#Technologies-Used>)
* [**Testing**](<#testing>)
* [**Deployment**](<#deployment>)
* [**Credits**](<#credits>)
* [**Content**](<#content>)
* [**Future Features**](<Future-Features>)
* [**Acknowledgements**](<#acknowledgements>)                

# User Experience (UX)

## User stories

 ### First time Vistor Goals 
1. As first time user i would like some information one what the site is and what the sites does.
2. The interface to be easy to use and self-explanatory. 
3. I want to be able to access the site on my phone and be easy to use while im using smaller devcies.
4. I would like to know if m was registration sucessful.

 ### Returning Vistor Goals   
1. I would like to be able to add and edit my comments that i post online and be able to delete them if i so require.
2. I have the ability to log out, and am notified when this is successful and i have logged out
3. I would like have a warning message appear before i delete any information form the site. 

 ### Frequent User Goals
1. when a user, logs in would like to know if i have been logged in correclty.
2. As returing user i want to know that my password is secured and that nobody can access it.
3. Restrictions on certians on the database so that i can cause my self any issues and have to contact the developer.


# Wireframes
The wireframes for ‘Games Review’ were produced in[Balsamiq](https://balsamiq.com).
There are frames for a full width display ( 1920 x 1080 package)and a small mobile 
device (360 x 640). The final site varies slightly from the wireframes due to bugs and design 
changes during development that occurred during the creation process. Mobile wireframes havent been included due to the use of Materialize as this
inculdes integrated responsivness package.

 

![Wireframe Desktop](gamesreviewc/static/image/frames1.PNG)
![Wireframe Desktop](gamesreviewc/static/image/frames2.PNG)
![Wireframe Desktop](gamesreviewc/static/image/frames3.PNG)

[Contents](<#contents>)

# Design Choices
 When designing the games reveiw database I wanted it to be to be simple to use, as wanted the CRUD functionality present in the databse . Games review contains 13 pages which 11 pages relate to Crud functions with in the database. After spending serval hours looking at Materialize i eventually decided on cards, collapsibles and a nav bar with a built side nav bar for the desgin. I wanted the overall look of the side to feel simple and easy to use. All pages are linked up either via url`s or with buttons directing you to the different pages on the site.

 The nav bar covers all 13 pages of the side which is kept on the base template, across all the pages i have put in a background image which gives the site a nice contrasts from the text on the page. Early on in the design I knew i was going to use green for the overall look of the site, I orginally choose blue for the text but due to it being difficult to see and changed the text colour scheme to white which stood out more. 

The game page was designed to give users ideas of games ideas that they can input into the database. All the images on the games page are for educational purposes only.
The design for the page comes from materialize cards which i edited the background to white and the text to a dark green colour.

During the final stages of devlepoment i choose to lock out users from deleting publishers as this ties all the relational database together. i wnated to give the uses so feed back and warining messages so i choose to implement flash messages.
 

![Hex Color](assets/images/hex1.PNG)
 THe colors that where choosen for the history quiz are displayed in image above.

 Red Copper with a hex code of #9e2c0b was used for text, backgorund and hoover effects.(Red- Copper colour)

 White smoke with a hex code of #f6f6f6 was used text, backgorund and hoover effects.(White Smoke)

  

[Contents](<#contents>)

# Features
### Home
The quiz of the world is a simple quiz game that contains 3 buttons on the home page. Each button will take user to three different pages. The buttons will be highlighted once the user clicked on them, this so that the user and keep track of which page they are on.

![Home](assets/images/home1.PNG)

### Instructions
The instructions page contains a summary of the games rules as well as button to return home.
![Instructions](assets/images/ins.PNG)

### Game
The game contains multiple different features which are designed to help the user while playing the quiz of the world.

1.	Located on the top left is a question counter to help the user keep track of what question they are up too.
2.	Below the question counter is a progress bar which fills up as the user progress through the quiz.
3.	Located on the top right is a score counter which will help the user keep track of the scores. 
4.	THe questions are displayed below the progress bar and change at random once a question has been answered.
5.	The quiz it is self is a multiple-choice quiz with four possible answers with 17 questions in total.
6.	Each option will change colour once selected. 

![Game](assets/images/test1.png)

### Score
The score page has a line of text and a name box as well as two buttons which will either restart the quiz or take the user back to the home page. 

![Game](assets/images/score1.PNG)

[Contents](<#contents>)

## Deployment

  ### **Deployment**

  The site was deployed using GitHub. THe following step will depoly You matter site.
  1. on the github repository, naviagte to **Settings** tab.
  2. Once on setting page, naviagte to **Pages** on the left hand side of the screen second from the bottom.
  3. Under **Source**, select the branch to **main**, then click **save**.
  4.  once you have selected the main branch, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 
 
 ![GitHub pages for deployment](assets/images/github.jpg)
 
 # Technologies Used
   
* [HTML5](https://html.spec.whatwg.org/) -Used to create the contents and structure for the website.
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html) -Used to create the styling.
* [Balsamiq](https://balsamiq.com/wireframes/) - Used to create the wireframes.
* [Gitpod](https://www.gitpod.io/#get-started) - Used to deploy the website.
* [Github](https://github.com/) - Used to host and edit the website code.
* [Code Beautify](https://codebeautify.org/jsvalidate) - To test and run the code
* [W3 Schools](https://validator.w3.org/)- To test the html and css code.
* [JavaScript (ES6)](https://open-vsx.gitpod.io/vscode/item?itemName=xabikos.JavaScriptSnippets)
* [ami responsive design](http://ami.responsivedesign.is) - To test out responsiness all devices

[Contents](<#contents>)

# Testing
 Please refer to [**_here_**](TESTING.md) for more information on testing 'Quiz Of The World'.

The live link will take you directly to **History Quiz** repository - https://github.com/Jon9851/History-Quiz
  
  # Clone  Repository
   To Clone a repository use the following steps to guide you throught it.
   1. Under the repository’s name, click on the code tab.
   2. click on the clipboard icon to copy the given URL.
   3. In your IDE of choice, open Git Bash.
   4. Change the current working directory to the location where you want the cloned directory to be made.
   5. Type git clone, and then paste the URL copied from GitHub.
   6. Press enter and the local clone will be created.

   ![clone Image ](assets/images/clone.png)



[Contents](<#contents>)

### Credits
1. W3schools- I used their tutorials on HTML and CSS for further understanding and troubleshooting  throughout my project.
2. Stack Overflow- I used Stack Overflow to get a more in depth understanding on HTML and CSS throughout my project.
3. Code Institute Example of the READ.MD- I used these as template when planning and writing my README file.
4.Code Institute tutors that helped me during my project.

[Contents](<#contents>)

# Acknowledgements
 
 The site was cerated for my milestone project 1 for the [Code Institute](https://codeinstitute.net/) Full Stack Software Developer diploma. I would like to thank all the tutors at the code institute for their help during the development of my first milestone project. I would aslo like to thank [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/) for his guidence and help as his feedback was extremely key in completing my first milestone project.
 Brain Codex for help during the creation process. [Brian Codex](https://github.com/briancodex/quiz-app-js)