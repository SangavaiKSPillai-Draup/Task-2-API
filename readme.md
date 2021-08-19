# Task - 2

Developing the backend for a Mobile Store, and the corresponding CRUD API's. 
The APIs are tested with POSTMAN.

There are various folders in this project:

1. configuration - This initializes the database and mail with the app. (config.py)
2. controllers - This contains the set of code that interacts with the database (stores, retrieves, updates, deletes data. File - controller.py). It also contains the definition of a decorator (role_decorator.py) that identifies the role of a user, and then decides if the user can send a post request or not. 
3. Models - Defines the structure of the data stored in the database (model.py). It also contains the class definitions of user - defined exceptions (CustomErrors.py).
4. Resources - Stores the API endpoints (routes.py), as well as code to authenticate (login and sign up) into the application (auth.py).

To run the project:

1. Download all the files and folders, and place them in the same directory.
2. Install python3 and pip (I used python 3.9.4 with pip 21.2.4).

3. Install all the requirements present in requirements.txt by the command:

    
    $ pip install -r requirements.txt

4. Create a connection in mongodb, with a new database.
5. Add three collections: Smartphone, Customer, Orders ; according to the schema given in Models/model.py. Populate them with documents.
6. Create a .env file, that stores values for the following parameters:
   1. JWT_SECRET_KEY (The value of this can be anything, but ensure it's hard to guess. Preferably an uuid (without any hyphens in between))
   2. MAIL_SERVER (smtp.gmail.com, in my case)
   3. MAIL_PORT (465, in my case)
   4. MAIL_USERNAME (a gmail id, if you are using gmail server)
   5. MAIL_PASSWORD (the password for the corresponding mail id)
   6. MAIL_USE_TLS (False)
   7. MAIL_USE_SSL (True)
      
     Ensure that the gmail id used does not have two - step verification enabled.
     You'll have to configure the account to allow access from less secure apps. Refer these links in case of any hiccups with email:
   8. https://stackoverflow.com/questions/18881929/flask-mail-gmail-connection-refused 
   9. https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp
   10. MONGODB_SETTINGS: This value should be set in the following format:
      
       {'host':'your_mongodb_connection_string'}

7. In the post request under OrdersApi, modify the sender's email address. It should be the same as MAIL_USERNAME in the .env file. 
The recipient should also be a valid email address.
8. Execute the command:


    $ flask run

to run the application.
9. To test these API endpoints, you'll need to make use of POSTMAN.
10. While giving a post request, in POSTMAN, ensure you do the following:
    1. Go to the Authorization tab.
    2. Select Auth type as Bearer token.
    3. Paste the token. You'll get this token when you sign up into the application for the first time. This token will expire after 7 days.
