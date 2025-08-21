Very basic flask app with celery and redis based on https://medium.com/@Aman-tech/celery-with-flask-d1f1c555ceb7.

Its now been modified with routes and blueprints based on a combination of: https://github.com/ericmbernier/ericbernier-blog-posts/tree/master/flask_celery_redis_pokeapi and https://github.com/miguelgrinberg/flask-celery-example.


To run:
```bash
redis-server
celery --app app.celery.celery_app worker --loglevel=info
flask run
```
Output can now be viewed as normal in browser.