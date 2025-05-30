# 🗓️ API de Reservas - Microsserviço

Microsserviço responsável pela **reserva de salas de aula**, vinculado ao **ID da turma**. Desenvolvido como parte de um sistema educacional distribuído baseado em **arquitetura de microsserviços**.

---

## 🔗 Ecossistema de Microsserviços

Este microsserviço integra um sistema composto por três APIs:

- **📘 Sistema de Gerenciamento (API Principal)**  
  Cadastro e gerenciamento de alunos, professores e turmas.

- **🗓️ API de Reservas**  
  Controle das reservas de salas com base nas turmas cadastradas.

- **🧩 API de Atividades**  
  Gerenciamento de atividades vinculadas a professores.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10  
- Flask  
- SQLite  
- Docker  
- Padrão **MVC (Model-View-Controller)**

---

## 📁 Estrutura do Projeto

```
api-reservas/
├── controllers/
│   └── reserva_controller.py        # Lógica de negócio
├── models/
│   └── reserva_model.py             # Modelo de dados (Reserva)
├── routes/
│   └── reserva_route.py             # Rotas da API
├── database/
│   └── db.py                        # Conexão com SQLite
├── app.py                           # Arquivo principal
├── requirements.txt                 # Dependências
├── Dockerfile                       # Dockerfile para containerização
├── docker-compose.yml               # Orquestração de containers
└── README.md                        # Documentação da API
```

---

## 🚀 Como Executar com Docker

### 🔹 Subir com Docker Compose (junto à API Principal)

```bash
docker-compose up --build
```

### 🔹 Executar manualmente (isoladamente)

```bash
docker build -t api-reservas .
docker run -p 5001:5001 api-reservas
```

---

## 🔗 Endpoints Disponíveis

### 📥 POST `/reservas`
Cria uma nova reserva de sala vinculada a uma turma existente.

**Exemplo de JSON:**

```json
{
  "sala": "101",
  "data": "2024-06-15",
  "horario": "10:00",
  "id_turma": 1
}
```

**Respostas possíveis:**
- `201 Created`: Reserva criada com sucesso.
- `400 Bad Request`: Dados incompletos.
- `404 Not Found`: Turma não encontrada na API Principal.
- `500 Internal Server Error`: Erro interno ou de conexão.

---

### 📤 GET `/reservas`
Retorna todas as reservas cadastradas.

---

## 🔄 Integração com Sistema de Gerenciamento

Antes de criar uma reserva, a **API de Reservas** verifica se a turma está cadastrada na **API Principal** (`/turmas/<id_turma>`).

Essa validação é feita via requisição HTTP (`requests.get`), garantindo integridade no cadastro das reservas.

---

## 🧱 Arquitetura MVC

- **Model**  
  Define a estrutura e operações da tabela de reservas (`reserva_model.py`).

- **Controller**  
  Contém a lógica de negócio e integração com a API Principal (`reserva_controller.py`).

- **View (Rotas)**  
  Define os endpoints públicos da API (`reserva_route.py`).
