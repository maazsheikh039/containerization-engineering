from flask import Flask, jsonify
import os, tempfile

app = Flask(__name__)

@app.route('/')
def hello():
    return f"Read-only container active. UID: {os.getuid()}"

@app.route('/write-test', methods=['POST'])
def write_test():
    try:
        with tempfile.NamedTemporaryFile(mode='w', delete=False, dir='/tmp') as f:
            f.write("Temp data write test")
        return jsonify({"status": "success", "message": "Wrote to /tmp successfully"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/illegal-write', methods=['POST'])
def illegal_write():
    try:
        with open('/app/illegal_file.txt', 'w') as f:
            f.write("Illegal write")
        return jsonify({"status": "success", "message": "File written"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
