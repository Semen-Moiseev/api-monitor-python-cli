# api-monitor-python-cli

`APIMonitor` — это консольный инструмент, который позволяет проверять API, выводить статистику и сохранять ее в файлах и логах

## Установка и запуск

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/<your-username>/api-monitor-python-cli.git
cd api-monitor-python-cli
```

### 2. Создайте и активируйте виртуальное окружение

```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # Linux / macOS
```

## Использование

### 1. Запуск мок-сервера

```bash
python mock_server.py
```

### 2. Выполнение команд

```bash
python cli.py <команда>
```

Аргументы:

- check — Проверка API, + config — путь к файлу с эндпоинтами
- stats — Вывод и сохранение в файл статистики проверок
