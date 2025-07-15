# 🛠️ TechFlow Agile System

## 🎯 Objetivo do Projeto
Desenvolver um sistema de gerenciamento de tarefas utilizando metodologias ágeis, permitindo à startup cliente acompanhar o fluxo de trabalho em tempo real, priorizar tarefas críticas e monitorar o desempenho da equipe.

---

## 📦 Escopo
- CRUD básico de tarefas com título e prioridade.
- Campo de prioridade (`alta`, `normal`, `baixa`).
- Interface em linha de comando (terminal).
- Testes automatizados com `pytest`.
- Integração contínua com GitHub Actions.
- Gestão de tarefas usando Kanban (GitHub Projects).

---

## 🚀 Metodologia Adotada
A metodologia utilizada foi o **Kanban**, com tarefas organizadas nas colunas:

- A Fazer
- Em Progresso
- Concluído

> A aba **Projects** do GitHub foi usada para esse controle visual do fluxo.

---

## ⚙️ Como Executar o Sistema

### ✔️ Requisitos
- Python 3 instalado

### ▶️ Executar via terminal:
```bash
python src/app.py

✅ Testes Automatizados
Os testes estão localizados na pasta /tests

São executados automaticamente via GitHub Actions sempre que há um push no repositório.

🔁 Simulação de Mudança no Escopo
Durante o desenvolvimento, foi simulada uma mudança de escopo, conforme exigido no projeto:

Adição do campo prioridade às tarefas.

O código foi ajustado para suportar esse novo atributo.

O quadro Kanban foi atualizado com tarefas relacionadas a essa mudança.

Essa simulação representa a capacidade de adaptação a novos requisitos.

📊 Modelagem UML
Os diagramas foram criados com a ferramenta draw.io e estão disponíveis na pasta /docs.

📌 Diagrama de Casos de Uso


📌 Diagrama de Classes


👥 Autor
Guilherme da Lapa S.
GuILS00
GitHub

🧠 Reflexão Final
Este projeto simula na prática o desenvolvimento ágil de um sistema real, colocando em ação conhecimentos sobre:

Planejamento de tarefas

Controle de qualidade

Entrega contínua

Flexibilidade para mudanças no escopo

A experiência foi extremamente valiosa para aplicar os conceitos de Engenharia de Software com uma abordagem prática e moderna.

video no youtube
https://youtu.be/pO5QPp2mtxw
