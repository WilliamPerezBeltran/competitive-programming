
import time

class FunctionTime():
    @staticmethod
    def decorator(func):
        def wrapper(*args, **kwargs):
            inicial_time = time.time() 
            func(*args, **kwargs)
            final_time = time.time() 
            test = final_time - inicial_time
            return round(test,5)
        return wrapper 




