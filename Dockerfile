# Используем базовый образ с Python
FROM python:3.9

# Устанавливаем необходимые библиотеки
RUN pip install pyserial

# Копируем ваш скрипт в контейнер
COPY my_serial_program.py /app/my_serial_program.py

# Устанавливаем рабочую директорию
WORKDIR /app

# Запускаем скрипт
CMD ["python", "my_serial_program.py"]

