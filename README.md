# 🛒 E-commerce Product Analytics

Полный цикл продуктовой аналитики: от проектирования ETL и SQL-мартов до расчёта метрик, RFM-сегментации, когортного анализа и подготовки бизнес-отчёта. Проект демонстрирует умение превращать сырые данные в actionable-инсайты для роста выручки и удержания.

 [📥 Скачать PDF-отчёт](report/Product_Analytics_Report.pdf) |  [Jupyter Notebooks](notebook/) | 🗄 [SQL-скрипты](SQL/)

---

##  Ключевые инсайты

| Метрика | Значение | Бизнес-вывод |
|---------|----------|--------------|
| **Conversion Rate** | `7.93%` | Узкое место воронки. Рост на 2% → +25% к Revenue/Session |
| **AOV** | `2 838 ₽` | Выше бенчмарка (~2 500 ₽), но монетизация сессий низкая |
| **Stickiness (DAU/MAU)** | `~8%` | Норма для e-commerce. Фокус на росте MAU, а не DAU |
| **Pareto (Top 30%)** | `~52% выручки` | Высокая концентрация дохода. Требуется VIP-стратегия удержания |
| **Retention (30d ±3)** | `39%` | Цикличный паттерн возврата (14–30 дней). Подтверждает транзакционную модель |

💡 **Главная точка роста**: Сегмент `New` (10.5% базы) со средним чеком ~4 500 ₽. При конверсии в `Loyal` средний чек вырастает до ~9 800 ₽ → **доходность сегмента удваивается**.

---

##  Стек технологий

| Категория | Инструменты |
|-----------|-------------|
| **Язык & Обработка** | `Python 3.10+`, `pandas`, `numpy` |
| **Базы данных** | `SQLite`, `SQL` (DDL/DML для mart-таблиц) |
| **Анализ & Визуализация** | `Jupyter Notebook`, `matplotlib`, `seaborn` |
| **Отчётность** | `Obsidian` → `PDF`, `Markdown` |
| **Инфраструктура** | `gdown` (загрузка данных), `git` |

---
##  Структура проекта
```
product-analytics/
├── data/ # Сырые и предобработанные данные
│ ├── raw/ # Исходные CSV-файлы
│ └── processed/ # Очищенные датасеты
├── database/ # SQLite БД (analytics.db)
├── SQL/ # Скрипты построения витрин
│ ├── 01_staging.sql
│ ├── 02_user_mart.sql
│ ├── 03_session_mart.sql
│ └── 04_revenue_mart.sql
├── src/ # Python-модули
│ ├── data_loader.py # Подключение к БД и загрузка таблиц
│ ├── metrics.py # Расчёт продуктовых метрик
│ └── utils.py # RFM-сегментация и вспомогательные функции
├── scripts/ # Скрипты автоматизации
│ └── data_download.py # Загрузка данных с Google Drive
├── notebook/ # Jupyter-ноутбуки анализа
│ ├── 01_eda.ipynb
│ ├── 02_metrics_analysis.ipynb
│ ├── 03_cohort_analysis.ipynb
│ └── 04_rfm.ipynb
├── report/ # Аналитический отчёт
│ ├── Product_Analytics_Report.md
│ └── Product_Analytics_Report.pdf
└── README.md
```
## Запуск 

**Клонируйте репозиторий**
```bash
   git clone https://github.com/ArtemShad901/E-commerce-Product-Analytics.git
   cd E-commerce-Product-Analytics
   pip install -r requirements.txt
   python scripts/data_download.py
   jupyter notebook notebook/
```
порядок запуска ноутбуков 
`01_eda.ipynb` → `02_metrics_analysis.ipynb` → `03_cohort_analysis.ipynb` → `04_rfm.ipynb`


### Что было сделано в ходе проекта : 
---

| Компонент             | Описание                                                                                                                          | Где в коде                              |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| ** Модуль метрик**    | Параметризуемый движок расчёта 10+ продуктовых метрик (APRAU, Stickiness, Pareto, CR, AOV и др.)                                  | `src/metrics.py`                        |
| **ETL & Data Marts**  | 4-слойная архитектура витрин (`staging → user/session/revenue_mart`) на SQLite с чётким разделением сырых и агрегированных данных | `SQL/`, `database/`                     |
| **RFM-пайплайн**      | Автоматическая сегментация базы через квантильный скоринг + бизнес-правила кластеризации (VIP, Loyal, New, At Risk, Regular)      | `src/utils.py`, `notebook/04_rfm.ipynb` |
| ** Retention-анализ** | Расчёт exact/windowed retention с настраиваемым окном ±N дней для корректного учёта цикличности возвратов                         | `notebook/03_cohort_analysis.ipynb`     |
| **Бизнес-отчёт**      | Executive summary, разбор монетизации, карта гипотез и                                                                            | `report/Product_Analytics_Report.pdf`   |

