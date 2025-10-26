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

python cli.py check endpoints.json
python cli.py stats
python cli.py graphs --dispersion
python cli.py graphs --average
```

Аргументы:

- check — Проверка API, + config — путь к файлу с эндпоинтами
- stats — Вывод и сохранение в файл статистики проверок
- graphs — Вывод графиков + --dispersion — график разюроса времени отклика / --average — график средних времени отклика

<img width="998" height="570" alt="image" src="https://github.com/user-attachments/assets/acbe6a50-dd87-4cfe-b959-da3b3363ffa0" />
<img width="997" height="569" alt="image" src="https://github.com/user-attachments/assets/d0aa794a-c5c1-4a67-bc1a-e14f4c09b679" />



