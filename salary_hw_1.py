def total_salary(path):
    total_salary = 0
    num_developers = 0
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    total_salary += int(parts[1])
                    num_developers += 1
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

    average_salary = total_salary / num_developers if num_developers > 0 else 0
    return total_salary, average_salary


total, average = total_salary(r"C:\Users\krolc\PycharmProjects\goit-algo-hw-04\salaries.txt")
print(f"Cума заробітної плати: {total}, Середня заробітна плата: {average}")
