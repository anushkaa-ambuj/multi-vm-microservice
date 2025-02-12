from flask import Flask, jsonify, request

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
    return jsonify(new_task); 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
