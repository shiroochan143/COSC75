# COSC75 WEB DEVELOPMENT
A group project intended for system evaluation. Developed by CS3B B2023-2024 for COSC75 requirement. Purposely academic.


# Get Started
__To setup locally, follow these guidelines:__
* Clone the repository <code>git clone https://github.com/thisishaykins/PyShop.git</code>
* Open Project folder on terminal 
* Prepare your virtual environment <code>python3 -m venv venv</code> 
* Activate your virtual environment > Windows: <code>source venv/Scripts/activate</code> | MacOS : <code>source venv/bin/activate</code>
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



> Project fork from [Akinshola Samuel AKINDE's PyShop](https://github.com/thisishaykins/PyShop?fbclid=IwAR2gI0fokCIaXavmbhuHQK9RJ9RX1tAvfLN3k7f2L1j88Fr3DbvIwViI0bE). Usin the project as a template and a starting gound while building toward our main requirements.
