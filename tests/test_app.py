import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import app

from src import app

def test_soma():
    assert app.soma(2, 3) == 5

def test_create_task():
    app.tasks = []  # limpa as tarefas
    task = app.create_task("Teste", "alta")
    assert task["title"] == "Teste"
    assert task["priority"] == "alta"
    assert task["id"] == 1

