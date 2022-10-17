Intensive Yandex

# Установка

Клонируйте репозиторий:
```bash
git clone https://github.com/dino-mayk/IntensiveYandex.git
```

Создайте виртуальное окружение:

Windows:
```bash
python -m venv venv
```
Mac, Linux:
```bash
python3 -m venv venv
```

Активируйте виртуальное окружение:

Windows:
```bash
cd venv/Scripts/
.\activate
```
Mac, Linux:
```bash
source venv/bin/activate
```

Скачайте зависимости:

Windows:
```bash
pip install -r requirements.txt
```
Mac, Linux:
```bash
pip3 install -r requirements.txt
```

# Запуск 

Windows:
```bash
python IntensiveYandex/manage.py runserver
```
Mac, Linux:
```bash
python3 IntensiveYandex/manage.py runserver
```

# Другое

Критичные данные располагаются в .env локально, для разработки в dev.env.
Для запуска на продакшен измените комментарий в settings.