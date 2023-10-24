from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

experts = [{'name': 'albert'}]

@app.route('/')
def index(expert = None):
    if expert:
        return render_template('index.html', experts=experts, expert=expert)
    return render_template('index.html', experts=experts, expert=None)

@app.post('/expert')
@app.post('/expert/')
def selectExpert():
    body = request.form
    expert_name = body.get('expert')
    if expert_name == None:
        return redirect(url_for('index'))
    try:
        expert = list(filter(lambda a: a['name'] == expert, experts))[0]
    except:
        expert = None
    return redirect(url_for('index', expert=expert))

@app.post('/message')
@app.post('/message/')
def genMessage():
    body = request.get_json()
    message = body.get('message')
    if not message:
        return {'error': 'Message field is required'}
    data = requests.get(url = 'http://catfact.ninja/fact').json()
    return {'message': data['fact']}
