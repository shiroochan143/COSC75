# ADD2KART
An online shopping experience made using Django for COSC75 requirements.

# Contributing
To setup the ADD2KART project, here is the following guidelines:
* Clone the repository <code>git clone https://github.com/thisishaykins/PyShop.git</code>
* Open Project folder on terminal 
* Prepare your virtual environment <code>python3 -m venv venv</code>
* Activate your virtual environment:
* For WinOS: <code>source venv/Scripts/activate</code>
* For MacOs: <code>source venv/bin/Activate</code>
* Alternatively, you can deactivate virtual env by typing <code>deactivate</code> in the terminal
* Install your requirements.txt file <code>pip install -r requirements.txt</code>
* Create migrations using <code>python3 manage.py makemigrations</code> 
* Run migrations <code>python3 manage.py migrate</code>
* Start your dev server with <code>python3 manage.py runserver</code>
* Visit your App using <code>http://127.0.0.1:8000/</code>
* Create super user to access admin dashboard using <code> python3 manage.py createsuperuser</code>
* Follow the prompts after <code>Username: , Email address: , Password: , Password (again): </code>
* Visit Admin Page using <code>http://127.0.0.1:8000/admin</code> and login with the credentials created above.
* Add Products under the <b>Products</b> Menu, Add Offers also.
* Visit Products Page using <code>http://127.0.0.1:8000/products/</code>
* Visit New Arrival (Products) Page using <code>http://127.0.0.1:8000/products/new</code>

> Special Thanks to project template owner, [Shaykins' PyShop](https://github.com/thisishaykins/PyShop). Modified and revised for specific requirements based on our SDLC model and in no collaboration with the template owner.