"""
Задание №1
Создайте класс-функцию, который считает факториал числа при
вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и
их факториалов.
Добавьте к ним логирование ошибок и полезной информации.
*Также реализуйте возможность запуска из командной строки с передачей параметров
"""

import argparse
import logging
import datetime
from math import factorial

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] - %(asctime)s - %(message)s')

class Factorial:

    def __init__(self, count: int = 1) -> None:
        self.history = []
        self.count = count

    def __call__(self, n: int = 1) -> list[int]:
        try:
            res = factorial(n)
            self.history.append({n: res})
            self.history = self.history[-self.count:]
            logging.info(f'Factorial({n}) calculated. Result: {res}')
            return res
        except ValueError as e:
            logging.error(f'Error while computing factorial({n}): {e}')
            return None

    def get_history(self):
        return self.history

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Calculate factorials and log results')
    parser.add_argument('--count', type=int, default=1, help='Number of history entries to keep')
    parser.add_argument('--n', type=int, default=1, help='Number to calculate factorial for')


    args = parser.parse_args()

  
    f = Factorial(args.count)


    for i in range(1, args.n + 1):
        result = f(i)
        if result is not None:
            print(f'{i}! = {result}')
        else:
            print(f'Error calculating factorial({i})')

    print(f.get_history())