import serial  # Импортирует библиотеку для работы с последовательными портами
import time  # Импортирует модуль работы со временем
import serial.tools.list_ports  # Импортирует инструменты для работы с портами

speeds = ['1200','2400', '4800', '9600', '19200', '38400', '57600', '115200']  # Список скоростей передачи данных
ports = [p.device for p in serial.tools.list_ports.comports()]  # Список доступных последовательных портов
port_name = ports[0]  # Выбор первого доступного порта
port_speed = int(speeds[-1])  # Установка скорости передачи данных на максимальную
port_timeout = 10  # Установка тайм-аута в 10 секунд
ard = serial.Serial(port_name, port_speed, timeout=port_timeout)  # Открытие последовательного порта
time.sleep(1)  # Ожидание 1 секунду для инициализации
ard.flushInput()  # Очистка входного буфера порта

try:
    msg_bin = ard.read(ard.inWaiting())  # Чтение данных из порта
    msg_bin += ard.read(ard.inWaiting())  # Чтение оставшихся данных
    msg_bin += ard.read(ard.inWaiting())
    msg_bin += ard.read(ard.inWaiting())  # Повторное чтение данных
    msg_str_ = msg_bin.decode()  # Декодирование байтов в строку
    print(len(msg_bin))  # Вывод длины полученного сообщения
except Exception as e:  
    print('Error!')  # Вывод сообщения об ошибке, если что-то пошло не так
ard.close()  # Закрытие порта
time.sleep(1)  # Ожидание перед завершением
print(msg_str_)  # Вывод полученной строки
