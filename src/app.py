tasks = []

def create_task(title, priority="normal"):
    task = {"id": len(tasks) + 1, "title": title, "priority": priority}
    tasks.append(task)
    return task

def read_tasks():
    return tasks

def update_task(task_id, title=None, priority=None):
    for task in tasks:
        if task["id"] == task_id:
            if title:
                task["title"] = title
            if priority:
                task["priority"] = priority
            return task
    return None

def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]

if __name__ == "__main__":
    print("Sistema de Tarefas Ágeis\n")

    create_task("Escrever README")
    create_task("Configurar GitHub Actions", "alta")
    print("📋 Tarefas:", read_tasks())

    update_task(1, "Atualizar README.md")
    delete_task(2)

    print("📋 Tarefas após atualizações:", read_tasks())

