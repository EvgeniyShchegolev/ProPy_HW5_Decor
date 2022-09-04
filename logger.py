from datetime import datetime


def logger(path_log: str):
    def decorator(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)

            str_log = f'{datetime.now()}: name: "{old_function.__name__}", ' \
                      f'arguments: ({args}, {kwargs}), result: {result}'
            with open(path_log, 'w', encoding='utf-8') as file:
                file.write(str_log)

            return result
        return new_function
    return decorator
