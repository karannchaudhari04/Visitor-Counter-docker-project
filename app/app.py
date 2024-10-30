import os
import redis
from flask import Flask, send_from_directory

app = Flask(__name__)

# Configure Redis connection
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = os.getenv("REDIS_PORT", 6379)
cache = redis.Redis(host=redis_host, port=redis_port)

# Serve the frontend HTML
@app.route('/')
def serve_frontend():
    return send_from_directory('frontend', 'index.html')

# API endpoint for visit count
@app.route('/api/visits')
def get_visit_count():
    try:
        count = cache.incr('visits')
        return {'count': count}
    except redis.exceptions.ConnectionError as e:
        return {'error': str(e)}, 500
@app.route('/')
def index():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
