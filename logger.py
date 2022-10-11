from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler
from typing import Callable, Any


def logger_(path_log: str):
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


# '''Вариант с записью в файл'''
def make_trace(path: str) -> Callable:

    def trace(old_function: Callable) -> Callable:

        def new_function(*args, **kwargs) -> Any:
            result = old_function(*args, **kwargs)

            with open(path, 'a') as log:
                log.write(f'{datetime.utcnow()}: called {old_function.__name__}\n'
                          f'\t args: {args}\n'
                          f'\t kwargs: {kwargs}\n'
                          f'\t result: {result}')

            return result
        return new_function
    return trace


# '''Вариант с использованием logging'''
def make_log(path: str) -> Callable:

    def log(old_function: Callable) -> Callable:
        logger = logging.getLogger(path)
        logger.setLevel(logging.INFO)
        handler = RotatingFileHandler(path, backupCount=10, maxBytes=1000000)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        def new_function(*args, **kwargs) -> Any:
            result = old_function(*args, **kwargs)

            logger.info(f'called: {old_function.__name__}\n'
                        f'\t args: {args}\n'
                        f'\t kwargs: {kwargs}\n'
                        f'\t result: {result}')
            return result

        return new_function

    return log
