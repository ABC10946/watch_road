import redis
from prometheus_client import start_http_server, Summary, Counter

class PrometheusMetrics:
    def __init__(self, port=8000, redisEnabled=True):
        self.redis_client = None
        if redisEnabled:
            self.redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

        self.motion_detected_counter = Counter('motion_detected_total', 'Total number of motion detections')
        self.motion_detection_time = Summary('motion_detection_duration_seconds', 'Time spent detecting motion')

        # if motion_count is stored in Redis, get the initial value
        if self.redis_client:
            self.motion_detected_counter.inc(int(self.redis_client.get('motion_count') or 0))

        start_http_server(port)

    def increment_motion_count(self):
        self.motion_detected_counter.inc()
        if self.redis_client:
            self.redis_client.incr('motion_count')

    def measure_motion_detection_time(self, duration):
        self.motion_detection_time.observe(duration)

    def get_motion_count(self):
        if self.redis_client:
            gotCount = int(self.redis_client.get('motion_count') or 0)


        return 0