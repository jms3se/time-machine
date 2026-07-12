# Time Machine

Time Machine é uma API REST desenvolvida em Python com Flask para gerenciar registros de tempo, organizar atividades por projeto e etiqueta, e servir como base para uma futura plataforma de produtividade pessoal ou empresarial.

O projeto foi concebido para explorar a construção de uma aplicação backend com autenticação, persistência relacional, relacionamento entre entidades e uma estrutura modular que facilita evolução e manutenção.

## Propósito do projeto

A ideia central do Time Machine é oferecer uma solução simples e flexível para:

- registrar blocos de tempo associados a uma tarefa ou atividade;
- organizar esses registros por categorias, como tags e projetos;
- criar uma base sólida para futuras funcionalidades de acompanhamento de produtividade, relatórios e gestão de equipes.

Em termos mais práticos, o projeto simula um sistema de controle de tempo com foco em organização, rastreio e escalabilidade.

## Principais funcionalidades

- Autenticação de usuários com JWT;
- Cadastro, login e logout;
- CRUD de timers (registros de tempo);
- CRUD de tags;
- CRUD de projetos;
- Relacionamento entre timers, tags e projetos;
- Estrutura de API REST com respostas JSON padronizadas;
- Configuração local com Docker Compose para serviços como PostgreSQL e Redis.

## Stack tecnológica

- Python 3.8+
- Flask
- Flask RESTful
- Flask-SQLAlchemy
- Flask-Marshmallow
- Flask-Migrate
- Flask-JWT-Extended
- PostgreSQL
- Redis
- Docker Compose
- Sentry para monitoramento de erros

## Arquitetura do projeto

A aplicação segue uma organização modular, separando responsabilidades entre camadas:

- src/server.py: inicialização da aplicação Flask;
- src/routes: definição dos endpoints por domínio;
- src/resources: implementação das operações HTTP;
- src/schemas: serialização e validação de dados;
- src/models: entidades do banco de dados;
- src/repositories: abstração para acesso e persistência de dados;
- src/config.py: configuração de ambiente e variáveis da aplicação;
- migrations: versionamento do banco com Alembic.

Essa estrutura facilita a manutenção do código e a expansão do projeto com novos módulos e recursos.

## Estrutura de diretórios

```text
src/
  config.py
  server.py
  models/
  repositories/
  resources/
  routes/
  schemas/
  utils/
```

## Como executar localmente

1. Clone o repositório.
2. Instale as dependências com o ambiente virtual de sua preferência.
3. Suba os serviços de banco e cache com Docker Compose.
4. Configure as variáveis de ambiente necessárias para a aplicação.
5. Execute a aplicação a partir do diretório principal.

Exemplo de fluxo de execução:

```bash
pipenv install
docker-compose up -d
python src/server.py
```

## Visão de evolução

Este projeto ainda está em evolução e pode crescer para incluir recursos como:

- recuperação de senha e confirmação por e-mail;
- exportação e importação de dados;
- perfil do usuário e edição de dados pessoais;
- suporte a equipes e permissões;
- relatórios e análise de produtividade;
- melhorias de segurança e conformidade.

## Destaques para portfólio

Este repositório demonstra habilidades relevantes para um perfil backend, incluindo:

- construção de APIs REST com Flask;
- modelagem de entidades relacionais;
- implementação de autenticação e proteção de rotas;
- uso de migrações de banco de dados;
- organização de código em camadas;
- preparação para evolução em direção a um produto mais completo.

## Licença

Este projeto é um estudo técnico e pode ser utilizado como referência para aprendizado, experimentação e desenvolvimento posterior.
