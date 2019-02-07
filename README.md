# Solar System Quiz - Practical Python Milestone Project

This is my Milestone Project for the Practical Python part of the Full Stack Development Course. This site has been developed to give the user a basic understanding of the solar system. They can then test their knowledge by taking the quiz, and compare their performance with those of other users.

The site has the same background images throughout the site, creating a consistent feel and user experience. The Solar Info page contains information that may be of interest to the user and uses images and an interactive style that the user will find visually appealing.

## User Experience

Before beginning the build of the site, I created wireframes of the site, to help with the design. These can be found in the following links:......................................

### Example use of site

I have aimed to make this site easy to use and self explanitory in how to use it. The front page is simple with just a site overview, in basic overview of the two main following pages, the 'Solar System Info' page and the 'Take Quiz' page.

At any time while on the site, the user will have access to the social media links, displayed in the footer of everyone of the pages, or can revert to the home page, by clicking the 'Solar System Quiz' writting, displayed at the top of every page.

### Home Page

The homepage of this site contains an overview to introduce the user, and two links: First to the 'Solar System Info' page and the second to the 'Take Quiz' page.

### Solar Info Page

For those interested to learn more about the solar system, they can click on the solar info page. This displays information about the subject, and images of the objects are displayed through the page. Each object has a brief overview, which can be expanded to show more information if the user clicks the 'More Info' button. At the end of this page there is a link direct to the quiz.

### Take Quiz

The 'Take Quiz' page can be linked to from the home page or the bottom of the 'Solar System Info' page. 

Once the submit button has been selected the user is provided with a message, which is different depending on the score they achieved. If they want to see the leaderboard they can go here. Usernames are used on the leaderboard, as not all players would necessarily want their names listed against their score. 

### Questions

The questions are listed and need to be answered. When finished the user can click the 'Submit' button and be take through to the quiz completed section.

### Quiz Completed

A message is displayed to the user which varies depending on the score achieved in the quiz. If the user has achieved a high score, the message will be congratulatory, and a lower score will persuade the user to visit the 'Solar System Info' page. In all cases, the user will also find a link through to the 'leaderboard' page.

### Leaderboard

If the user clicks on this link they will be able to see the usernames and the scores of the previous users. They will be able to search the list and see where they stand. This page also carries a link back to the home page.

## Features

### Form 

When the user clicks on this button they are taken to a page with a form which asks them to provide their first name, last name and a username. This is run through the 'solar-quiz.html' page. When the form is filled out, the first name, last name and the username is stored in the ....'names.json' file.... These are called on later in the following pages.

### Questions

They are then taken to the quiz questions. They will then answer each of the questions. All questions need to answered as the radio buttons are set as 'required'. The quiz pages are implemented through the templates, questions.html, quiz-completed.html and solar-quiz-uesr.html.......

### Quiz completed message

The message is displayed using Python logic in 'run.py', and displayed using the 'quiz-complete.html'. For players that have not scored the result they wanted, there is an option to go to the 'Solar Info Page'.

### Leaderboard

The leaderboard is presented on the 'leaderboard.html' page and its route is /solar_quiz/leaderboard. The leaderboard is there for players that want to see their performance compared to other players.

### Features to Add

.................................

## Technology Used

This project was built using different languages, libraries and frameworks. 

The site has been built using the Python based Flask framework (http://flask.pocoo.org/), and is run from the 'run.py' file. All the pages are routed from here, and contain the logic required for the quiz. Python has been used to create the logic within the 'run.py' file (https://www.python.org/). The 'jinja template engine' (http://jinja.pocoo.org/) has been ued within the templates html pages.

The template pages have been written with HTML5 (http://www.html5.com/) and styled with CSS3 (www.css3.com) in the style.css file. CSS3 was used to create the mobile responsiveness seen across the whole site. It has also been used to create the hover effects for the buttons and the social icons. On each of the pages, you will find the jinja template engine used. A 'base.html' page has been created to contain the HTML code that is to be used on each of the pages i.e. The head, header and the footer.

On the 'Solar Info' page uses jQuery (https://jquery.com/) to reveal the extra information if the user clicks on the 'More Info' button. When one of these buttons is selected, a 'slideToggle' instruction is used. The other solar objects information has a 'slideUp' instruction placed on it meaning that only one object will have its information revealed at any one time. 

The data for the questions asked in the quiz, the information contained on the 'Solar Info' page, and the names gathered in the form when starting the quiz are contained in their own individual json files (https://json.org/). 

Git was used throughout the project for version control. I also used the 'File Revision History' to revert when there was experementation with different design techniques.

## Testing

The site has been tested manually by clicking the links to the pages, and checking all of the jQuery options 








In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Issues While Building the Project

### Data Storage

### Iterating over the Questions



## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

Different values for environment variables (Heroku Config Vars)?
Different configuration files?
Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.

## Credits

### Media

There are several images used throughout the site:
    Fine Art America - oort cloud picture
    MetaBallStudio Youtube Channel - Video comparing Solar System object sizes in Solar Info Page

### Acknowledgements

The basis of the information was taken from various websites and 



