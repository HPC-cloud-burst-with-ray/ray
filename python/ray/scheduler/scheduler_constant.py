SERVER_IP = "http://34.199.201.49:8000"

MAX_COMPLEXITY_SCORE = 100000000000
DATA_IP=""

# spec constant
HPC_DIR = "working_dir"
COMPLEXITY_SCORE = "complexity_score"
SCHEDULING_STRATEGY = "scheduling_strategy"

CPU = "num_cpus"
GPU = "num_gpus"
MEMORY = "memory"

USER_TASK_ID = "user_task_id"



# status constant
ASSIGN_NODE = "assign_node"

BIND_TASK_ID = "bind_task_id"
BIND_TASK_STATUS = "bind_task_status"
BIND_TASK_DURATION = "bind_task_duration"
BIND_TASK_START_TIME = "bind_task_start_time"
BIND_TASK_END_TIME = "bind_task_end_time"

USER_TASK_STATUS = "user_task_status"
USER_TASK_DURATION = "user_task_duration"
USER_TASK_START_TIME = "user_task_start_time"
USER_TASK_END_TIME = "user_task_end_time"
USER_TASK_ESTIMATED_START_TIME = "user_task_estimated_start_time"

# Ray task status, See https://docs.ray.io/en/latest/ray-observability/reference/doc/ray.util.state.common.TaskState.html#ray.util.state.common.TaskState
START_TIME = "start_time_ms"
END_TIME = "end_time_ms"
STATE = "state"


# task status
PENDING = "PENDING"
RUNNING = "RUNNING"
FINISHED = "FINISHED"



# Ray node
NODE_ID = "NodeID"
RESOURCE = "Resources"

NODE_CPU = "CPU"
NODE_GPU = "GPU"
NODE_MEMORY = "memory"


AVAILABLE_CPU = "available_cpu"
AVAILABLE_GPU = "available_gpu"
AVAILABLE_MEMORY = "available_memory"

SPEED = "speed"
TOTAL_DURATION = "total_duration"
TOTAL_COMPLEXITY_SCORE = "total_complexity_score"
RUNNING_OR_PENDING_TASKS = "running_or_pending_tasks"

PENDING_TASKS = "pending_tasks"
PENDING_TASKS_COUNT = "pending_tasks_count"

MAX_PENDING_TASK= 2