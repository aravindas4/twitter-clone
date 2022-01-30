# Twitter Clone

The Backend APIs for Twitter.

## Getting Started

1. Need to make sure [python3.8+](https://www.python.org/downloads/release/python-380/) is installed on the machine
2. Need to create and activate a [virtualenv](https://docs.python.org/3/library/venv.html)
```bash
virtualenv -p python3.8 doc-lib
source ./doc-lib/bin/activate
```

3. Installed the dependencies
```bash
pip3 install -r requiremnets.txt
```
4. Move into environemnt and clone the [repo](https://github.com/aravindas4/doc-lib)
5. Duplicate `.env.example` file into `.env` and replace the dummy values with genuine
6. Run the migration command
```bash
python manage.py migrate
```

7. Run the local server
```bash
python manage runserver
```
8. Create a user using command
```bash 
   python manage.py createsuperuser
```

## Local Links:
1. Admin: `http://127.0.0.1:8000/admin/`. Example:
user:` admin` 
password: `something`


## Tech Stack
Python 3.8, Django, Django Rest Framework, Sqlite

## Assumptions and Conventions
1. Authentication mechanism used is [JWT Authentication](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html) 
2. [Pre-commit](https://pre-commit.com/) framework is used to do auto formatting using black
3. All the secrets are kept in gitignored file `.env` supported by [decouple](https://pypi.org/project/python-decouple/)
4. All list APIs are [paginated](https://www.django-rest-framework.org/api-guide/pagination/)
5. A file, `utils.py`, houses various utils in the code
6. While developing APIs, Resource Model approach is used ie, For each DB model a Viewset.

## Database Design
There are 2 models
1. User - Represents the user or human [Abstract fields provided by django]
2. Tweet -Represents a tweet by an author
`Fields: Owner: text, author (FK)`

## API Structures

### Tweet Resource:
1. Create - POST `{{host}}/apis/tweet/`
Input:
```
{
   "text": "KKKhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhKKKhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhKKKhhhhhhhhhhhhhhhhh"
}
```

Output: 
```
{
    "id": "D1032F325D",
    "author": "AD3CC8A61A",
    "created_at": "2022-01-30 14:07:43",
    "author_username": "aravinda",
    "text": "KKKhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhKKKhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhKKKhhhhhhhhhhhhhhhhh"
}
```
2. List - GET `{{host}}/apis/tweet/?date=2022-01-22`
Output:
```
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "D1032F325D",
            "author": "AD3CC8A61A",
            "created_at": "2022-01-30 14:07:43",
            "author_username": "aravinda",
            "text": "KKKhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhKKKhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhKKKhhhhhhhhhhhhhhhhh"
        }
    ]
}
```
3. Delete Multiple - POST `{{host}}/apis/tweet/multi/delete/`
Input: 
```
{
    "ids": ["8B7FD4AE5D", "unrelated_ids"]
}
```
Output: 
```
{
    "count": 1,
    "tweets": [
        {
            "id": "8B7FD4AE5D",
            "author": "B24426179A",
            "created_at": "2022-01-30 14:27:59",
            "author_username": "aravinda_s",
            "text": "hddd"
        }
    ]
}
```

### User
1. Create - POST `{{host}}/apis/user/`
Input: 
```
{
    "username": "aravinda_s",
    "password": "very_secret"
}
```

Output:
```
{
    "id": "B24426179A",
    "username": "aravinda_s",
    "created_at": "2022-01-30 14:14:56"
}
```
2. Get Bearer for authentication - POST `{{host}}/apis/token/`
```
{
    "username": "arasvinda_s",
    "password": "very_secret"
}
```

Output: 
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0MzYxODg2NywiaWF0IjoxNjQzNTMyNDY3LCJqdGkiOiJkNWEwOWUyNDRiZTc0MTE3OTVkMGVmNDJlMWYwYmI4MyIsInVzZXJfaWQiOiJCMjQ0MjYxNzlBIn0.l_yStiaLHB2GfJIMRY67ot8W-VPYuvmHuaMZwNNmPsI",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQzNTM5NjY3LCJpYXQiOjE2NDM1MzI0NjcsImp0aSI6IjZjMzJiY2VmOWZmNTQxY2RhNzEwOTYzNzRkZGQ0MzVjIiwidXNlcl9pZCI6IkIyNDQyNjE3OUEifQ.ayP5MpBdB8-I4shWLTcrqxhivIDLzs6jXmtXkxNP8MU"
}
```
