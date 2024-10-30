import os
import redis
from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

# Configure Redis connection
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))
cache = redis.Redis(host=redis_host, port=redis_port)

# Serve the frontend HTML
@app.route('/')
def serve_frontend():
    return send_from_directory('frontend', 'index.html')

# Check Redis connection on startup
try:
    cache.ping()
    print("Connected to Redis!")
except redis.ConnectionError:
    print("Failed to connect to Redis!")

# API endpoint for visit count
@app.route('/api/visits')
def get_visit_count():
    try:
        count = cache.incr('visits')
        return {'count': count}
    except redis.exceptions.ConnectionError as e:
        return {'error': str(e)}, 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
