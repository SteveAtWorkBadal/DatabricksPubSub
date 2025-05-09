import os
import json
from random import randrange
import time
import datetime
from google.cloud import pubsub_v1

project_id = os.environ["GCP_PROJECT"]
topic_id = os.environ["GCP_TOPIC_ID"]
publisher = pubsub_v1.PublisherClient()
# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_id}`
topic_path = publisher.topic_path(project_id, topic_id)
print(topic_path)

with open("./data/events.json", 'r') as f:
    data = json.load(f)
    for row in data:
        now = datetime.datetime.now()
        row['event_date'] = now.strftime("%Y-%m-%d %H:%M:%S")
        data = json.dumps(row).encode("utf-8")
        api_future = publisher.publish(topic_path, data=data)
        message_id = api_future.result()
        print(message_id)
        time.sleep(randrange(1, 10))

print(f"messages published to {topic_path}")
