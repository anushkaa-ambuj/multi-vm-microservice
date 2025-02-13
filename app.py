from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory Task Storage
tasks = [
    {'id': 1, 'title': 'Sample Task 1', 'completed': False}
]

# Routes
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def add_task():
    new_task = {
        'id': len(tasks) + 1,
        'title': request.json['title'],
        'completed': False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if not task:
        abort(404, description="Task not found.")
    task['title'] = request.json.get('title', task['title'])
    task['completed'] = request.json.get('completed', task['completed'])
    return jsonify(task)

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Task deleted'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)