Py-Tableau
===========

A simple proxy for Tableau Server REST API that implement with Python, Flask, Flask-RESTful and Rquests.


### Stack

* [Flask](http://flask.pocoo.org/)
* [Flask-RESTful](http://flask-restful-cn.readthedocs.io/en/0.3.4/)
* [Requests](http://docs.python-requests.org/en/master/)
* [Tableau Server](http://www.tableau.com/products/server)
* [Tableau Server REST API](https://community.tableau.com/community/developers/rest-api)


### Tableau Server Setup

* [Trusted Authentication Setup](http://onlinehelp.tableau.com/current/server/en-us/help.htm#trusted_auth.htm%3FTocPath%3DAdministrator%2520Guide%7CTrusted%2520Authentication%7C_____0)


### Environment Setup

  * Using **pip** install required packages

  ```
  pip install -r requirements.txt
  ```

  * Config Setup

    * Open terminal, edit postactivate (work on virtual env)
    
    ```
    vi $VIRTUAL_ENV/bin/postactivate
    ```

    * Add environment variable (press "i" to insert)

    ```
    export APP_SETTINGS=“config.DevelopmentConfig"
    ```

    * Save file (press ":wq" to exit)


### Run Server

```
python manage.py runserver --host 0.0.0.0
```


### REST API

  * Get Ticket for Display Tableau View

  ```
  GET http://<your-ip>/tableau/ticket
  ```

  * Response Body

  ```
  {
    'ticket': your-ticket-from-tableau
  }
  ```
