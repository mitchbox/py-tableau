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


### Python Development Environment Setup

* [Python Development Env](https://medium.com/@mitchbox/python-%E9%96%8B%E7%99%BC%E7%92%B0%E5%A2%83%E8%A8%AD%E5%AE%9A-9a7acbd1cf33#.ca9kjpqb8)


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

    * After modified, remember to restart virtual env


### Run Server

```
python manage.py runserver --host 0.0.0.0
```


### REST API

  * Get Ticket for Display Tableau View

  ```
  GET http://<your-ip>/tableau/ticket
  ```

    Request Header

    ```
  Username: 'tableau-server-username'
    ```

    Response Body

    ```
  {
    'ticket': your-ticket-from-tableau
  }
    ```

  * Tableau REST API Proxy

  ```
  GET/POST http://<your-ip>/tableau/<tableau-rest-api-uri>
  ```

    **Example:**

    Tableau Server API - Sign In

    ```
  POST /api/<api-version>/auth/signin
    ```

    Proxy Usage Method

    ```
  POST http://<your-ip>/tableau/api/<api-version>/auth/signin
    ```
