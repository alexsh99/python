from time import sleep
from itertools import cycle


class TrafficLight:
    __color = {'RED': 7, 'YELLOW': 2, 'GREEN': 7}

    def running(self):
        for c in cycle(self.__color):
            print(f'{c}', end='')
            sleep(self.__color[c])
            print('\r', end='')


t = TrafficLight()
t.running()
