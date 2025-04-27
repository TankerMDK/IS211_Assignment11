from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# This is the todo_list that will hold items
todo_list = [
    {'task': 'Buy Milk', 'email': 'testAddress@exmaple.com', 'priority': 'High'}
] # this is a test

@app.route('/')
def index():
    return render_template('index.html', todo_list=todo_list)


@app.route('/submit', methods=['POST'])
def submit():
    task = request.form.get('task')
    email = request.form.get('email')
    priority = request.form.get('priority')

    # Basic validation
    if not task or not email or priority not in ['Low', 'Medium', 'High']:
        return redirect('/')

    # This adds the new to-do item. AKA Submits them.
    todo_list.append({
        'task': task,
        'email': email,
        'priority': priority
    })

    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    todo_list.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)