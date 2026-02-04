import multiprocessing
import traceback

def run_in_sandbox(func, *args, **kwargs):
    def wrapper(q, *args, **kwargs):
        try:
            result = func(*args, **kwargs)
            q.put(result)
        except Exception as e:
            q.put(traceback.format_exc())
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=wrapper, args=(q,)+args, kwargs=kwargs)
    p.start()
    p.join()
    return q.get()
