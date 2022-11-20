Intensive Yandex

![flake8 test](https://github.com/dino-mayk/IntensiveYandex/actions/workflows/python-package.yml/badge.svg)

# Оглавление

- [Установка](#установка)
- [Запуск](#запуск)
- [Тесты](#тесты)

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
python manage.py runserver
```
Mac, Linux:
```bash
python3 manage.py runserver
```

# Тесты

Windows:
```bash
python manage.py test
```
Mac, Linux:
```bash
python3 manage.py test
```

## Другое

Критичные данные располагаются в .env локально, для разработки в dev.env.
Чтобы запустить на production измените комментарий в settings.py.

Запуск isort:
```bash
isort .
```

Диаграмма базы данных:
```bash
https://app.quickdatabasediagrams.com/#/d/ReX14b
```