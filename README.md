Very basic flask app with celery and redis based on https://medium.com/@Aman-tech/celery-with-flask-d1f1c555ceb7.

To run:
```bash
redis-server
celery -A tasks worker --loglevel INFO
python app.py
```
Use postman to interact with the app:
```bash
http://127.0.0.1:5000/trigger_task?iterations=10
127.0.0.1:5000/get_result?result_id=bd069dc5-2c50-443b-8af2-3b88c91e787d
```