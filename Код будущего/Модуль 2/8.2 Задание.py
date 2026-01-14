import os

def create_folder_and_check_file(folder_path: str, file_name: str) -> bool:
    try:
        os.makedirs(folder_path, exist_ok=True) # создаём папку
    except Exception as e:
        print(f"Не удалось создать папку: {e}")
        return False
    
    file_path = os.path.join(folder_path, file_name)
    exists = os.path.isfile(file_path)
    print(f"Файл '{file_name}' {'существует' if exists else 'не найден'} в папке '{folder_path}'")
    return exists
