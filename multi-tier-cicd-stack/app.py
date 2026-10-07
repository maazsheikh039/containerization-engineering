import os
from flask import Flask, jsonify
import redis

app = Flask(__name__)

REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', '')

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True)

@app.route('/')
def root():
    try:
        count = r.incr('hits')
    except Exception as e:
        count = f"Redis error: {str(e)}"
    return jsonify({
        "app_name": "cicd-microservice",
        "version": "1.0.0",
        "environment": os.getenv('APP_ENV', 'production'),
        "request_counter": count
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "http_code": 200}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
