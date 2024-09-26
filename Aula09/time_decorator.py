import time
from functools import wraps

def time_measure_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Função {func.__name__} executada em {end_time - start_time:.4f}")
        return result
    return wrapper