from flask import Flask, render_template, request, redirect
import re, os, pickle

app = Flask(__name__)

# This is the todo_list that will hold items
todo_list = [
    {'task': 'Buy Milk', 'email': 'testAddress@exmaple.com', 'priority': 'High'}
] # this is the assigned test



# Building the Extra Credit 1 - Save the List
# NOTICE: This stops the assigned test from populating on to the screen!
SAVE_FILE = 'todo.pkl'

# Load existing todo_list if save file exists
if os.path.exists(SAVE_FILE):
    with open(SAVE_FILE, 'rb') as f:
        todo_list = pickle.load(f)
else:
    todo_list = []

@app.route('/save', methods=['POST'])
def save():
    with open(SAVE_FILE, 'wb') as f:
        pickle.dump(todo_list, f)
    return redirect('/')



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

    # Additional email validation with regex
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "Invalid email address.", 400

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

# Extra Credit -- Deleting Items
@app.route('/delete/<int:task_index>', methods=['POST'])
def delete_task(task_index):
    if 0 <= task_index < len(todo_list):
        todo_list.pop(task_index)
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)