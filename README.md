# 📝 Microblog API - Backend

Esta API foi desenvolvida com **Python e Flask** como parte das atividades práticas da Sprint-01 (Desenvolvimento Full-Stack Básico) do curso de Pós-Graduação em Engenharia de Software. 

O objetivo é fornecer uma base funcional para gerenciamento de **postagens**, **comentários** e **curtidas** em um mini-blog, aplicando conceitos fundamentais de backend, autenticação e boas práticas de desenvolvimento.

---

## ⚙️ Estrutura do Projeto

```
api/
├── config/          # Configurações da aplicação e variáveis de ambiente
├── db/              # Conexão e inicialização do banco de dados
├── instance/        # Criado automaticamente para armazenar o SQLite
├── models/          # Definições dos modelos (Post, User, Comentário, etc.)
├── routes/          # Rotas da API (endpoints)
├── services/        # Lógicas de negócio e funcionalidades auxiliares
```

---

## 🚀 Como executar localmente

### ✅ Pré-requisitos
- Python 3.9+
- Git instalado

### 📦 Etapas de instalação

1. **Clone este repositório**

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd pos-puc/sprint-01/mvp/microblog/api
```

2. **Crie um ambiente virtual**

```bash
python -m venv venv
```

3. **Ative o ambiente virtual**

No Windows:
```bash
venv\Scripts\activate
```

No Linux/Mac:
```bash
source venv/bin/activate
```

4. **Instale as dependências**

```bash
pip install -r requirements.txt
```

> Se o arquivo `requirements.txt` ainda não existir, você pode criar um com os seguintes pacotes:

```txt
Flask
Flask-SQLAlchemy
flask-cors
flask-jwt-extended
flask-openapi3
flask-openapi3-swagger
flasgger
pyjwt
passlib[bcrypt]
python-dotenv
```

5. **Configure o ambiente** (opcional)

Crie um arquivo `.env` na raiz de `api/` com variáveis como:

```env
SECRET_KEY=sua_chave_secreta
DATABASE_URL=sqlite:///instance/database.db
```

6. **Execute o servidor**

```bash
flask run
```

> A aplicação estará disponível em: [http://localhost:5000](http://localhost:5000)

---

## 📚 Documentação da API

A documentação interativa estará disponível automaticamente via Swagger ou OpenAPI após o servidor iniciar. Acesse:

- Swagger UI: [http://localhost:5000/apidocs](http://localhost:5000/apidocs)
- OpenAPI Explorer (se configurado)

---

## 🧠 Tecnologias Utilizadas
- Python 3.9+
- Flask
- SQLAlchemy
- JWT para autenticação
- Swagger/OpenAPI para documentação
- CORS e Dotenv para suporte e configuração

---

📌 *Projeto desenvolvido para fins acadêmicos no curso de Pós-Graduação em Engenharia de Software - Sprint 01.*
