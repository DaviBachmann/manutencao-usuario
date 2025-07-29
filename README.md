# manutencao-usuarios

Sistema automatizado em Python para **criação e desativação padronizada de usuários administradores** nas bases da empresa.

---

## 📌 Descrição Geral

Este projeto foi desenvolvido com o objetivo de **facilitar e padronizar a gestão de usuários nas bases de dados** da empresa. A ferramenta automatiza as tarefas de criação e desativação de usuários administradores em múltiplas bases, utilizando parâmetros definidos pelo operador.

A solução contribui diretamente para:
- **Praticidade** na criação de acessos administrativos.
- **Segurança** ao evitar usuários ativos indevidamente.
- **Padronização** nos nomes e senhas dos usuários criados.

---

## ⚙️ Funcionalidades

- 🗃️ Criação automática de usuários em múltiplas bases simultaneamente.
- 🔒 Desativação de usuários de forma rápida e segura.
- 📝 Padronização de login e senha conforme regras internas.

---

💡 Resenha do Projeto

Desenvolvimento de uma aplicação em Python para padronizar e automatizar o processo de criação e desativação de usuários administradores nas bases da empresa. 

O projeto surgiu a partir da necessidade de aumentar a segurança e a praticidade na gestão de acessos administrativos, evitando processos manuais e propensos a falhas. 
Com o QG, é possível criar rapidamente um usuário com o mesmo login e senha em múltiplas bases, garantindo consistência e economia de tempo. 

Além disso, a funcionalidade de desativação centralizada permite encerrar acessos de forma ágil e padronizada, o que contribui diretamente para a redução de riscos de segurança — especialmente em casos onde o desligamento do colaborador exige ação imediata. 
A ferramenta proporciona mais controle, padronização e segurança no ambiente corporativo, sendo uma solução eficiente e reutilizável para times de suporte, infraestrutura ou segurança da informação.

---

## 🚀 Exemplo de Uso

### 🔹 Criação de Usuários

O operador executa o script e informa:
- Nome de usuário a ser criado
- Senha padrão
- Ambiente desejado (produção, homologação etc.)

A aplicação:
- Conecta-se automaticamente às bases definidas
- Cria o usuário em cada uma, se não existir
- Aplica a senha padrão definida
- Retorna relatório de sucesso/erro

### 🔹 Desativação de Usuários

O operador:
- Informa o login do usuário a ser removido

A aplicação:
- Conecta-se às bases
- Desativa o acesso do usuário em todas elas
- Gera relatório de confirmação

---

## 🪄 Tecnologias Utilizadas

- **Python**
- **SQL Server**
- **pyodbc** (para conexão com SQL Server)
- **dotenv** (para leitura de variáveis de ambiente)

---

## ✅ Destaques do Projeto

- Padronização automática de login e senha para usuários administradores.
- Execução simultânea de ações em diversas bases, garantindo agilidade e consistência.
- Centralização do controle de acessos, evitando erros manuais e atrasos operacionais.
- Facilidade para desativar acessos de ex-colaboradores, contribuindo diretamente para a segurança da informação.
- Código modular e reutilizável, permitindo expansão futura para outros tipos de usuários ou permissões.

---

> Projeto criado por [Davi Bachmann](https://github.com/DaviBachmann) — Cientista de Dados em formação, com foco em automação, dados e performance.
