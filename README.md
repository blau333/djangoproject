# Семинар 1. Инициализация проекта

## Цели семинара

К концу занятия студент должен:

- понимать, зачем нужен менеджер зависимостей и изоляция окружения;
- уметь инициализировать Python‑проект с помощью `uv`;
- создать и запустить базовый Django‑проект;
- понимать назначение ключевых файлов Django;
- уметь инициализировать git‑репозиторий и сделать первый коммит;
- иметь базовую автоматизацию через `pre-commit` и `Makefile`.

---

## Теоретическая часть

### 1. uv — менеджер окружений и зависимостей

**Что это:**
`uv` — современный инструмент для работы с Python‑проектами. Он заменяет сразу несколько вещей:

- `venv`
- `pip`
- Сборщик пакетов

**Почему используем:**

- быстрое создание окружения;
- фиксированные зависимости;
- единый интерфейс для команд.

#### Установка

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Linux / macOS:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Проверка установки:

```bash
uv --version
```

---

### 2. Инициализация проекта

1. Создаём директорию проекта:

```bash
mkdir blog_project
cd blog_project
```

2. Инициализируем Python-проект:

```bash
uv init --package .
```

**Что происходит:**

- создаётся `pyproject.toml`;
- подготавливается структура проекта;
- uv понимает, что это пакет.

#### Активация виртуального окружения

`uv` создаёт виртуальное окружение автоматически, но иногда удобно явно активировать его, особенно для понимания, где выполняются команды.

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

Если PowerShell запрещает выполнение скриптов:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

После активации в терминале появится префикс с именем окружения (обычно `.venv`).

Важно:

- при использовании `uv run` явная активация **не обязательна**;
- активация нужна для понимания концепции виртуальных окружений и ручной работы с Python.

---

### 3. Установка и создание Django‑проекта

#### Установка Django

```bash
uv add django
```

Django будет зафиксирован в `pyproject.toml`.

#### Создание проекта

Мы создаём Django‑проект в папке `src`, чтобы отделить код от конфигурации.

```bash
uv run django-admin startproject blog_project src/blog_project
```

**Объяснение:**

- `uv run` — запускает команду внутри виртуального окружения;
- `blog_project` — имя Django‑проекта;
- `src/blog_project` — путь, где лежит код.

#### Запуск сервера

```bash
uv run src/blog_project/manage.py runserver
```

Открыть в браузере: [http://127.0.0.1:8000](http://127.0.0.1:8000/)

---

### 4. Структура Django‑проекта (база)

```text
blog_project/
├── pyproject.toml
├── src/
│   └── blog_project/
│       ├── blog_project/
│       │   ├── settings.py
│       │   ├── urls.py
│       │   ├── asgi.py
│       │   └── wsgi.py
│       └── manage.py
```

#### Ключевые файлы

- **manage.py** — точка входа для управления проектом (сервер, миграции, команды)
- **settings.py** — конфигурация проекта (БД, приложения, middleware)
- **urls.py** — маршрутизация (URL → view)

Важно: _мы пока ничего не пишем, только понимаем назначение_.

---

### 5. Git: базовые действия

#### Инициализация репозитория

```bash
git init
```

#### Основные команды

```bash
git add -A
git commit -m "Initial commit"
```

Работа с удалённым репозиторием:

```bash
git push
git pull
```

**Важно:**

- коммит — это зафиксированное состояние проекта;
- писать осмысленные сообщения.

---

### 6. pre-commit

**Что это:**
Инструмент, который автоматически запускает проверки перед коммитом.

#### Установка

```bash
uv add pre-commit
```

#### Файл `.pre-commit-config.yaml`

Минимальный пример:

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v6.0.0
    hooks:
      - id: trailing-whitespace
      - id: check-yaml
        exclude: ^migrations/
      - id: check-case-conflict
      - id: check-merge-conflict
      - id: end-of-file-fixer

  - repo: https://github.com/asottile/pyupgrade
    rev: v3.21.2
    hooks:
      - id: pyupgrade
        args: [--py313-plus]

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.13.0
    hooks:
      - id: ruff-check
        args: ["--fix", "--line-length=120"]
```

Активация:

```bash
uv run pre-commit install
```

Теперь при каждом `git commit` будут запускаться проверки.

Ручной запуск:

```bash
uv run pre-commit run -a
```

**Важно:**

pre-commit проверяет только файлы добавленные в git!

---

### 7. Makefile

**Зачем:**

- скрыть длинные команды;
- единый интерфейс для проекта.

Пример `Makefile`:

```makefile
run:
    uv run src/blog_project/manage.py runserver
```

Запуск:

```bash
make run
```

Пояснение: `make` ищет файл `Makefile` и выполняет указанную цель.

Установка на Windows:

1. Запустить PowerShell от имени администратора: ПКМ по кнопке Пуск -> PowerShell (Администратор)

2. Установить make:

```powershell
winget install ezwinports.make
```

4. Проверить установку:

```powershell
make --version
```

Установка на MacOS:

1. Установить Homebrew (если не установлен):

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Установить make:

```bash
brew install make
```

3. Проверить установку:

```bash
make --version
```

---

## Практическая часть семинара

### Задача 1 (15 минут)

**Цель:** получить запущенный Django‑проект.

Что нужно:

- установить `uv`;
- инициализировать проект;
- установить Django;
- создать и запустить сервер.

---

### Задача 2 (5–15 минут)

**Цель:** базовая инфраструктура качества.

Что нужно:

- `git init`;
- добавить `.pre-commit-config.yaml`;
- установить и активировать `pre-commit`.

---

### Задача 3 (5 минут)

**Цель:** автоматизация запуска.

Что нужно:

- создать `Makefile`;
- добавить команду `run`;
- запустить проект через `make`.

---

### Задача 4 (5–15 минут)

**Цель:** зафиксировать результат.

Что нужно:

- первый коммит;
- создать репозиторий на GitHub;
- выполнить `push`.

---

## Домашнее задание

1. Полностью настроить проект:
    - uv
    - pre-commit
    - Makefile
2. GitHub‑репозиторий:
    - защищённая ветка `main` (Изучить вопрос самостоятельно!)
3. Описать проделанное в README.md
4. Добавить команду по запуску pre-commit в Makefile

Формат сдачи:
я сделал
