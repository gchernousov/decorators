from datetime import datetime

def log_decorator(file_path):
    def add_log(old_func):
        def new_func(*args, **kwargs):
            arguments_in = args, kwargs
            result = old_func(*args, **kwargs)
            datetime.now()
            req_line = f"{datetime.now()}: function: {old_func.__name__}, incoming arguments: {arguments_in}, result: {result}\n"
            with open(file_path, "a", encoding="utf-8") as file:
                file.write(req_line)
                file.close()
            return result
        return new_func
    return add_log