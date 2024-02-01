from tsk_mng_mod import TaskManager
import argparse

def main():
    parser = argparse.ArgumentParser(description="Скрипт для управления задачами")
    parser.add_argument("file", help="Файл с задачами в формате JSON")
    args = parser.parse_args()

    task_manager = TaskManager()
    try:
        task_manager.load_from_file(args.file)
        print("Задачи успешно загружены.")
    except FileNotFoundError:
        print("Файл с задачами не найден. Запись начнётся в новый файл.")

    while True:
        print("\n===== Меню менеджера задач =====")
        print("1. Добавить задачу")
        print("2. Изменить статус задачи")
        print("3. Посмтореть список задач")
        print("4. Очистить список задач")
        print("5. Сохранить и выйти")

        i = input("Что нужно сделать? (1-5): ")

        if i == "1":
            task_manager.add_task()

        elif i == "2":
            task_manager.change_task_status()

        elif i == "3":
            task_manager.view_tasks()

        elif i == "4":
            task_manager.clean_tasks()
            print("Список задач успешно очищен.")

        elif i == "5":
            task_manager.save_to_file(args.file)
            print(f"Задачи успешно сохранены. Завершение...")
            break

        else:
            print("Некорректный выбор действия.")

if __name__ == "__main__":
    main()
