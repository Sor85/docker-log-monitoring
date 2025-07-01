from flask import Flask, render_template, jsonify, request
import docker

app = Flask(__name__)
client = docker.from_env()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/containers')
def get_containers():
    try:
        containers = client.containers.list(all=True)
        container_data = [
            {
                'id': c.short_id,
                'name': c.name,
                'status': c.status,
                'image': c.image.tags[0] if c.image.tags else 'N/A'
            }
            for c in containers
        ]
        return jsonify(container_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

import re

@app.route('/api/logs', methods=['POST'])
def get_logs():
    try:
        data = request.get_json()
        container_ids = data.get('container_ids', [])
        filter_regex = data.get('filter_regex')

        if not container_ids:
            return jsonify({'logs': ''})

        all_logs = ""
        for container_id in container_ids:
            try:
                container = client.containers.get(container_id)
                logs = container.logs(tail=200, stream=False).decode('utf-8')
                
                if filter_regex:
                    try:
                        filtered_logs = []
                        for line in logs.splitlines():
                            if re.search(filter_regex, line):
                                filtered_logs.append(line)
                        logs = "\n".join(filtered_logs)
                    except re.error as e:
                        logs = f"无效的正则表达式: {e}"

                all_logs += f"--- Logs for {container.name} ({container.short_id}) ---\n{logs}\n\n"
            except docker.errors.NotFound:
                all_logs += f"--- Logs for {container_id} (Not Found) ---\nContainer not found.\n\n"
            except Exception as e:
                all_logs += f"--- Logs for {container_id} (Error) ---\n{str(e)}\n\n"
        return jsonify({'logs': all_logs})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)