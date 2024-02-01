import json
from datetime import datetime


class Task:
    def __init__(self, name, description, status, creation_date=None, updating_date=None):
        self.name = name
        self.description = description
        self.status = status
        self.creation_date = creation_date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updating_date = updating_date or self.creation_date

    def to_dict(self):
        return {
            "название": self.name,
            "описание": self.description,
            "статус": self.status,
            "дата создания": self.creation_date.strftime("%Y-%m-%d %H:%M:%S"),
            "дата изменения статуса": self.updating_date.strftime("%Y-%m-%d %H:%M:%S"),
        }

    @staticmethod
    def from_dict(data):
        name = data["название"]
        description = data["описание"]
        status = data["статус"]
        creation_date = datetime.strptime(data["дата создания"], "%Y-%m-%d %H:%M:%S")
        updating_date = datetime.strptime(data["дата изменения статуса"], "%Y-%m-%d %H:%M:%S")

        return Task(name, description, status, creation_date, updating_date)


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        name = input("Введите название задачи: ")
        description = input("Введите описание задачи: ")
        creation_date = datetime.now().replace(microsecond=0)
        updating_date = datetime.now().replace(microsecond=0)
        task = Task(name, description, "новая", creation_date, updating_date)
        self.tasks.append(task)
        print("Задача успешно добавлена")

    def change_task_status(self):
        task_name = input("Введите название задачи: ")
        flag = 0
        for task in self.tasks:
            if task.name == task_name:
                new_status = input("Введиет новый статус (новая, выполняется, ревью, выполнено, отменено): ")
                if new_status in ["новая", "выполняется", "ревью", "выполнено", "отменено"]:
                    task.status = new_status
                    task.updating_date = datetime.now().replace(microsecond=0)
                    print(f"Статус задачи успешно изменён на '{new_status}'")
                else:
                    print("Такой статус недоступен.")
                flag = 1
        if flag == 0:
            print(f"Задачи с названием {task_name} не найдено")

    def view_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
        else:
            for task in self.tasks:
                print(f"\nназвание: {task.name}")
                print(f"описание: {task.description}")
                print(f"статус: {task.status}")
                print(f"дата создания: {task.creation_date}")
                print(f"дата изменения статуса: {task.updating_date}")

    def save_to_file(self, filename):
        data = [task.to_dict() for task in self.tasks]
        with open(filename, "w", encoding="utf-8") as file:
            jsonstr = json.dumps(data, ensure_ascii=False, indent=2)
            file.write(jsonstr)
    def load_from_file(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.tasks = [Task.from_dict(task) for task in data]

    def clean_tasks(self):
        self.tasks = []
