from src import app

def test_create_task():
    app.tasks = []  # limpa as tarefas
    task = app.create_task("Teste", "alta")
    assert task["title"] == "Teste"
    assert task["priority"] == "alta"
    assert task["id"] == 1
