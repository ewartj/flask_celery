long_task = "long_task"


broker_url = "redis://localhost:6379/0"
imports = ["app.celery.jobs.long_task"]
result_backend = "redis://localhost"
task_default_queue = long_task