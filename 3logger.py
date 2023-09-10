"""
Задание №3
Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.
Добавьте к ним логирование ошибок и полезной информации.
*Также реализуйте возможность запуска из командной строки с передачей параметров
"""

import logging
import argparse

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] - %(asctime)s - %(name)s - %(message)s')

class Factorial:

    def __init__(self, *args) -> None:
        logging.info(f'Initializing Factorial with arguments: {args}')
        match args:
            case (stop, ):
                self.stop = stop
                self.start = 1
                self.step = 1
            case (start, stop, ):
                self.start = start
                self.stop = stop
                self.step = 1
            case (start, stop, step):
                self.start = start
                self.stop = stop
                self.step = step
        self.res = 1

    def __iter__(self):
        return self

    def __next__(self):
        try:
            while self.start <= self.stop:
                self.res *= self.start
                self.start += self.step
                return self.res
            raise StopIteration
        except Exception as e:
            logging.error(f'An error occurred: {e}')
            raise StopIteration

if __name__ == '__main__':
   
    parser = argparse.ArgumentParser(description='Calculate factorials and log results')
    parser.add_argument('args', nargs='+', type=int, help='Arguments for Factorial class (stop, start stop, or start stop step)')

    args = parser.parse_args()
 
    f = Factorial(*args.args)

    print(list(f))