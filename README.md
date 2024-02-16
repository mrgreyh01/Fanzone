# Fanzone ![fanzone favicon](./frontend/public/favicon-16x16.png)

![fanzone logo](./frontend/src/assets/logo.png)

### A social media site for football fans

---

### The goal with Fanzone

The goal with Fanzone was to create a simple social media site with the usual
post, comment and like functions but with the twist of being able to support a
specific team to also see a feed with only posts about that certain team.

### Click here to view [Fanzone](https://fanzone-ceb2b022a19f.herokuapp.com/)

---

## Table of contents

1. Project Overview<br/>
   1.1 Structural Planning<br/>
   1.2 Design Ideas<br/>
2. Front-End Documentation<br/>
   2.1 Design Process: UX Desing, mockups and design diagrams<br/>
   2.2 Security Practices: security secret keys etc <br/>
   2.3 Component Usage: use of React components, architecture and component composition<br/>
   2.4 Deployment: How to deploy the Front-End<br/>
   2.5 Coding Standards: JSX, modular component use<br/>
3. Back-End Documentation<br/>
   3.1 API Overview: description of API, functionality and how it integrates with the Front-End<br/>
   3.2 Security Practices: security measures (handling of sensitive data)<br/>
   3.3 Database Design: Structure of database, incl. custom models used<br/>
   3.4 Deployment: How to deploy Back-End<br/>
   3.5 Coding Standards: Python coding standars, adhering to PEP8 guidelines<br/>
4. Testing and Version Control<br/>
   4.1 Manual Testing: testing procedures and results for Front End and Back-End<br/>
   4.2 Version Control: Usage of Git and Githug for version control, incl explanation of commit messages<br/>
   4.3 Remaining errors after testing<br/>
   4.4 Other issues
5. Agile Project Management<br/>
   5.1 User Stories - Front-End
   5.2 User Stories - Back-End
   5.3 Agile Practices - Explanation of other Agile Methodology used
6. Additional Information<br/>
   6.1 Connecting via the terminal
   6.2 Front-End libraries: Justification for the choice of libraries used during the project<br/>
   6.3 Credits: Tutorials or articles used while developing<br/>
   6.4 License: Add info about software license if needed<br/>
   6.5 Thanks: add thanks to individuals who have helped or guided during the project<br/>


---

## 1. Project Overview

### 1.1 Structural Planning

The aim of the website was to use a standard modern design using icon to
simplify and with as few pages as possible.
Users can perform the CRUD functions of create, read, update and delete in many
parts of the website.

### 1.2 Design ideas

Initial deas for layout and app title

![Screenshot](static/readme-images/layout_ideas.jpg "Flowchart detailing the pages linked in the fanzone app")

---

## 2. Front-End Documentation

### 2.1 Design Process

**Data Model**

I started from a few drawings of a flowchart and by using the free flowchart
maker from the website [Canva](https://www.canva.com/online-whiteboard/flowcharts/)
the design was set.

![Screenshot](static/readme-images/fanzone-flowchart.png "sketches of main page layout and app name ideas")

**Font and colour schemes**

**Font**

My two main choices of font were:

The Oxygen Mono

![Screenshot](static/readme-images/font-oxygen-mono.jpg "Example text in Oxygen Mono font")

and the Open Sans fonts

![Screenshot](static/readme-images/font-open-sans.jpg "Example text in Open Sans font")

I chose the Oxygen Mono font as I felt it was simple and clean but a little
relaxed at the same time.

Throughout the app I have used Oxygen Mono as the chosen font and have the
sans-serif as the default backup font.

**Colour**

I chose the colour green as the dominant colour to represent the colour of grass
and so to feel like the background was similar to a football pitch.

There were a few other colours involved during the planning process.

On deciding on the colour green I then chose between a few shades of green.

![Screenshot](static/readme-images/4fb076.jpg "colour wheel with the color #4fb076")

![Screenshot](static/readme-images/4ff10e.jpg "Colour wheel with the color #4ff10")

I chose this shade of green felt energetic. #B5E61D

![Screenshot](static/readme-images/b5e61d.jpg "Colour wheel with the color #b5e61d")

**Logos, Icons and images**

**Fanzone Logo designed in Microsoft Paint**

![Screenshot](static/readme-images/logo.jpg "fanzone logo")

The Favicon logo was designed by myself using Microsoft Paint and using a
ball image shrunk down.

I wanted to keep the theme of green and thought the brighter green was energetic
and I felt the logo was more appealing with white text as opposed to black text.

**Fanzone Favicon**

![Screenshot](static/readme-images/favicon-16x16.png "fanzone favicon")

The Favicon was created using [favicon generator](https://favicon.io/favicon-generator/)

The green is the same used in the logo and also with white text.

**FontAwesome Icons used as links**

| Linked command |                                          Icon                                          |
| -------------: | :------------------------------------------------------------------------------------: |
|       **Home** |      ![Screenshot](static/readme-images/house-solid.svg "fontAwesome house icon")      |
|    **Sign Up** |  ![Screenshot](static/readme-images/user-plus-solid.svg "fontAwesome user plus icon")  |
|    **Sign In** |  ![Screenshot](static/readme-images/sign-in-alt-solid.svg "fontAwesome sign in icon")  |
|   **Add Post** |    ![Screenshot](static/readme-images/user-plus-solid.svg "fontAwesome plus icon")     |
|  **Supported** |      ![Screenshot](static/readme-images/heart-solid.svg "fontAwesome heart icon")      |
|      **Likes** |      ![Screenshot](static/readme-images/futbol-solid.svg "fontAwesome ball icon")      |
|   **Sign Out** | ![Screenshot](static/readme-images/sign-out-alt-solid.svg "fontAwesome sign out icon") |

**Other FontAwesome icons**

|      Linked command |                                        Icon                                        |
| ------------------: | :--------------------------------------------------------------------------------: |
|        **Comments** | ![Screenshot](static/readme-images/comments-solid.svg "fontAwesome comments icon") |
|            **Edit** |     ![Screenshot](static/readme-images/edit-solid.svg "fontAwesome edit icon")     |
| **Change username** |  ![Screenshot](static/readme-images/id-card-solid.svg "fontAwesome id card icon")  |
| **Change password** |      ![Screenshot](static/readme-images/key-solid.svg "fontAwesome key icon")      |
|          **Search** |   ![Screenshot](static/readme-images/search-solid.svg "fontAwesome search icon")   |

#### 2.2 Security Practices: security secret keys etc



#### 2.3 Component Usage: use of React components, architecture and component composition

#### 2.4 Deployment: How to deploy the Front-End

**Steps to deploy in Github**

To deploy in Github, you'll need to do the following things once logged in:

- Create a repository
- Click on Settings
- Click on Pages

![Screenshot](static/readme-images/github_deployment_one.jpg "Github deployment ettings and pages")

- Under Source, select "Deploy from a branch"

![Screenshot](static/readme-images/github_deployment_two.jpg "Choose branch")

- Under Branch, make sure your branch is set to "main" and then that the "/(root)" is selected
- Save

**Steps to deploy in Heroku**

To deploy in Heroku, you'll need to do the following things once logged in:

- Click on the "New" icon on the right-hand side of the page
- Choose "Create new app"

![Screenshot](static/readme-images/heroku_deploy_one.jpg "Heroku create new app")

- Enter a name for your app
- Choose your region (USA or Europe)
- Click on "Create app"

![Screenshot](static/readme-images/heroku_deploy_two.jpg "Heroku enter app name")

- Click to go to Settings
- Click to open the Config Vars

![Screenshot](static/readme-images/heroku_deploy_three.jpg "Github deployment ettings and pages")

  Add your specific config vars here:

- ALLOWED_HOST
- CLIENT_ORIGIN
- CLOUDINARY_URL
- DATABASE_URL
- DEBUG (only used during development)
- DISABLE_COLLECTSTAIC (only used during development)
- POSTRESQL_DB
- POSTGRESQL_ENGINE
- SECRET_KEY

![Screenshot](static/readme-images/heroku_deploy_four.jpg "Github deployment settings and pages")

The final part to the deployment is to connect your Heroku app to Github:

- Click on the Deploy tab
- Select the "Deploy to Github" option in the middle
- Make sure it is connected as shown in this final image

![Screenshot](static/readme-images/heroku_deployment_final.jpg "deployed")

Further information can be found on the Heroku site [here](https://devcenter.heroku.com/articles/git)

#### 2.5 Coding Standards: JSX, modular component use

**What is JSX?**

The website [geeksforgeeks.org]('https://www.geeksforgeeks.org/reactjs-jsx-introduction/') describes JSX as the following:</br>
"React JS JSX is a syntax extension of JavaScript for writing React Code in a simple way. Using JSX it is easier to create reusable UI components with fewer lines of code in a template-type language with the power of JavaScript."

**Examples of JSX in Fanzone**



---

## 3. Back-End Documentation

#### 3.1 API Overview: description of API, functionality and how it integrates with the Front-End

#### 3.2 Security Practices: security measures (handling of sensitive data)

To protect sensitive information, such as secret keys, an env.py file was created and this held sensitive information connected to the settings file using os.environ:

![Screenshot](static/readme-images/os_path.jpg "settings code that imports os")

![Screenshot](static/readme-images/secret_key.jpg "settings code for secret key")

In env.py:

![Screenshot](static/readme-images/env.jpg "a redacted version of the env.py file")

#### 3.3 Database Design: Structure of database, incl. custom models used

#### 3.4 Deployment: How to deploy Back-End

**Steps to deploy in Github**

This is identical to the Front-End deployment, except the title of the repository should be similar to the Front-End title but include "drf" in the title. For example, "project" = Front-End and "drf-project" for Back-End.

**Cloudinary**

Create an account and then click on "Dashboard" to access the following page:

![Screenshot](static/readme-images/cloudinary_one.jpg "cloudinary dashboard that contains important information")

Your API env variable will be important to add to your Heroku config vars and your env file. Then click "Media Library" to go to the images.

In the Media Library there are the following links:

- "Home": Your start page
- "Assets": Contains all uploaded images
- "Folders": Contains uploaded images sorted into folders

![Screenshot](static/readme-images/cloudinary_two.jpg "cloudinary dashboard that contains important information")

**DRF - Django Rest Framework**

To initiate the DRF, in the python terminal, enter:

```
pip3 install 'django<4'
```

Then to start your project (if your project was named "Fanzone" for example), enter:

```
django-admin startproject drf-fanzone
```

Then to connect your project to Cloudinary, you'll need to enter:

```
pip install django-cloudinary-storage
```

Then to enable a library that provides image processing in the project, "Pillow" needs to be added:

```
pip install Pillow
```

**ElephantSQL creation**

Once you have logged in, the following steps need to be taken:
- Create a "new instance"
- Name the instance after your drf prject name (e.g. drf-fanzone)
- Keep to the Tiny Turtle (free) plan
- Select Europe as your region, if you are in Europe
- Click "Create ElephantSQL" to create your instance
- Once created, you will get a connection string. This string should be added to both your Heroku config vars and your env.py file

Link to the creation of the ElephantSQL database can be found [here](https://www.elephantsql.com/docs/index.html)

##### 3.5 Coding Standards: Python coding standards, adhering to PEP8 guidelines

---

## 4. Testing and Version Control

#### 4.1 Manual Testing: testing procedures and results for Front End and Back-End

#### 4.2 Version Control: Usage of Git and Githug for version control, incl explanation of commit messages

#### 4.3 Remaining errors after testing

#### 4.4 Other issues

---

## 5. Agile Project Management

#### 5.1 User Stories - Front-End

![Screenshot](static/readme-images/user_stories_front.jpg "list of front-end user stories")

#### 5.2 User Stories - Back-End

![Screenshot](static/readme-images/user_stories_back.jpg "list of back-end user stories")

#### 5.3 Agile Practices - Explanation of other Agile Methodology used

Github "Milestones

![Screenshot](static/readme-images/milestones.jpg "list of milestone groups")

---

## 6. Additional Information

#### 6.1 Connecting via the terminal

Starting the app required two terminals open (I chose a split terminal)

1. Starting Django from the backend
2. Starting React js from the frontend.

To start the app, I started with these codes in terminal 1:

First the Back-End in terminal 1:

```
python manage.py runserver
```

Then the Front-End in terminal 2:

Change directory to Fanzone/frontend

```
cd frontend
```

Then to start React and open the webpage in a browser:

```
npm start
```

The website was then run using Port: 3000 which is the connected to the
frontend. While I could connect to the DRF part of the API by using Port: 8000

#### 6.2 Front-End libraries: Justification for the choice of libraries used during the project

#### 6.3 Credits: Tutorials or articles used while developing

The following sources have been used to provide either a direct influence or
as a source of inspiration:

- The lessons, tutorials and course literature of Code Institute's Advanced
  Front End section, particularly including the 'Moments' and Django REST
  Framework modules.

- [Guide for models for Supported posts](https://docs.djangoproject.com/en/5.0/ref/models/fields/)

#### 6.4 License: Add info about software license if needed

Thanks to the following image creators for their free images:

From pixabay.com:

- jplenio
- Pexels
- Bessi
- artsysolomon
- Leroy_Skalstad
- Engin_Akyurt
- planet_fox
- 134213
- Ralphs_Fotos
- qimono
- Mohamed_hassan
- StartupStockPhotos

From freepix.com:

- master1305
- Freepik
- rawpixel.com

#### 6.5 Thanks: add thanks to individuals who have helped or guided during the project

The following sources have been directly involved in helping to solve problems
issues with the development of Fanzone:

- Tutor Support provided by Code Institute
- My Mentor Akshat Garg
- Slack, the business messaging app, and its users, for help with issues
  including lines too long errors and cookie refresh errors
- Keith Herne
- Abhi Shek

---

## 4. Installation

#### Dependencies

Frontend

```
npm install
ES7 React/Redux/GraphQl/React-Native - (snippets) by dsznajder
npm install react-bootstrap@1.6.3 bootstrap@4.6.0
npm install axios
npm install react_infinite-scroll-component
npm install msw –save-dev (for mock API for testing)
npm install jwt-decode (to decode json webtokens)
```

Backend

```
pip3 install 'django<4'
django-admin startproject drf_fanzone .
pip install django-cloudinary-storage
Pip install Pillow
Pip install djangorestframework
Pip install django-filter
pip3 install dj-rest-auth==2.1.9 (For JSON web tokens)
pip install ‘dj-rest-auth[with_social]’
pip install djangorestframework-simplejwt
pip3 install dj_database_url==0.5.0 psycopg2
pip3 install gunicorn django-cors-headers
```

---

## 5. Usage

#### Test Profiles

**Admin**

- admin / admin12345
- TestUser1 - TestPassword1

**Users**

- Alan / AlanPassword
- Phil / PhilPassword
- TaraTaylor / TaraPassword1
- Sam / SamPassword
- Sally / SallyPassword

---

## 6. Testing Issues

There was an issue with the backend at one point and so there were parts of the
testing which remain incomplete. I also had to restart my workspace the day
before submission which helped to create some gremlins in the system.

Backend tests that were run include:

- Tests can list posts
- Test if user can create a post
- Test if pages can be accessed when logged out
- Test if user can see a post using post id
- Test if user can see a post with an invalid id
- User can see own posts
- User cannot update a post that isn't their own

---

## Problems and incompletions

#### Problems

The website is slow and there are many styling issues. The website is has not
been checked using lighthouse, for its code or its layout.

#### Incompletions

There is a major part of this website that isn't complete.
The supported teams function is not complete and is only partially complete in
the code.

The README.md file is not complete and lacks extensive information on testing,
website layout and descriptions, as well as how the website operates.

---

## 8. Credits, Help and Copyright

### Copyright

---

Problems 6/2
Bad Request: /api/dj-rest-auth/login/
[06/Feb/2024 14:46:10] "POST /api/dj-rest-auth/login/ HTTP/1.1" 400 68
[solution](https://stackoverflow.com/questions/62592113/fetching-user-details-in-react-from-django-rest-auth-gives-back-403-forbidden)
