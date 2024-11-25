import random
import time
import logging
from redis.sentinel import Sentinel


logger = logging.getLogger(__name__)
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

# Configuration for Sentinel
sentinels = [
    ('redis-headless.redis.svc.cluster.local', 26379),  # Statefulset DNS
]
# Connecting to Redis Sentinel
sentinel = Sentinel(sentinels, socket_timeout=0.5)
# Get the master for the service
master = sentinel.master_for('mymaster', socket_timeout=0.5)
# Get a slave for read operations
slave = sentinel.slave_for('mymaster', socket_timeout=0.5)


def make_operation():
    users = [
        ("user:mark", {"name": "mark", "view": "0"}),
        ("user:bob", {"name": "bob", "view": "0"}),
        ("user:alice", {"name": "alice", "view": "0"}),
        ("user:jason", {"name": "jason", "view": "0"}),
        ("user:tony", {"name": "tony", "view": "0"}),
    ]
    index = random.randint(0, len(users)-1)
    # Write to Redis (master)
    h_key, mapping = users[index]
    if not master.hexists(h_key, "view"):
        master.hset(h_key, mapping=mapping)
    # Read from Redis (slave)
    record = slave.hgetall(h_key)
    logger.info(f"Value from Redis slave: {record}")
    master.hincrby(h_key, "view", 1)


if __name__ == "__main__":
    while True:
        make_operation()
        time.sleep(random.randint(1, 5))
