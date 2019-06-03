from flask import Flask, render_template, request
# request will be used for input forms

import json

# GAE has changed to Datastore lib: https://pypi.org/project/google-cloud-datastore/
# have to update the code below
# from google.appengine.ext import ndb
# from datamodel import *

# to implement inputcheck, i.e. valiate user uploaded data
# from inputcheck import inputcheck

app = Flask(__name__)

@app.route('/')
def explore():
    '''
    Use case #1 to show on front page.
    '''
    # result = get_json(1)
    result = test_local()
    return render_template('index.html', result_data = result, )

     

@app.route('/show/<case_id>')
def get_json(case_id):
    '''
    job status is checked in /check/jid
    '''
    jid = int(case_id)
    this_case = Case.query( Case.id==jid ).get()

    if this_case:
        return json.loads(this_case.json)

    else:
        return 'Incorrect credential.', 401

def test_local():
    '''
    local read to test
    '''
    result = json.loads( open('result.json', 'r').read() )
    return result
    


def use_user_data():
    '''
    Yet to implement
    '''
    pass

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8090, debug=True)
# [END gae_python37_app]
