import ray
# Specify required resources.
@ray.remote(num_cpus=4, num_gpus=2,label="hi")
def my_function():
    return 1


# Override the default resource requirements.
my_function.options(num_cpus=3,label="second try").remote()
# my_function.remote()