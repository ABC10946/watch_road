import redis
from prometheus_client import start_http_server, Summary, Counter
import time

class PrometheusMetrics:
    def __init__(self, port=8000):
        self.redis_client = redis.StrictRedis(host='redis', port=6379, db=0)
        self.motion_detected_counter = Counter('motion_detected_total', 'Total number of motion detections')
        self.motion_detection_time = Summary('motion_detection_duration_seconds', 'Time spent detecting motion')

        start_http_server(port)

    def increment_motion_count(self):
        self.motion_detected_counter.inc()
        self.redis_client.incr('motion_count')

    def register_motion_detection(self):
        self.motion_detected_counter.inc()

    def measure_motion_detection_time(self, duration):
        self.motion_detection_time.observe(duration)

    def get_motion_count(self):
        return int(self.redis_client.get('motion_count') or 0)