#API de Reservas - Sistema de Gestão Escolar

Este microsserviço ´responsável pela reserva de salas de aula, sendo parte integrada de um sistema educacional composto por três APIs:
1) Sistema de Gerencionamento (API Principal) _ Cadastro e gerencimento de alunos, professores e turmas.
2) API de Reserva - Controle de reservas de  salas vinculadas ao ID da turma.
3) API de Atividades - Controle de atividades vinculadas ao ID do professor.

#Tecnologias Utilizadas
-Python 3.10
-Flask
-SQLite
-Docker
-Padrão MVC (Model-View-Controller)

#Estrutura do Projeto
api-reservas/
│
├── controllers/
│   └── reserva_controller.py       # Lógica de negócio
│
├── models/
│   └── reserva_model.py            # Modelo de dados (Reserva)
│
├── routes/
│   └── reserva_route.py            # Rotas da API
│
├── database/
│   └── db.py                       # Conexão com SQLite
│
├── app.py                          # Arquivo principal da aplicação
├── requirements.txt                # Dependências do projeto
├── Dockerfile                      # Dockerfile para containerizar a aplicação
├── docker-compose.yml              # Composição e execução dos serviços
└── README.md                       # Documentação da API

#Integração com o sistema de gerenciamento
Essa API depende do ID da turma fornecido pela API de Sistemas de Gerenciamento. Ou seja:
-Antes de criar uma reserva, a turma precisa existir no sistema principal.
-Essa relação é feita via campo turma_id

#Arquitetura(MVC)
Model: Define a estrutura dos dados(reserva_model.py)
View: Interface com o usuário via rotas HTTP(reserva_route.py)
Controller: Lógica de negócio(reserva_controller.py)

