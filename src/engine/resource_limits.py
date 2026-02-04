import psutil

def check_resource_limits(memory_limit_mb=100, cpu_time_limit_s=10):
    process = psutil.Process()
    mem = process.memory_info().rss / (1024 * 1024)
    if mem > memory_limit_mb:
        raise MemoryError(f"Memory limit exceeded: {mem:.2f} MB > {memory_limit_mb} MB")
    cpu_time = process.cpu_times().user + process.cpu_times().system
    if cpu_time > cpu_time_limit_s:
        raise RuntimeError(f"CPU time limit exceeded: {cpu_time:.2f} s > {cpu_time_limit_s} s")
