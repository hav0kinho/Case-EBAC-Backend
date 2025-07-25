# 🛍️ Huellysin Store - Catálogo de Produtos (Back-end)

Este é o back-end da aplicação **Huellysin Store**, um sistema de catálogo de produtos com painel administrativo, autenticação via JWT e controle de usuários. A API é construída com Django + Django REST Framework, e serve um front-end feito com React + Redux Toolkit.

---

## ⚙️ Tecnologias Utilizadas

- Python 3.11+
- Django 5
- Django REST Framework
- Simple JWT (Autenticação)
- CORS Headers
- SQLite (padrão, mas pode ser trocado)

---

## 📦 Funcionalidades

- API RESTful com endpoints organizados por rota
- Autenticação e registro de usuários via JWT
- CRUD completo de produtos e categorias (restrito a usuários autenticados)
- Catálogo público acessível sem autenticação
- Filtragem de produtos por categoria

---

## 📂 Organização do Projeto

```
catalogapp/
├── catalogapp/ # Configurações do projeto Django
├── categories/ # App de categorias
├── products/ # App de produtos
├── users/ # App de usuários (login e registro)
├── manage.py # Comando de execução do Django
└── requirements.txt # Dependências do projeto
```

---

## 🔐 Endpoints da API

| Rota                        | Tipo de Acesso     | Descrição                                    |
|-----------------------------|--------------------|----------------------------------------------|
| `/api/catalog/`             | Público            | Lista todos os produtos ativos              |
| `/api/catalog/?category=ID` | Público            | Lista produtos filtrados por categoria       |
| `/api/products/`            | Privado (JWT)      | CRUD de produtos                             |
| `/api/categories/`          | Privado (JWT)      | CRUD de categorias                           |
| `/api/register/`            | Público            | Criação de novos usuários                    |
| `/api/login/`               | Público            | Login com JWT                                |

---

## 🧪 Execução Local

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/huellysin-store-backend.git
cd huellysin-store-backend
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
### 4. Execute as migrações

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
### 5. Rode o servidor local

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

---

## 🔑 Autenticação JWT

O projeto utiliza o pacote `SimpleJWT` para autenticação.

Ao fazer login `(/api/login/)`, um par de tokens é retornado `(access e refresh)`.

O token `access` deve ser enviado no header `Authorization` como: `Authorization: Bearer <seu_token>`

--- 

## 🔗 Front-end
Este back-end se conecta ao front-end React disponível neste repositório:

👉 [Repositório do Back-end](https://github.com/hav0kinho/Case-EBAC-Frontend)

---

## 📩 Contato

Desenvolvido por **Ruallyson Felype Travassos de Moura** para um Case Técnico :D  
📧 [ruallysonfelype@gmail.com]