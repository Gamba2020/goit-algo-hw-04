def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                cat_info = {"id": cat_data[0], "name": cat_data[1], "age": cat_data[2]}
                cats_info.append(cat_info)
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print("An error occurred:", e)

    return cats_info


# Приклад використання:
cats_info = get_cats_info("Cats_info.txt")
print(cats_info)