from flask import Flask, render_template, request
# request will be used for input forms

import json

from google.cloud import firestore
# Case 1 was added via Firestore console manually.

# to implement inputcheck, i.e. valiate user uploaded data
# from inputcheck import inputcheck

app = Flask(__name__)



@app.route('/')
def index():
    '''
    Temporary hack for showing the exposome X metabolome study
    '''
    return render_template('exposome.html', )


@app.route('/main')
def explore():
    '''
    This should be the front page
    Use case #1 to show on front page.
    '''
    result = get_json('1')
    # result = test_local()
    return render_template('index.html', result_data = result, )

# Temporary hack - don't touch these two for now
@app.route('/exposome')
def exposome():
    '''
    Temporary hack for showing the exposome X metabolome study
    '''
    return render_template('exposome.html', )

@app.route('/malaria')
def malaria():
    '''
    Temporary hack for showing the Malaria transcriptomics X metabolomics study
    '''
    return render_template('malaria.html', )

     

#@app.route('/show/<case_id>')

def get_json(case_id):
    '''
    job status is checked in /check/jid
    '''
    db = firestore.Client()
    doc_ref = db.collection(u'Case').document(u'exposome')
    try:
        doc = doc_ref.get()
        print (doc)
        print(doc.project)
        return "test CHDS 451 - set 1"
        #return json.loads(doc.json)
    except:
        # ?
        return (u'No such document!', 401)



def test_local():
    '''
    local read to test. Not working on GAE
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
