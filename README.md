# Portfolio website
_This is a my portfolio website. With static and dinamic content_
![](img-readme/home.png)
![](img-readme/contact.png)

## Built with🛠️
* [Django](https://www.djangoproject.com/) For the backend
* [Bootstrap](https://getbootstrap.com/) For the frontend

## Instructions📋:
_How to get a copy of the project running on your local machine_
<strong>1.Clone the repository</strong>
```
git clone https://github.com/santiudev/myportfolio
```
<strong>2.Create a virtual environment</strong>
_From the cloned directory run:_
```
python -m venv env
```
<strong>3.Activate the virtualenv</strong>
On macOs or Linux:
```
source venv/bin/activate
```
On Windows:
```
env\scripts\activate
```
<strong>3.Install required requirements</strong>
```
pip install -r requirements.txt
```
<strong>4.Run migrations</strong>
```
python manage.py makemigrations
```
```
python manage.py migrate
```
<strong>5.Create an admin User</strong>
```
python manage.py createsuperuser
```
<strong>5.Run the application</strong>
```
python manage.py runserver
```
