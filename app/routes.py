from flask import render_template, flash, redirect, url_for, Blueprint

import os
import random
import time
from flask import Flask, request, render_template, session, flash, redirect, \
    url_for, jsonify
from flask_mail import Mail, Message
from celery import Celery
from app.celery.jobs.long_task import (
    long_task
)

views_blueprint = Blueprint("views", __name__)

@views_blueprint.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@views_blueprint.route('/longtask', methods=['POST'])
def longtask():
    print("Starting long task")
    task = long_task.apply_async()
    return jsonify({}), 202, {'Location': url_for('views.taskstatus',
                                                  task_id=task.id)}


@views_blueprint.route('/status/<task_id>')
def taskstatus(task_id):
    task = long_task.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        # something went wrong in the background job
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # this is the exception raised
        }
    return jsonify(response)
