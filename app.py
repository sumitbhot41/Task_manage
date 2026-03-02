from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory task storage (for demo)
tasks = []

# 🏠 Home route
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Task Manager API 🚀",
        "status": "Running",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


# ❤️ Health check
@app.route('/health')
def health():
    return jsonify({
        "status": "OK",
        "server": "Task Manager",
        "time": datetime.now().isoformat()
    })


# 📌 API to receive hit
@app.route('/task', methods=['GET', 'POST'])
def receive_hit():

    # ✅ GET: View all tasks
    if request.method == 'GET':
        return jsonify({
            "message": "All tasks fetched successfully",
            "count": len(tasks),
            "tasks": tasks
        })

    # ✅ POST: Add new task
    if request.method == 'POST':
        data = request.json

        if not data or "task" not in data:
            return jsonify({"error": "Task field required"}), 400

        task = {
            "id": len(tasks) + 1,
            "task": data["task"],
            "created_at": datetime.now().isoformat()
        }

        tasks.append(task)

        print("New Task Added:", task)

        return jsonify({
            "message": "Task added successfully 🎉",
            "task": task
        }), 201


# ✏️ Update task
@app.route('/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json

    for task in tasks:
        if task["id"] == task_id:
            task["task"] = data.get("task", task["task"])
            task["updated_at"] = datetime.now().isoformat()

            return jsonify({
                "message": "Task updated ✅",
                "task": task
            })

    return jsonify({"error": "Task not found"}), 404


# ❌ Delete task
@app.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):

    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]

    return jsonify({
        "message": "Task deleted successfully 🗑️"
    })


if __name__ == '__main__':
    app.run(debug=True)