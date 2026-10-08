"""
Кейс-стаді — аналіз CSV-файлу

Ваше завдання — пройти весь шлях від порожньої папки до проєкту на GitHub:

1. Створити папку з проєктом
2. Завантажити туди дані
3. Зробити аналіз
4. Зберегти результат у .txt файл
5. Запушити все на GitHub
"""


# ============================================================
# Крок 1. Створіть папку з проєктом
# ============================================================
# У терміналі:
#
#   mkdir students_analysis
#   cd students_analysis
#
# Усі наступні файли мають лежати всередині цієї папки.


# ============================================================
# Крок 2. Завантажте туди дані
# ============================================================
# Скопіюйте файл students.csv у папку students_analysis.
# Формат файлу: name,math,python,english
# (перший рядок — заголовок, далі по одному студенту в рядку)
#
# Також збережіть цей скрипт у ту саму папку як analyze.py.


# ============================================================
# Крок 3. Зробіть аналіз
# ============================================================
# Потрібно порахувати:
#   - середній бал по класу з кожного предмета (math, python, english);
#   - ім'я студента з найвищим середнім балом (по трьох предметах).

INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"


with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    next(f)

    sum_math = 0
    sum_python = 0
    sum_english = 0
    students = 0
    best_avrg = 0
    best_name = ''
    for line in f:
        line = line.strip().split(',')
        math = float(line[1])
        python = float(line[2])
        english = float(line[3])
        sum_math += math
        sum_python += python
        sum_english += english
        students += 1
        current_avrg = round((math + python + english) / 3, 1)
        if current_avrg > best_avrg:
            best_avrg = current_avrg
            best_name = line[0]
avrg_grade_math = round(sum_math / students, 1)
avrg_grade_python = round(sum_python / students, 1)
avrg_grade_english = round(sum_english / students, 1)

with open(OUTPUT_FILE, 'w') as fout:
    fout.write("Середній бал по класу:\n")
    fout.write(f"math: {avrg_grade_math}\n")
    fout.write(f"python: {avrg_grade_python}\n")
    fout.write(f"english: {avrg_grade_english}\n\n")
    fout.write(f"Найкращий студент: {best_name} ({best_avrg})\n")



print("Середній бал по класу:")
print(f"math: {avrg_grade_math}")
print(f"python: {avrg_grade_python}")
print(f"english: {avrg_grade_english}")
print()
print(f"Найкращий студент: {best_name} ({best_avrg})")


# TODO 1: відкрийте INPUT_FILE через with open(...) as f:
#   і пропустіть рядок заголовка (next(f))

# TODO 2: пройдіться по рядках файлу (for line in f:), для кожного рядка:
#   - приберіть символ переносу рядка (line.strip())
#   - розбийте рядок по комі (line.split(","))
#   - перетворіть оцінки на числа (int або float)

# TODO 3: по ходу циклу накопичуйте:
#   - суми оцінок з кожного предмета та кількість студентів
#   - найкращого студента (ім'я та його середній бал) — порівнюйте
#     середній бал поточного студента з найкращим на цей момент

# TODO 4: після циклу порахуйте середній бал по класу з кожного предмета
#   (сума / кількість студентів)


# ============================================================
# Крок 4. Збережіть результат у .txt файл
# ============================================================
# TODO 5: відкрийте OUTPUT_FILE в режимі 'w' і запишіть туди результат
#   у такому вигляді (числа округліть до одного знака після коми):
#
#   Середній бал по класу:
#   math: 67.8
#   python: 67.9
#   english: 67.9
#
#   Найкращий студент: Ім'я Прізвище (97.0)
#
# Також виведіть цей самий текст на екран через print().
#
# Запустіть скрипт (
#) і перевірте, що в папці
# з'явився файл result.txt.


# ============================================================
# Крок 5. Запушіть усе на GitHub
# ============================================================
# 1) Створіть новий ПОРОЖНІЙ репозиторій на github.com
#    (без README і .gitignore).
#
# 2) У терміналі, всередині папки students_analysis:
#
#   git init
#   git add .
#   git commit -m "Students analysis"
#   git branch -M main
#   git remote add origin <посилання_на_ваш_репозиторій>
#   git push -u origin main
#
# 3) Оновіть сторінку репозиторію на GitHub і переконайтеся, що там
#    є students.csv, analyze.py та result.txt.
