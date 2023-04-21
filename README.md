# Django Book Models
Add Django debug toolbar.
Use models from the Django documentation in the application.
https://docs.djangoproject.com/en/4.0/topics/db/aggregation/
Add models to the admin panel. Use more functionality (inline, filters, search, output and grouping of fields in the form, filter_vertical, date_hierarchy ...)

Create several templates, views, and urls to display data on models. (Only output data from the database, without forms)

In views and templates minimize the number of database queries. (Prefetches, selects, annotations, aggregations)

Add cache via Redis

```
    python manage.py migrate
```
```
    python manage.py makemigrations bookstore
```
```
    python manage.py sqlmigrate bookstore 0001
```

### Add 200 random fixtures into db

```
    python manage.py create_book_fixtures 200
```
### Or download fixtures from json file
```
    python manage.py loaddata fixtures.json
```
```
    python manage.py createsuperuser
```
```bash
    ./manage.py runserver
```
# [Main paige with links to all lists](http://127.0.0.1:8000/bookstore/)


# HW 16

# [Authors list ListView](http://127.0.0.1:8000/bookstore/authors/)
# [AuthorDetailView authors/<int:pk>/](http://127.0.0.1:8000/bookstore/authors/155/)
# [Author CreateView](http://127.0.0.1:8000/bookstore/authors/create/)
# [Author UpdateView authors/<int:pk>/update/](http://127.0.0.1:8000/bookstore/authors/155/update/)
# [Author DeleteView authors/<int:pk>/delete/](http://127.0.0.1:8000/bookstore/authors/155/delete/)

# HW 17 


## Cache was added to BookList page because it have the biggest number of relations. Pagination = 500.
## Fixtures, management command, etc.  at top of readme
# [Booklist page with cache](http://127.0.0.1:8000/bookstore/booklist_cache)
