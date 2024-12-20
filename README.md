command:

virtualenv venv

source venv/bin/activate

pip install django

django-admin startproject djangoadminui

cd djangoadminui/

python3 manage.py startapp blog

python3 manage.py startapp comment

after go to the djangoadminui/djangoadminui/settings.py
mentioned installed_app
'blog'
'comment'


python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py startapp adminui



----------------------------------------------------------------------------------------------------


![image](https://github.com/user-attachments/assets/99d82878-86fa-45c2-9242-d41cd860bc6e)


![image](https://github.com/user-attachments/assets/de492972-8408-4645-a909-f231c527bf8b)


![image](https://github.com/user-attachments/assets/a53fba55-8f18-43e7-a05f-4e426a1add00)




