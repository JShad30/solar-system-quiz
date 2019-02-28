# Solar System Quiz - Practical Python Milestone Project

This is my Milestone Project for the Practical Python part of the Full Stack Development Course. This site has been developed to give the user a basic understanding of the solar system. They can then test their knowledge by taking the quiz and compare their performance with those of other users.

The site has the same background images throughout the site, creating a consistent feel and user experience. The Solar Info page contains information that may be of interest to the user and uses images and an interactive style that the user will find visually appealing.

## User Experience

Before beginning the build of the site, I created wireframes to help with the design. These can be found in the following link:

### Example uses of site

I have aimed to make this site easy to use and self explanitory in how to use it. The front page is simple with just a site overview, in basic overview of the two main following pages, the 'Solar System Info' page and the 'Take Quiz' page.

At any time while on the site, the user will have access to the social media links, displayed in the footer of every one of the pages, or can revert to the home page, by clicking the 'Solar System' writing, displayed at the top of every page. However, where necessary there are also return home buttons throughout the site.

#### Home Page

The homepage of this site contains an overview to introduce the user, and two links: First to the 'Solar System Info' page and the second to the 'Take Quiz' page.

#### Solar Info Page

For those interested to learn more about the solar system, they can click on the solar info page. This displays information about the subject, and images of the objects are displayed through the page. Each object has a brief overview, which can be expanded to show more information if the user clicks the 'More Info' button. At the end of this page there is a link direct to the quiz.

#### Take Quiz

The 'Take Quiz' page can be linked to from the home page or the bottom of the 'Solar System Info' page. 

Once the submit button has been selected the user is provided with a message, which is different depending on the score they achieved. If they want to see the leaderboard they can go here. Usernames are used on the leaderboard, as not all players would necessarily want their names listed against their score. 

#### Questions

The questions are listed and need to be answered. When finished the user can click the 'Submit' button and be take through to the quiz completed section.

#### Quiz Completed

A message is displayed to the user which varies depending on the score achieved in the quiz. If the user has achieved a high score, the message will be congratulatory, and a lower score will persuade the user to visit the 'Solar System Info' page. In all cases, the user will also find a link through to the 'leaderboard' page.

#### Leaderboard

If the user clicks on this link, they will be able to see the usernames and the scores of the previous users. They will be able to search the list and see where they stand. This page also carries a link back to the home page.

## Features

### Form 

When the user clicks on this button, they are taken to a page with a form which asks them to provide their first name, last name and a username. This is run through the 'solar-quiz.html' page. When the form is filled out, the first name, last name and the username is stored in the 'names.json' file These are called on later in the following pages.

### Questions

They are then taken to the quiz questions. They will then answer each of the questions. All questions need to answer as the radio buttons are set as 'required'. The quiz pages are implemented through the templates, solar-quiz.html, solar-quiz-user.html, questions.html, quiz-completed.html. When filling out the information on the solar-quiz page, the user initialises a cookie that is then stored for the rest of the quiz.

### Quiz completed message

The message is displayed using Python logic in 'run.py’ and displayed using the 'quiz-complete.html'. The message displayed depends on the score the player has got. 

The message displayed varies depending on what the user scored. This is currently built in the run.py page with an if statement. Prior to this message being displayed the score as a percentage should be worked out. This would allow new questions to be added to the quiz without the need for the code in run.py to be changed.

### Leaderboard

The leaderboard is presented on the 'leaderboard.html' page and its route is /solar_quiz/leaderboard. The leaderboard is there for players that want to see their performance compared to other players.

### Extra Features that could be added

I would in the future consider adding a feature where when the form is completed it does a check for the existing usernames. If there is a clash the user would be asked for a different username.

## Technology Used

This project was built using different languages, libraries and frameworks. 

The site has been built using the Python based Flask framework (http://flask.pocoo.org/) and is run from the 'run.py' file. All the pages are routed from here, and contain the logic required for the quiz. Python has been used to create the logic within the 'run.py' file (https://www.python.org/). The 'jinja template engine' (http://jinja.pocoo.org/) has been used within the templates html pages.

The template pages have been written with HTML5 (http://www.html5.com/) and styled with CSS3 (www.css3.com) in the style.css file. CSS3 was used to create the mobile responsiveness seen across the whole site. It has also been used to create the hover effects for the buttons and the social icons. On each of the pages, you will find the jinja template engine used. A 'base.html' page has been created to contain the HTML code that is to be used on each of the pages i.e. The head, header and the footer.

On the 'Solar Info' page uses jQuery (https://jquery.com/) to reveal the extra information if the user clicks on the 'More Info' button. When one of these buttons is selected, a 'slideToggle' instruction is used. The other solar objects information has a 'slideUp' instruction placed on it meaning that only one object will have its information revealed at any one time. jQuery is also used in the navbar which changes from transparent to black when the user scrolls down the page.

The data for the questions asked in the quiz, the information contained on the 'Solar Info' page, and the names gathered in the form when starting the quiz are contained in their own individual json files (https://json.org/). 

Git was used throughout the project for version control. I also used the 'File Revision History' to revert when there was experimentation with different design techniques.

## Testing

The CSS was run through a CSS validator and errors were corrected. It now shows no errors. The javascript/jquery code was validated using jshint and showed no errors.

The site has been tested manually by clicking the links to the pages and checking all of the jQuery options. It has also been tested in different browsers.

The quiz has been completed many times in order to check scores calculate correctly.

## Issues While Building the Project

At first, I was storing the variables in a separate text file and was then going to call them at the end and add them with score to a separate text file. Following advice from the tutor a session cookie was opened at the solar-quiz-user page and kept open to the end. The variable of score was set early at 0, and then 1 is added with each correct answer. This worked better, except for the following issue...

When a username, first name and last name are filled out in the form a session cookie is initialised. This then is carried throughout the quiz to the quiz-completed page. I noticed that the session cookie remained open at this point. Therefore, if the user clicked the back arrow in their browser it would return to the last question (or further depending how many times the back arrow was clicked). They could then submit the answer again which would add to their score .......How problem eliminated?

I have tried different methods of storing the data regarding the username, firstname and lastname of the users. The current site has them stored in a dictionary file and then they are read as a json file in the run.py file.

## Deployment

This project has been deployed to Heroku by doing a git push. This create the site on the Heroku platform.

## Credits

### Media

There are several images used throughout the site:

The background picture used throughout the entirety of the site was sourced from Pixabay.

All images of the planets and objects on the Solar Info Page were obtained from Pixabay other than the following:
    Oort Cloud - Fine Art America
    Video comparing Solar System object sizes in Solar Info Page - MetaBallStudio Youtube Channel

### Acknowledgements

The basis of the information was taken from various websites primarily wikipedia, but information was also obtained from the official NASA website and solarviews.com.

I had assistance from tutor support and the mentor on some of the areas of the project when I had difficulties as specified earlier. 




