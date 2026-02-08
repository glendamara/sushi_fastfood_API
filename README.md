# 🍱 Sushi Fast Food - Backend API

Esta é uma API REST simples desenvolvida para gerenciar o cardápio de um serviço de fast-food japonês. O projeto foi criado para servir como base de estudos sobre integração entre back-end e front-end, focado em rotas de consulta de produtos.

## 🚀 Tecnologias Utilizadas

* **Python 3**: Linguagem base.
* **Flask**: Micro-framework para web.
* **Flask-CORS**: Para permitir o acesso do front-end (React/Next.js).

## 🛠️ Como rodar o projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
   cd nome-do-repositorio

Crie um ambiente virtual (opcional):
Bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

Instale as dependências:Bashpip install flask flask-cors
Execute a aplicação:Bashpython app.py
A API estará disponível em http://127.0.0.1:5000.

Método,Endpoint,Descrição
GET,/api/menu,
Retorna a lista completa de itens do cardápio.
GET,/menu/<id>,
Retorna os detalhes de um item específico baseado no ID.

