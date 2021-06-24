# Pizza (REST API)

Browsable REST API To do CRUD operations on DB 

## Installation & Setup

*These commands are for windows machine.(Commands for linux and mac machines may differ)*

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/aditya2712/pizza.git
$ cd pizza
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ py -m venv pizza-env
$ .\pizza-env\Scripts\activate.bat
```

Then install the dependencies:

```sh
(pizza-env)$ pip install -r requirements.txt
```

Note the `(pizza-env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv module`.

Once `pip` has finished downloading the dependencies:

```sh
(pizza-env)$ python manage.py runserver
```

And navigate to `http://127.0.0.1:8000/admin`

*You do not need to setup  mongoDB in local machine. This repository already consists of a smaple DB. The sample DB is hosted on Atlas cloud.*

## Endpoints

- Access Admin Dashboard : **`/admin`**
- Add Pizza : **`/pizza/create/`**
- Get All pizzas : **`/pizza/get-all`**
- Get pizza based on filter : **`/pizza/get?type=Regular&size=Jumbo`**
- Delete pizza : **`/pizza/delete/<pk>`**
- Update/Edit Pizza : **`/pizza/update/<pk>`**
- Add Pizza Topping : **`/pizza/topping/create/`**

To access the admin dashboard, either you can create a super user using the command:

```sh
(pizza-env)$ python manage.py createsuperuser
```

*OR*

You can login on admin dashboard using the sample Super User credientials:

```sh
Username: testuser
Email: testuser@gmail.com
Password: asdf@1234
```

## Walkthrough

``To test the API you can either use Browser (This is a browsable API) or Postman``

### Create Pizza

```ssh
POST Request
URL: http://127.0.0.1:8000/pizza/create/
```

If you are using Browser, then a form will appear to create Pizza. You can select Multiple Toppings for a single pizza.

### Create Pizza Toppings

This is used if user wants to create their own Toppings

```ssh
POST Request
URL: http://127.0.0.1:8000/pizza/topping/create/
```

If you are using Browser, then a form will appear to create Pizza Toppings. 

### Get list of all Pizzas in DB

```ssh
GET Request
URL: http://127.0.0.1:8000/pizza/get-all
```

### Get list of Pizzas based on Filter

```ssh
GET Request
URL: http://127.0.0.1:8000/pizza/get?type=regular&size=jumbo
```

User can use either or both filters (type and size). The value of filter is case insensitive i.e.

```url
http://127.0.0.1:8000/pizza/get?type=Regular

http://127.0.0.1:8000/pizza/get?type=regular
```

Both will fetch same results

Avaliable filters:

* type
    * regular
    * square
* size
    * small
    * medium
    * large
    * jumbo


### Delete Pizza

This is used if user wants to delete any pizza

```ssh
DELETE Request
URL: http://127.0.0.1:8000/pizza/delete/<pk>
```
\<pk> is the primary key, replace \<pk> with id of pizza want to delete.

For exaple if you want to delete a pizza with id = 2, use:

`http://127.0.0.1:8000/pizza/delete/2`


### Update/Edit Pizza

This is used if user wants to edit/update any pizza details

*Postman will be a better choice to test this API endpoint*

```ssh
PATCH/PUT Request
URL: http://127.0.0.1:8000/pizza/update/<pk>
```

\<pk> is the primary key, replace \<pk> with id of pizza want to update/edit.

For exaple if you want to edit/update details of pizza with id = 2, use:

`http://127.0.0.1:8000/pizza/update/2`
