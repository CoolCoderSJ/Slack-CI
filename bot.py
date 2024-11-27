from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os, requests

load_dotenv()

app = Flask(__name__)

@app.post('/canvas')
def list_canvases():
    print(request.form)

    r = requests.get(f"https://slack.com/api/conversations.info?channel={request.form['channel_id']}", headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ['TOKEN']}"
    })
    props = r.json()['channel']['properties']
    if "canvas" not in props:
        return "no canvas found"

    return f"Canvas ID: `{props['canvas']['file_id']}`"


@app.post('/update_canvas/<canvas_id>')
def update_canvas(canvas_id):
    print(request.json)

    r = requests.post("https://slack.com/api/canvases.edit", headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ['TOKEN']}"
        }, json={
              "canvas_id": canvas_id,
              "changes": [
                {
                  "operation": "replace",
                  "document_content": {
                    "type": "markdown",
                    "markdown": request.json['content']
                  }
                }
              ]
    })

    return r.json(), r.status_code

app.run('0.0.0.0', 7522, debug=True)