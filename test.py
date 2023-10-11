import ray
# Specify required resources.
@ray.remote(num_cpus=4, num_gpus=2,label="hi")
def my_function():
    m=1
    for i in range(1000):
        m*=i
    return m
# Override the default resource requirements.
my_function.options(num_cpus=3).remote()
