🗓️ API de Reservas - Microsserviço
Microsserviço responsável pela reserva de salas de aula, vinculado ao ID da turma. Desenvolvido como parte de um sistema educacional baseado em arquitetura de microsserviços.

🔗 Ecossistema de Microsserviços
Este microsserviço integra um sistema composto por três APIs:

Sistema de Gerenciamento (API Principal): Cadastro e gerenciamento de alunos, professores e turmas.

API de Reservas: Controle das reservas de salas de aula com base nas turmas cadastradas.

API de Atividades: Gerenciamento de atividades vinculadas a professores.

🛠️ Tecnologias Utilizadas
Python 3.10

Flask

SQLite

Docker

Padrão MVC (Model-View-Controller)

📁 Estrutura do Projeto
bash
api-reservas/
├── controllers/
│   └── reserva_controller.py       # Lógica de negócio
├── models/
│   └── reserva_model.py            # Modelo de dados (Reserva)
├── routes/
│   └── reserva_route.py            # Rotas da API
├── database/
│   └── db.py                       # Conexão com SQLite
├── app.py                          # Arquivo principal
├── requirements.txt                # Dependências
├── Dockerfile                      # Dockerfile para containerização
├── docker-compose.yml              # Orquestração de containers
└── README.md                       # Documentação da API
🚀 Como Executar com Docker
🔹 Subir com Docker Compose
bash
docker-compose up --build
🔹 Executar manualmente
bash
docker build -t api-reservas .
docker run -p 5001:5001 api-reservas
🔗 Endpoints Disponíveis
GET /reservas
Retorna todas as reservas cadastradas.

POST /reservas
Cria uma nova reserva vinculada a uma turma existente.

🧾 Exemplo de JSON para POST:
json
{
  "sala": "101",
  "horario": "10:00",
  "turma_id": 1
}
🔄 Integração com Sistema de Gerenciamento
A API de Reservas depende do ID da turma, fornecido pela API Principal (Sistema de Gerenciamento).

Antes de criar uma reserva, a turma deve estar cadastrada.

Essa integração ocorre por meio do campo turma_id.

🧱 Arquitetura MVC
Model: Define a estrutura da tabela de reservas (reserva_model.py)

Controller: Contém a lógica de criação e listagem (reserva_controller.py)

View (Rotas): Define os endpoints públicos da API (reserva_route.py)
