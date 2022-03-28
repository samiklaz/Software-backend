## Software Engineering Exercise

This is the instruction for running the project

* Turn on your Computer System and connect to an Internet Connection
* Open Docker Desktop in your Comnputer System
* Open your Terminal
* Move to your workspace directory
* Clone the repository with command git clone https://github.com/samiklaz/Software-backend.git
* Navigate into the project with command cd Software-backend 
* Build the Dockerized Django Project with command docker-compose build
* Run the Dockerized Django Project with command docker-compose up
* Open this URL with your browser http://127.0.0.1:8000/<str:country>/


The SPA application is on repository https://github.com/samiklaz/software-frontend.git


## THE ACHITECTURAL DECISION
The Project was built on Django and Django Rest Framework which was the project requirement. This follows the MVC Software achitecture which is considered to be MVT in Django.
Since we are supposed to consume an API and return the response, we used the REQUESTS Django Library to fetch the API from the endpoint, we persisted it using our SQLite database and return the JSON response with the help of Django Rest Framework.
This response was consumed by our SPA Application







