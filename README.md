# ToDo Application - REST API Documentation

This is the documentation of REST APIs for a Task Manager Application.

The entire application is built using Django Framework.

Please follow the below steps in windows terminal for running the application.

## Clone repository

    git clone https://github.com/sunilthapa1993/josh_talks_task.git

## Change to project directory

    cd josh_talks_task

## Run migrations

    python manage.py migrate

## Run server

    python manage.py runserver

Open chrome and enter below URL to access the API endpoints: 

    http://127.0.0.1:8000/api/

The REST API endpoints to the application is described below.

## Create Token

### Request

`POST /tasks/`

    curl --location 'http://127.0.0.1:8000/api-token-auth/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "username": "adminUser",
        "password": "Random@123"
    }'

### Response

    HTTP/1.1 200 OK
    Date: Mon, 24 Mar 2025 15:37:35 GMT
    Server: WSGIServer/0.2 CPython/3.12.6
    Content-Type: application/json
    Allow: POST, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 52
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Cross-Origin-Opener-Policy: same-origin
     
    {"token":"592afdbdb8964cee85defb606dd6d6d77ef3288b"}

## Create a new Task

### Request

`POST /tasks/`

    curl --location 'http://127.0.0.1:8000/api/tasks/' \
    --header 'Authorization: Token 592afdbdb8964cee85defb606dd6d6d77ef3288b' \
    --header 'Content-Type: application/json' \
    --data '{
        "name": "Complete assigment",
        "description": "Complete assigment from vendor",
        "task_type": "Professional",
        "status": "Pending"
    }'

### Response

    HTTP/1.1 201 Created
    Date: Mon, 24 Mar 2025 15:32:05 GMT
    Server: WSGIServer/0.2 CPython/3.12.6
    Content-Type: application/json
    Vary: Accept
    Allow: GET, POST, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 172
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Cross-Origin-Opener-Policy: same-origin
     
    {"id":4,"name":"Complete assigment","description":"Complete assigment from vendor","created_at":"2025-03-24T15:32:05.262259Z","task_type":"Professional","status":"Pending"}

## Get list of Tasks

### Request

`GET /tasks/`

    curl --location 'http://127.0.0.1:8000/api/tasks/' \
    --header 'Authorization: Token 592afdbdb8964cee85defb606dd6d6d77ef3288b'

### Response

    HTTP/1.1 200 OK
    Date: Mon, 24 Mar 2025 16:00:54 GMT
    Server: WSGIServer/0.2 CPython/3.12.6
    Content-Type: application/json
    Vary: Accept
    Allow: GET, POST, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 680
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Cross-Origin-Opener-Policy: same-origin
     
    [{"id":1,"name":"Order Shoes","description":"But new shoes from Amazon","created_at":"2025-03-24T13:19:04.927681Z","task_type":"Personal","status":"Pending","users":[1]},{"id":2,"name":"Order Clothes","description":"But new clothes from Amazon","created_at":"2025-03-24T13:35:32.670303Z","task_type":"Personal","status":"Pending","users":[]},{"id":3,"name":"Get Milk","description":"buy milk from shop","created_at":"2025-03-24T15:27:06.109299Z","task_type":"Home","status":"Pending","users":[]},{"id":4,"name":"Complete assigment","description":"Complete assigment from vendor","created_at":"2025-03-24T15:32:05.262259Z","task_type":"Professional","status":"Pending","users":[]}]

## Get task by ID

### Request

`GET /tasks/:id`

    curl --location 'http://127.0.0.1:8000/api/tasks/1/' \
    --header 'Authorization: Token 592afdbdb8964cee85defb606dd6d6d77ef3288b'

### Response

    HTTP/1.1 200 OK
    Date: Mon, 24 Mar 2025 16:02:19 GMT
    Server: WSGIServer/0.2 CPython/3.12.6
    Content-Type: application/json
    Vary: Accept
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 168
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Cross-Origin-Opener-Policy: same-origin
     
    {"id":1,"name":"Order Shoes","description":"But new shoes from Amazon","created_at":"2025-03-24T13:19:04.927681Z","task_type":"Personal","status":"Pending","users":[1]}

## Create a new User

### Request

`POST /users/`

    curl --location 'http://127.0.0.1:8000/api/users/' \
    --header 'Authorization: Token 592afdbdb8964cee85defb606dd6d6d77ef3288b' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "name": "Sample User 2",
        "email": "sampleuser2@yopmail.com",
        "mobile": "9870104590"
    }'

### Response

    HTTP/1.1 201 Created
    Date: Mon, 24 Mar 2025 15:39:57 GMT
    Server: WSGIServer/0.2 CPython/3.12.6
    Content-Type: application/json
    Vary: Accept
    Allow: GET, POST, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 98
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Cross-Origin-Opener-Policy: same-origin
     
    {"id":2,"name":"Sample User 2","email":"sampleuser2@yopmail.com","mobile":"9870104590","tasks":[]}

## Get list of Users

### Request

`GET /users/`

    curl --location 'http://127.0.0.1:8000/api/users/' \
    --header 'Authorization: Token 592afdbdb8964cee85defb606dd6d6d77ef3288b'

### Response

    HTTP/1.1 200 OK
    Date: Mon, 24 Mar 2025 16:03:14 GMT
    Server: WSGIServer/0.2 CPython/3.12.6
    Content-Type: application/json
    Vary: Accept
    Allow: GET, POST, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 364
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Cross-Origin-Opener-Policy: same-origin
     
    [{"id":1,"name":"Sample User","email":"sampleuser@yopmail.com","mobile":"9870104563","tasks":[{"id":1,"name":"Order Shoes","description":"But new shoes from Amazon","created_at":"2025-03-24T13:19:04.927681Z","task_type":"Personal","status":"Pending","users":[1]}]},{"id":2,"name":"Sample User 2","email":"sampleuser2@yopmail.com","mobile":"9870104590","tasks":[]}]

## Get User by ID

### Request

`GET /users/:id`

    curl --location 'http://127.0.0.1:8000/api/users/1/' \
    --header 'Authorization: Token 592afdbdb8964cee85defb606dd6d6d77ef3288b'

### Response

    HTTP/1.1 200 OK
    Date: Mon, 24 Mar 2025 15:57:48 GMT
    Server: WSGIServer/0.2 CPython/3.12.6
    Content-Type: application/json
    Vary: Accept
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 263
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Cross-Origin-Opener-Policy: same-origin
     
    {"id":1,"name":"Sample User","email":"sampleuser@yopmail.com","mobile":"9870104563","tasks":[{"id":1,"name":"Order Shoes","description":"But new shoes from Amazon","created_at":"2025-03-24T13:19:04.927681Z","task_type":"Personal","status":"Pending","users":[1]}]}

## Assign Task to User

### Request

`PATCH /api/tasks/:id`

    curl --location --request PATCH 'http://127.0.0.1:8000/api/tasks/1/' \
    --header 'Authorization: Token 592afdbdb8964cee85defb606dd6d6d77ef3288b' \
    --header 'Content-Type: application/json' \
    --data '{
        "users": [1]
    }'

### Response

    HTTP/1.1 200 OK
    Date: Mon, 24 Mar 2025 15:57:32 GMT
    Server: WSGIServer/0.2 CPython/3.12.6
    Content-Type: application/json
    Vary: Accept
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 168
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Cross-Origin-Opener-Policy: same-origin
     
    {"id":1,"name":"Order Shoes","description":"But new shoes from Amazon","created_at":"2025-03-24T13:19:04.927681Z","task_type":"Personal","status":"Pending","users":[1]}

