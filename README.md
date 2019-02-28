# Wordplease

## Prerequisites

1. Python 3
2. pip (Python package manager)
#

## Start

Create database

```shell
python manage.py migrate
```

Create superuser

```shell
python manage.py createsuperuser
```

Get a development environment running
```shell
python manage.py runserver
```

## Website

+ Url: http://127.0.0.1:8000

## API

+ `POST /api/v1/users/<id>/` Any user can register using:

```json
{
	"first_name": "test",
	"last_name": "test",
	"username": "test",
	"email": "test@test.com",
	"password": "test"
}
```

+ `GET /api/v1/users/<id>/` Only admin and authenticated users will be able to display their own account's detail.
+ `PUT /api/v1/users/<id>/` Only admin and authenticated users will be able to update their own account.
+ `DELETE /api/v1/users/<id>/` Only admin and authenticated users will be able to delete their own account.

### Blogs API

+ `GET /api/v1/blogs/` Any user can display a list of urls from the blogs available in the platform.
+ `GET /api/v1/blogs/?search=test&ordering=title&owner_username=test` Standard parameters are available for searching, ordering and filtering


### Posts API

+ `GET /api/v1/posts/` Any user can display the published posts and the owned unpublished when authenticated
+ `GET /api/v1/posts/?search=test&ordering=pub_date&status=PUB` Standard parameters are available for searching, ordering and filtering
+ `POST /api/v1/posts/` Admin and authenticated users will be able to publish posts on their own blogs. If the parameter blog is not present, the post will be assigned to one of the blogs of the user
```json
{
    "title": "this is the title",
    "description": "this is the description",
    "content": "this is the content",
    "video": "https://www.youtube.com/embed/1CRihg1X89A",
    "status": "PUB"
}
```

+ `GET /api/v1/posts/<id>/` Any user will be able to display a post's detail as long as it's published.
+ `PUT /api/v1/posts/<id>/` Only admin and authenticated users will be able to update their own post.
+ `DELETE /api/v1/posts/<id>/` Only admin and authenticated users will be able to delete their own account.

### Files API

+ `GET /api/v1/files/`  Only admin and authenticated users will be able to display the files
+ `POST /api/v1/files/` Only admin and authenticated users will be able to upload files

