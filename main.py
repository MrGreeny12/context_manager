#сделать менеджер контекста, который будет отслеживать open, close и время между ними
#применить это к какой-нибудь программе
from datetime import time
from datetime import date
from datetime import datetime
from datetime import timedelta

class Open_cm:

	

  def __init__(self, path, method):
    self.path = path
    self.method = method
    self.enter = 0
    print(self.path)

  def __enter__(self):
    self.file = open(self.path, self.method)
    self.enter = datetime.now()
    print(self.enter)

  def __exit__(self, exc_type, exc_val, exc_tb):
    exit = datetime.now()
    print(exit)
    self.differ = exit - self.enter
    print(f'Скорость открытия файла = {self.differ} мс')
    self.file.close()


with Open_cm('test.txt', 'r') as g:
   pass
