# Construindo um Projeto Ágil no GitHub: Da Gestão ao Controle de Qualidade

## 🎯 Objetivo do Projeto
Desenvolver um sistema de gerenciamento de tarefas utilizando metodologias ágeis, permitindo à startup cliente acompanhar o fluxo de trabalho em tempo real, priorizar tarefas críticas e monitorar o desempenho da equipe.

## 📦 Escopo
- CRUD básico de tarefas
- Campo de prioridade
- Interface em linha de comando (terminal)
- Integração com testes automatizados

## 🚀 Metodologia Adotada
A metodologia usada foi o **Kanban**, implementado usando a aba **Projects** do GitHub. As tarefas foram organizadas nas colunas:
- A Fazer
- Em Progresso
- Concluído

## ⚙️ Como Executar
Requisitos: Python 3 instalado

```bash
python src/app.py

✅ Testes Automatizados
Os testes são executados automaticamente via GitHub Actions ao fazer push no repositório. Os testes estão localizados na pasta tests.

🔁 Mudança no Escopo
Durante o desenvolvimento, foi simulada uma mudança de escopo solicitada pelo cliente, que incluiu a adição de prioridade nas tarefas. O CRUD foi ajustado para aceitar esse novo atributo.

📊 Diagramas UML
Os diagramas de Casos de Uso e Classes estão disponíveis na pasta /docs, criados com a ferramenta draw.io.

Guilherme L. dos Santos (GuILS00)

