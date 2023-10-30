# a = int(input("Enter your first number: "))
# b = int(input("Enter your second number: "))
# c = a+b
# print(c)

import pathlib

# # path = pathlib.Path("C:\softclub\python\week_3\day_4\salom.txt")
# path = pathlib.Path(r"C:\Users\Пайрав\Desktop\Лист Microsoft Excel.xlsx")
# # path = pathlib.Path("C:/softclub/python/week_3/day_4/salom.txt")
# path.unlink()

import os
import shutil
from pathlib import Path

def list_files(directory):
    folder = Path(directory)
    files = folder.glob('*')
    for file in files:
        if file.is_file():
            try:
                size = file.stat().st_size
                modified_time = file.stat().st_mtime
                print(f"File name: {file.name}")
                print(f"Size: {size} bytes")
                print(f"Modified time: {modified_time}")
            except OSError as e:
                print(f"Error: {e}")

def create_file(file_name):
    file_path = Path(file_name)
    if not file_path.exists():
        try:
            file_path.touch()
            print(f"File {file_path} created successfully")
        except OSError as e:
            print(f"Error: {e}")
    else:
        print(f"File {file_path} already exists")

def create_directory(directory_name):
    directory_path = Path(directory_name)
    if not directory_path.exists():
        try:
            directory_path.mkdir()
            print(f"Directory {directory_path} created successfully")
        except OSError as e:
            print(f"Error: {e}")
    else:
        print(f"Directory {directory_path} already exists")

def delete_file(file_name):
    file_path = Path(file_name)
    if file_path.exists():
        try:
            os.remove(file_name)
            print(f"File {file_path} deleted successfully")
        except OSError as e:
            print(f"Error: {e}")
    else:
        print(f"File {file_path} does not exist")

def delete_directory(directory_name):
    directory_path = Path(directory_name)
    if directory_path.exists():
        try:
            shutil.rmtree(directory_name)
            print(f"Directory {directory_path} deleted successfully")
        except OSError as e:
            print(f"Error: {e}")
    else:
        print(f"Directory {directory_path} does not exist")

def rename_file(file_name, new_name):
    file_path = Path(file_name)
    if file_path.exists():
        try:
            file_path.rename(new_name)
            print(f"File {file_name} renamed to {new_name} successfully")
        except OSError as e:
            print(f"Error: {e}")
    else:
        print(f"File {file_path} does not exist")

def rename_directory(directory_name, new_name):
    directory_path = Path(directory_name)
    if directory_path.exists():
        try:
            directory_path.rename(new_name)
            print(f"Directory {directory_name} renamed to {new_name} successfully")
        except OSError as e:
            print(f"Error: {e}")
    else:
        print(f"Directory {directory_path} does not exist")
        
# def change_directory():
#     print(f"Текущий каталог: {os.getcwd()}")
#     new_directory = input("Введите новый путь каталога: ")
#     try:
#         os.chdir(new_directory)
#         print(f"Текущий каталог изменен на: {os.getcwd()}")
#     except FileNotFoundError:
#         print("Указанный каталог не существует")

def change_directory(destination):
    try:
        cwd = pathlib.Path.cwd()
        cwd = cwd / f"{destination}"
        print(f"Текущий каталог: {cwd}")
    except FileNotFoundError:
        print("Указанный каталог не существует")

def main_menu():
    while True:
        print("\nWelcome to File Management Program!")
        print("Please choose an option:")
        print("=========================================")
        print("1. List files in a directory")
        print("2. Create a new file")
        print("3. Create a new directory")
        print("4. Delete a file")
        print("5. Delete a directory")
        print("6. Rename a file or directory")
        print("7. Search files")
        print("8. Save current directory")
        print("9. Change directory")
        print("10. Edit file")
        print("0. Exit")
        print("=========================================")
        choice = input("Enter your choice: ")

        if choice == '1':
            directory = input("Enter directory path: ")
            list_files(directory)
        elif choice == '2':
            file_name = input("Enter file name: ")
            create_file(file_name)
        elif choice == '3':
            directory_name = input("Enter directory name: ")
            create_directory(directory_name)
        elif choice == '4':
            file_name = input("Enter file name: ")
            delete_file(file_name)
        elif choice == '5':
            directory_name = input("Enter directory name: ")
            delete_directory(directory_name)
        elif choice == '6':
            name = input("Enter name of file or directory: ")
            new_name = input("Enter new name: ")
            rename_file(name, new_name) if os.path.isfile(name) else rename_directory(name, new_name)
        elif choice == '7':
            search_directory = input("Введите путь каталога для поиска: ")
            search_term = input("Введите строку для поиска в названиях файлов: ") 
            search_files(search_term)
        elif choice == '8':
            current_directory = os.getcwd()
            save_current_directory(current_directory)
        elif choice == '9':
            new_directory = input("Введите новый путь каталога: ")
            change_directory(new_directory)
        elif choice == '10':
            file_path = input("Введите путь к файлу для редактирования: ")
            edit_file(file_path)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

def save_current_directory():
    current_directory = os.getcwd()
    with open('db.txt', 'w') as file:
        file.write(current_directory)



def search_files():
    search_directory = input("Введите путь каталога для поиска: ")
    search_term = input("Введите строку для поиска в названиях файлов: ")
    for root, dirs, files in os.walk(search_directory):
        for file in files:
            if search_term in file:
                print(os.path.join(root, file))

def edit_file():
    file_path = input("Введите путь к файлу для редактирования: ")
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        print(f"Содержимое файла:\n{content}")
        new_content = input("Введите новое содержимое файла: ")
        with open(file_path, 'w') as file:
            file.write(new_content)
        print("Содержимое файла успешно изменено")
    except FileNotFoundError:
        print("Указанный файл не существует")

if __name__ == "__main__":
    main_menu()
