# DRF
Follow bellow steps. 
1. This App provides minimum functionalities to run server.
2. Create a Directory with specific name.
3. Clone this app with whatever the branch you needed [git clone -b DRF_ready_to_start git@github.com:sanjaygd/DjangoBase.git] 
4. Go inside DjangoBase copy all files and folders. Come out of DjangoBase directory paste them and delete .git and DjangoBase folders.
5. Create new repository in gitHub with same name as you created Folder name in local 
6. Add origin [git remote add origin <repo.git>]
7. Remove all text inside README.md file add whatever you want to add.
8. Stage the changes [git add .]
9. Commit all the changes [git commit -m "initial commit"]
10. Create a relevent branch (here creating main branch since gitHub is having main branch by default) [git branch -M main]
11. Push the changes to remote [git push -u origin main]
12. Create virtual environment in root directory(where manage.py and settings folder placed) [python -m venv venv]
13. Intall dependencies [pip install -r .\requirements\base.txt]
14. Add .env file in root directory.
15. Run migrations [ python manage.py migrate]
16. Create super user [python manage.py createsuperuser]
17. Run development server. [python manage.py runserver]
18. Open postman run this post request with super user credential endpoint [http://127.0.0.1:8000/accounts/token/] you will get 200 status response with refresh token and access token
19. Copy access token and open new tab in postman run this get request [http://127.0.0.1:8000/accounts/users/] with Autherization's bearer token as access token. it will list all the users.

<!-- Optional use case -->
20. Changing environemnt - go to .env file and modify ENV attribute
21. creating new App
    1. Go to apps directory create folder in the name application
    2. Run this command [python manage.py startapp expirement src/apps/expirement](python manage.py startapp <app_name> <distination_folder>)
    3. Register app in setting's installed app
    4. Go to apps.py of newly created app and change the name as 'src.apps.<app_name>'
    5. Run development server.


This is the app with below features
1. Custom user model
2. DRF with JWT authentication (don't forget to add auth_medel in settings)
3. Added api for listing users with admin-only permission for POC
4. Having jwt login(account/token), register features.
5. Refer this link for production ready django app.
    https://simpleisbetterthancomplex.com/tutorial/2021/06/27/how-to-start-a-production-ready-django-project.html

