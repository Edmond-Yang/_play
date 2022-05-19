from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
#userID = ['cse00_6698', 'cse00_6502', 'cse00_5188', 'cse00_6966', 'cse00_4857', 'cse01_1121', 'cse01_2801',
#          'cse01_8756', 'cse01_9728', 'cse01_7737', 'cse02_6601', 'cse02_7681', 'cse02_7707', 'cse02_1240',
   #       'cse02_5947', 'cse03_3827', 'cse03_2845', 'cse03_7613', 'cse03_1466', 'cse03_3443']


state = {ids: False for ids in userID}
group = {'0': 'a', '1': 'a', '2': 'b', '3': 'b'}
state_game = {'a': False, 'b': False}


@app.route('/login', methods=['GET', 'POST'])
def index():
    global group
    if request.method == 'POST':
        if request.form.get('ID') in userID and request.form.get('ID')[4] in group.keys():
            return redirect(url_for('waiting', username=request.form.get('ID'), groups=group[request.form.get('ID')[4]]))
        else:
            flash('wrong user ID')

    return render_template('index.html')


@app.route('/data/<groups>')
def data(groups):
    global group, state, state_game

    if state_game[groups]:
        return 'OK'

    group_list = [num for num in group.keys() if group[num] == groups]
    text = ''
    all_ok = True

    for i in state.keys():
        if i[4] in group_list:
            if state[i]:
                text += '<p><img src="/static/image/greenlight.png" width = "20">' + i + '</p>'
            else:
                text += '<p><img src="/static/image/redlight.png" width = "20">' + i + '</p>'
                all_ok = False

    if all_ok:
        state_game[groups] = True

    return text


@app.route('/waiting/<groups>/<username>')
def waiting(groups, username):
    global state
    state[username] = True
    return render_template("waiting.html", groups=groups, username=username)


@app.route('/game/<groups>/<username>')
def game(groups, username):
    return username + ' in game ' + groups


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.secret_key = "Your Key"
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port, debug=True)

