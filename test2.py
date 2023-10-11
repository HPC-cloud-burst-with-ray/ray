# import ray

# context = ray.init()
# print(context.dashboard_url)
# import ray

# ray.init()

# ray.timeline(filename="timeline.json")
import ray
ray.init()
from pprint import pprint
pprint(ray.nodes())