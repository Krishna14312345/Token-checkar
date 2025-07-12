from flask import Flask, request, render_template_string
import json

app = Flask(__name__)

# Your HTML embedded here
html_template = ''' 
<!-- paste your entire HTML here as-is -->
'''  # Replace this with your actual HTML (or serve from template if separate)

@app.route('/')
def index():
    return render_template_string(html_template)

@app.route('/configure', methods=['POST'])
def configure():
    try:
        appstate_raw = request.form['appstate']
        thread_id = request.form['threadId']
        enforced_name = request.form['enforcedName']

        # Try to parse appstate JSON to validate
        try:
            appstate = json.loads(appstate_raw)
        except json.JSONDecodeError:
            return "Invalid appstate JSON!", 400

        # Log or process the values here
        print("Received appstate:", appstate)
        print("Thread ID:", thread_id)
        print("Enforced Name:", enforced_name)

        # Simulated response
        return f"Monitoring started for group {thread_id} with name '{enforced_name}'"
    
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
