import os
import redis
import time
from flask import Flask, send_from_directory, jsonify

app = Flask(__name__)

# Configure Redis connection
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))
retry_attempts = 5
retry_delay = 2

def connect_to_redis():
    for attempt in range(retry_attempts):
        try:
            cache = redis.Redis(host=redis_host, port=redis_port)
            cache.ping()
            print("Connected to Redis!")
            return cache
        except redis.ConnectionError:
            print(f"Failed to connect to Redis. Attempt {attempt + 1}/{retry_attempts}. Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
    raise redis.ConnectionError("Failed to connect to Redis after multiple attempts.")

# Serve the frontend HTML
@app.route('/')
def serve_frontend():
    return send_from_directory('frontend', 'index.html')

# Connect to Redis
cache = connect_to_redis()

# API endpoint for visit count
@app.route('/api/visits')
def get_visit_count():
    try:
        count = cache.incr('visits')
        return jsonify({'count': count})
    except redis.exceptions.ConnectionError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    
