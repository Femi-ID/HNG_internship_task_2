# **Documentation on the HNG Task 2 CRUD Application**

## Standard Request Formats for the Endpoints

#### The API has **3** endpoints you can check out in the views.py:
1. **/:**  The home view to see all user profiles.

2. **/api:**  To create a new profile. A form will be displayed to create one.

3. **/api/user_id:**  To view details of the user profile. This is where you can READ, DELETE and UPDATE profile details.
    The user_id should be an integer, any other variable type will **not be accepted**. It is the id of the user.

### Example:
A user with the id=3, would view his/her profile by hitting the endpoint: ```domain.com/api/3```.
Then such user can **read, edit** and **delete** his/her profile.
To delete user profile,check the boolean field and then hit the delete button.

## Error Handling
The common errors that are customised in this application: 400, 401, 403, 404, 405 and 500.
They return a html page with a brief explanation of what went wrong.

## Limitations/ Assumptions

The create user endpoint does not login the user. This means the user data is not passed to the request session.
The application only emphasis on basic **CRUD** functionalities.

### Deploying your application 

##### Locally:
* Add your app to the list of installed apps in your settings. In this format: 
```my_app.apps.MyAppConfig```
* Still in your settings; Add your template directory for django to find your error html files. Only do this if you've made changes to the current setup.
```TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates/errors')```
* You can set _Debug = False_ to test the custom error handling.


##### Server:
* Set Debug = False
* Include your domain name in the allowed hosts list.

**Check the [README](https://github.com/Femi-ID/HNG_Internship_task_2) for more info on running the server locally.**
#### _And your good to go!_
