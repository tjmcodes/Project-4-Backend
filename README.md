## ![GA](https://cloud.githubusercontent.com/assets/40461/8183776/469f976e-1432-11e5-8199-6ac91363302b.png) General Assembly, Software Engineering Immersive
# Project-4-Backend

### Project Overview 

This two week pair project involved building a full stack web application which allowed both music venues and artists to view the details of the other in order to find acts to perform or venues which were looking for new talent. The back-end of the project was built using Python and Flask and the front-end using react with the styling being done in tailwind CSS with some plain css. The project was created with two user models to enable a tailored experience to each user depending on the type of user they are. The project includes a directory of venues and artists, more detailed information pages for each item in the directory and separate login and registration paths for each user including a typeform style multi page signup form.


### Project Brief

Build a full-stack application by making your own backend and your own front-end
Use a Python Flask API using a Flask REST Framework to serve your data from a Postgres database
Consume your API with a separate front-end built with React
Be a complete product which most likely means multiple relationships and CRUD functionality for at least a couple of models
Implement thoughtful user stories/wireframes that are significant enough to help you know which features are core MVP and which you can cut
Have a visually impressive design to kick your portfolio up a notch and have something to wow future clients & employers. ALLOW time for this.
Be deployed online so it's publicly accessible.

### Technologies used

HTML
CSS
JavaScript
React
Python 
Flask 
Tailwind CSS

### Planning, Whiteboarding and project management

After discussing ideas and settling on a directory for venues and artists we started a more detailed planning process. The first aspect we looked at was what information would be required in our backend models and how these would be structured into tables and what the relationship would be between them. We created a diagram which showed this and that we could refer back to during the project. Due to the large amount of information needed to create a users profile and only a few overlapping fields we decided to create two separate user models to gain more control over our model but also make our tables and Json response easier to work with. 

<img src="screenshots/Screenshot 2022-08-25 at 19.40.34.png" position/></img>
Once we had created the back end we then discussed the user journey and drew the below diagram which outlined the structure of the site and how the user would interact with the different pages as they moved through the site. 

<img src="screenshots/Screenshot 2022-07-28 at 20.24.01.png" position/></img>
Once the user journey had been mapped out we created wireframes in Figma which allowed us to design the site in detail so we could tweak it before coding, this sped up the styling both during the design  process and later in the project as we were writing code which copied the Figma design.
<img src="screenshots/Screenshot 2022-08-25 at 19.39.32.png" position/></img>
To manage the project we used JIRA. We created a JIRA board and broke the project down into epics and then further into stories which we then allocated to one of our two sprints. Throughout the project we used JIRA for assigning tasks, keeping track of progress on the JIRA board, leaving comments on stories with explanations and updates. We had stand up at the beginning of each working day on Zoom to update each other  on the work we had done, things we were struggling with and bugs that had been noticed as well as to plan out the day's work. We stayed in contact on Slack updating each other on work we have been doing. This allowed us to keep track of what was going on, plan our time effectively and support each other. 
<img src="screenshots/Screenshot 2022-08-25 at 19.41.34.png" position/></img>
### Challenge one - Creating the backend 

Due to the complexity of our backend and this also being our first project created in python we decided that we would work together to create the backend so that we both understood how the backend was constructed and that we both got the benefit of applying the knowledge we had learnt in classes. We started by creating our user models. During the planning phase we decided that we would create two separate user models for Venues and Artists. This decision, although the best in terms of organization of stored data did create issues when constructing the backend when the users tried to interact with each other.

This created a significant problem when setting up the backend to allow for comments. For our comments section we wanted to be able to display not just the comment but also information about the user who had posted it eg. username and profile image. To do this we needed to append the relevant user details in the JSON response. To do this we nested the relevant user models inside the comment schema, However this would only work when applied to one of the users as when applied to both of the user models at the same time this created an infinite loop of nested data. 

A second challenge we faced when creating the backend was regarding creating more advanced error handling. During our first sprint we created basic error handling which would display an error if the registration form failed to submit as can be seen in the uncommented section below. During our second sprint we decided that we would like a more advanced form of error handling which would identify individual errors on fields which as per our model needed to be unique eg. username, email, website url.
To do this I researched online regarding error handling in flask by looking both at the flask documentation and other independent online resources. I managed to get custom error handling working which would display errors on the page. This improved the user experience by telling them what specifically was wrong. However I was unable to get multiple errors displaying on the page at one time  which is what we desired for the form review page. Due to the short time left before the project deadline this feature was left out of the final deployed version and was commented out of the controller. If there was longer left on the project then I would have liked to spend more time researching and thinking through the problem to get this feature working.  
``` py
@router.route('/artist-signup', methods=["POST"])
def register():
    artist_dictionary = request.json
    # artistemail = ArtistModel.query.filter_by(email=artist_dictionary["email"])
    # artistusername = ArtistModel.query.filter_by(username=artist_dictionary["username"])
    # if artistemail:
    #     return {"email": "A user has already registed with that email"}
    # if artistusername:
    #     return {"username": "This Username is already taken"}
    
    try:
        artist = artist_schema.load(artist_dictionary)
        artist.save()
        return artist_schema.jsonify(artist)
    except ValidationError as e:
        return {"errors": e.messages, "messages": "Something went wrong validation"} , HTTPStatus.BAD_REQUEST
    except Exception as e:
        print (e)
        return { "messages": "Something went wrong" }, HTTPStatus.BAD_REQUEST

```

### Challenge Two - Signup form

One part of the project that I spent a significant amount of time working on was the signup form. When we planned the project we decided that as the signup form was going to be long we wanted it to be broken up into a more user friendly multi page form which was inspired from the typeform style.

The challenge which this presented was how to create the form that one question would appear at once but also the typed response would be saved and then submitted at the end of the form to create the user. Initially I looked into creating separate react components for each stage of the form which would be rendered when the next step button was clicked. The main advantages of this method was clean and readable code and the ability to reuse components between both user sign up forms. However the major complication in this method was in the storage and passing of form data. With multiple components this could involve passing large amounts of state which would complicate the logic. With a limited time window to work on this project I looked for an alternative.

The way in which I decided to create this was through the use of a single react component which used conditional rendering to show questions depending on the status of state. I firstly created state for each of the questions which I would have with the default state set to false except for the first question
``` js
const [Q1, setQ1] = React.useState(true)
const [Q2, setQ2] = React.useState(false)

```
After creating this state I then created the questions which would be rendered. The questions contained a ternary operator that would check if the state is true and if it was then would display the question on the page if it was not then it would display nothing. To allow the user to control movement through the form I created a next step and back buttons which when clicked would trigger the post function which matched the question number.
``` js
 {Q4 ? <>
        <div className={styles.questionbox}>
          <h3 className={styles.h3}>What is your website address?</h3>
          <div className={styles.titlebanner}>
          </div>
          <input 
            onChange={handleChange} 
            className={styles.textinput} 
            type="text" 
            placeholder="Enter your website address (url)"
            name="websiteUrl" 
            value={formData.websiteUrl}
          />
          {errors.websiteUrl && <small className="errors">{errors.websiteUrl}</small>}
          <button onClick={postQ4} className={styles.nextbutton}>Next Step</button>
          <button onClick={postQ4} className={styles.backbutton} value='back'><i className="fa-solid fa-arrow-left-long"></i> Previous step</button>
        </div></> : null }

```

The post function firstly set the state of the question to false which causes the question to disappear from the screen as per the ternary operator above if the state is false nothing is displayed. The function then uses if statements to determine which screen to render next. If the value of the button is “back” then the function will set the previous questions state to true and therefore render this on the page. If not then it will set the next question to true and display this. In this form I also included a progress bar which gets filled in as the user proceeds through the form. This function also assigns a new value to that progress bar dependent upon which button is clicked.
``` js
 function postQ4(event) {
    setQ4(false)
    if (event.target.value === 'back') {
      setQ3(true)
      progressBar.value = 30
    } else {
      setQ5(true)
      progressBar.value = 40
    }
  }

```

There Is one weakness in the code which is written. The weakness is that it is very repetitive as each question has its own state and its own post function. This makes the code difficult to navigate and makes it harder to maintain as amending one item would require the modification of all post functions and states. Due to the limited time available on this project I did not have the opportunity to refactor this code to find a more succinct way of writing this. However If I had the chance i would have liked to work on creating a single function which would be able to render the questions making the code easier to read and easier to maintain.

### Screenshots
<img src="screenshots/Screenshot 2022-08-12 at 17.45.27.png" position/></img>
<img src="screenshots/Screenshot 2022-08-25 at 19.43.25.png" position/></img>
<img src="screenshots/Screenshot 2022-08-25 at 19.43.08.png" position/></img>
<img src="screenshots/Screenshot 2022-08-10 at 23.29.37.png" position/></img>


### Wins 

We were able to create a website within the timeframe which was functional and met our MVP goals, the site included a slick UI which matched or improved upon our initial figma wireframe designs. 
We were able to create the multi page sign up form and get this working reliably.
We managed to overcome our initial struggles with the backend and the two user model to get trickier features such as the nested comments to work as required. 
Lessons Learnt 

When using frameworks or libraries to understand and account for the possibility they may act differently when deployed in the case of this project the Tailwind styling did not look the same in the deployed version as the localhost version and time was needed to fix this which was not available at the end of the project.
Ensure that testing is done incrementally and not left till the end of the feature. This would have made debugginging easier and quicker as it would have been easier to see exactly what was breaking the feature rather than searching through a number of changes to see where the error was. 

### Known Bugs

On both sign up forms if no data is entered on the first question then the progress bar does not move on all other pages it moves regardless however not on this page.
Submitting the form to register does not always submit if a field is not valid and no error is displayed on the page error handling is needed to ensure that the user knows that something is wrong and the form was not submitted successfully

Possible future developments 
Refactor the code on the signup form to create one function which handles rendering making it easier to read and maintain.
Create a contact button on the individual venue/artist page which allows the user to send a message to the other user which the user would be able to view when they logged in to their account 
Advanced error handling on the signup form that displays all errors at once to allow the user to go back and change all invalid fields. 
Edit button on form review screen so users could edit invalid fields without having to go back through the form which is time consuming.

### Created with 

Teresa Morini -- https://github.com/tjmcodes


