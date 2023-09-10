"""
Задание №2
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл.
Добавьте к ним логирование ошибок и полезной информации.
*Также реализуйте возможность запуска из командной строки с передачей параметров
"""

import argparse
import logging
import json
from math import factorial
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] - %(asctime)s - %(message)s')

class Factorial:

    def __init__(self, count: int = 1) -> None:
        self.history = []
        self.count = count

    def __call__(self, n: int = 1) -> list[int]:
        try:
            res = factorial(n)
            entry = {'n': n, 'result': res, 'timestamp': str(datetime.now())}
            self.history.append(entry)
            self.history = self.history[-self.count:]
            logging.info(f'Factorial({n}) calculated. Result: {res}')
            return res
        except ValueError as e:
            logging.error(f'Error while computing factorial({n}): {e}')
            return None

    def get_history(self):
        return self.history

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            logging.error(f'An error occurred: {exc_type}, {exc_val}')
        with open('loggerfactorial.json', 'w', encoding="UTF-8") as js_f:
            json.dump(self.history, js_f, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate factorials and log results')
    parser.add_argument('--count', type=int, default=1, help='Number of history entries to keep')
    parser.add_argument('--n', type=int, default=1, help='Number to calculate factorial for')

    args = parser.parse_args()
    f = Factorial(args.count)

    with f as js_f:
        for i in range(1, args.n + 1):
            result = f(i)
            if result is not None:
                print(f'{i}! = {result}')
            else:
                print(f'Error calculating factorial({i})')