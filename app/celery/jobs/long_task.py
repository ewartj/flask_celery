import os
import random
import time
from celery import states
from celery.exceptions import Ignore

from app.celery.celery_app import celery_app

LONG_TASK = "long_task"
SHORTTASK = "short_task"

@celery_app.task(name=LONG_TASK, bind=True)
def long_task(self):
    """Background task that runs a long function with progress reports."""
    verb = ['Starting up', 'Booting', 'Repairing', 'Loading', 'Checking']
    adjective = ['master', 'radiant', 'silent', 'harmonic', 'fast']
    noun = ['solar array', 'particle reshaper', 'cosmic ray', 'orbiter', 'bit']
    message = ''
    total = random.randint(10, 50)
    print("running long task")
    for i in range(total):
        print(i)
        if not message or random.random() < 0.25:
            message = '{0} {1} {2}...'.format(random.choice(verb),
                                              random.choice(adjective),
                                              random.choice(noun))
        self.update_state(state='PROGRESS',
                          meta={'current': i, 'total': total,
                                'status': message})
        time.sleep(1)
    return {'current': 100, 'total': 100, 'status': 'Task completed!',
            'result': 42}

@celery_app.task(name=SHORTTASK, bind=True)
def short_task(self):
    """Background task that runs a long function with progress reports."""
    verb = ['Starting up', 'Booting', 'Repairing', 'Loading', 'Checking']
    adjective = ['gollum', 'frodo', 'gandalf', 'sam', 'sauron']
    noun = ['ring', 'axe', 'bow', 'potato', 'bit']
    message = ''
    total = random.randint(10, 50)
    print("running long task")
    for i in range(total):
        print(i)
        if not message or random.random() < 0.25:
            message = '{0} {1} {2}...'.format(random.choice(verb),
                                              random.choice(adjective),
                                              random.choice(noun))
        self.update_state(state='PROGRESS',
                          meta={'current': i, 'total': total,
                                'status': message})
        time.sleep(1)
    return {'current': 100, 'total': 100, 'status': 'Task completed!',
            'result': 42}