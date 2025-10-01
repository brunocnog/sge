# 🧾 Sistema de Gestão de Estoque (SGE)

Este projeto foi desenvolvido durante o **Curso de Django da PycodeBR** com o objetivo de aplicar conceitos de desenvolvimento **Full Stack** com **Django**, consolidar boas práticas de modelagem de sistemas e criar um sistema completo de gestão de estoque — do CRUD ao dashboard com métricas e API com autenticação JWT.

> 📌 Este repositório foi publicado como parte do meu portfólio de aprendizado em **Django**.

---

## 📚 Sumário

* [Visão Geral](#-visão-geral)
* [Principais Funcionalidades](#-principais-funcionalidades)
* [Stack Utilizada](#-stack-utilizada)
* [Domínios do Sistema](#-domínios-do-sistema)
* [Dashboard & Métricas](#-dashboard--métricas)
* [Autenticação e Permissões](#-autenticação-e-permissões)
* [API REST](#-api-rest)
* [Coleção Postman](#-coleção-postman)
* [Configuração do Projeto](#-configuração-do-projeto)
* [Evolução do Projeto](#-evolução-do-projeto)
* [Licença](#-licença)

---

## 📝 Visão Geral

O **SGE - Sistema de Gestão de Estoque** permite o controle de marcas, categorias, fornecedores, produtos, entradas e saídas, além de apresentar dashboards dinâmicos com métricas e gráficos de vendas. O sistema foi desenvolvido de forma modular, utilizando **camadas bem definidas**, CRUD completo, paginação, filtros, autenticação, permissões de acesso e uma API REST com JWT.

---

## ✨ Principais Funcionalidades

* Cadastro e gerenciamento de:

  * ✅ Marcas
  * ✅ Categorias
  * ✅ Fornecedores
  * ✅ Produtos
  * ✅ Entradas e saídas de estoque
* Filtros avançados e busca em listagens
* Paginação de registros
* Atualização automática de inventário por meio de **signals**
* Dashboard com métricas e gráficos de vendas
* Sistema de autenticação e controle de permissões
* API REST autenticada com **JWT**

---

## 🧰 Stack Utilizada

* **Backend:** [Django 5.2.6](https://www.djangoproject.com/)
* **Frontend:** [Bootstrap](https://getbootstrap.com/) + Templates HTML
* **API:** [Django REST Framework](https://www.django-rest-framework.org/)
* **Autenticação da API:** [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
* **Outros:** Python 3.x, Virtualenv, Flake8 (boas práticas)

---

## 🧠 Domínios do Sistema

A arquitetura foi dividida em **apps (domínios)** independentes:

* `brands` → Marcas
* `categories` → Categorias
* `suppliers` → Fornecedores
* `products` → Produtos
* `inflows` → Entradas
* `outflows` → Saídas
* `authentication` → Login, Logout e JWT

Essa divisão facilita a manutenção, testes e escalabilidade do projeto.

---

## 📊 Dashboard & Métricas

O sistema conta com uma área administrativa visual que apresenta:

* Quantidade de produtos cadastrados
* Vendas e entradas nos últimos 7 dias
* Gráficos diários e agregados de vendas
* Métricas de estoque em tempo real

---

## 🔐 Autenticação e Permissões

* Login e Logout implementados com o sistema de autenticação padrão do Django.
* Permissões configuradas para grupos e usuários.
* Interface dinâmica conforme as permissões do usuário logado.
* Exemplo de usuário de visualização:

  ```
  user: user1
  senha: sge@1234
  ```

---

## 🌐 API REST

API desenvolvida com **Django REST Framework** e **JWT** para autenticação:

* Endpoints CRUD para todos os domínios (`brands`, `categories`, `products`, `suppliers`, `inflows`, `outflows`).
* Autenticação JWT com rotas de login, refresh e verificação de token.

---

### 🧪 Coleção Postman

Para facilitar os testes da API, disponibilizei a coleção **`SGE.postman_collection.json`** na raiz do repositório.
Você pode importá-la diretamente no [Postman](https://www.postman.com/) para explorar e testar todos os endpoints da aplicação de forma prática e organizada.

---

## ⚙️ Configuração do Projeto

### 1️⃣ Criar e ativar ambiente virtual

```bash
mkdir sge
cd sge
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 2️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 3️⃣ Aplicar migrações e criar superusuário

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 4️⃣ Rodar o servidor

```bash
python manage.py runserver
```

Acesse: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧭 Evolução do Projeto

O desenvolvimento seguiu uma trilha de **69 etapas** abordando desde:

* Modelagem de requisitos e domínios
* Criação das apps e templates base
* CRUD completo com filtros, paginação e detalhes
* Implementação de signals e métricas de estoque
* Dashboard e gráficos de vendas
* Sistema de login, logout e permissões
* Desenvolvimento de API REST com JWT
* Ajustes finais e boas práticas com Flake8

Essa estrutura reflete a **progressão natural de um sistema Django profissional**, servindo como excelente base para projetos futuros.

---

## 📄 Licença

Este projeto é de uso livre para fins de estudo e portfólio.
Sinta-se à vontade para clonar e adaptar às suas necessidades.

Os direitos sobre a criação e estrutura original do projeto pertencem ao **[Curso Django Master da PycodeBR](https://pycodebr.com.br/)**.
Este repositório foi desenvolvido como parte do meu processo de aprendizado, seguindo as aulas e práticas propostas no curso.