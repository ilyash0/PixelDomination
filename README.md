# Pixel Dominator
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
![GitHub License](https://img.shields.io/github/license/ilyash0/TASKILLS2024)

Интерактивная платформа для рисования пикселей в реальном времени. Пользователи могут рисовать, соревноваться и создавать уникальные произведения искусства.

## Установка и запуск сервера

### 1. Склонируйте репозиторий
```bash
git clone <URL репозитория>
cd <название папки>
```

### 2. Установите зависимости
1. Убедитесь, что установлен Python 3.12 или выше.
2. По желанию создайте и активируйте виртуальное окружение:
3. Установите зависимости из `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
### 3. Настройка переменных окружения
1. Создайте файл .env по образцу:
```dotenv
# MAIN
SECRET_KEY=""

# DATABASE
DB_NAME=""
DB_USER="postgres"
DB_PASSWORD=""
DB_HOST="localhost"
DB_PORT="5432"
```
2. Заполните пропуски своими данными

### 4. Настройка базы данных
1. Создайте базу данных PostgreSQL.
2. Примените миграции для Django:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### 5. Запуск сервера
#### Для Django:
```bash
python manage.py runserver
```

### 6. Открытие в браузере
Перейдите по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Контакты
Интерактивный сайт формата Пиксель-баттл на финал хакатона по информационным технологиям "TASKILLS" в 2024 году.
Сайт разработала команда "Code Crew":

- [Илья Шмырёв](https://github.com/ilyash0) 
- [Никита Ваганов](https://github.com/Electr0nic1)