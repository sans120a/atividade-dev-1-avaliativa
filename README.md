# Projeto Avaliativo DEV-1

É o sistema de uma biblioteca usando django, rest framework e tokens jwt.

## Instruções de instalação e execução do ambiente:
``` shell
# clone os arquivos do repositório.
git clone https://github.com/sans120a/atividade-dev-1-avaliativa.git
cd atividade-dev-1-avaliativa

# realize as instalações e preparação do venv.
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

# faça o migrate para o banco de dados, crie um usuário e faça e inicie o servidor.
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Lista de Endpoints:
### Endpoint do annotate:
| Método | Link | Descrição |
|--------|------|-----------|
| GET | http://127.0.0.1:8000/api/livros/ranking/ | Mostra um ranking de livros baseado no numero de impréstimos |

### Endpoint geral:
| Método | Link | Descrição |
|--------|------|-----------|
| GET | http://127.0.0.1:8000/api/ | Lista os endpoints ligados a ele |


### Endpoints de Livro:
| Método | Link | Descrição |
|--------|------|-----------|
| GET |  http://127.0.0.1:8000/api/livros/ | Lista todos os livros |
| POST | http://127.0.0.1:8000/api/livros/ | Cria um novo livro |
| GET | http://127.0.0.1:8000/api/livros/{id}/ | Mostra os dados de um livro específico |
| PUT | http://127.0.0.1:8000/api/livros/{id}/ | Atualiza todos os dados de um livro |
| PATCH | http://127.0.0.1:8000/api/livros/{id}/ | Atualiza alguns dados de um livro |
| DELETE | http://127.0.0.1:8000/api/livros/{id}/ | Remove o livro do sistema |

### Endpoints de Usuário:
| Método | Link | Descrição |
|--------|------|-----------|
| GET | http://127.0.0.1:8000/api/usuarios/ | Lista todos os usuários |
| POST | http://127.0.0.1:8000/api/usuarios/ | Cria um novo usuário |
| GET | http://127.0.0.1:8000/api/usuarios/{id}/ | Mostra os dados de um usuário específico |
| PUT | http://127.0.0.1:8000/api/usuarios/{id}/ | Atualiza todos os dados de um usuário |
| PATCH | http://127.0.0.1:8000/api/usuarios/{id}/ | Atualiza alguns dados de um usuário |
| DELETE | http://127.0.0.1:8000/api/usuarios/{id}/ | Remove o usuário do sistema |

### Endpoints de Empréstimo (Classe Protegida):
| Método | Link | Descrição |
|--------|------|-----------|
| GET | http://127.0.0.1:8000/api/emprestimos/ | Lista todos os empréstimos |
| POST | http://127.0.0.1:8000/api/emprestimos/ | Cria um novo empréstimo |
| GET | http://127.0.0.1:8000/api/emprestimos/{id}/ | Mostra os dados de um empréstimo específico |
| PUT | http://127.0.0.1:8000/api/emprestimos/{id}/ | Atualiza todos os dados de um empréstimo |
| PATCH | http://127.0.0.1:8000/api/emprestimos/{id}/ | Atualiza alguns dados de um empréstimo |
| DELETE | http://127.0.0.1:8000/api/emprestimos/{id}/ | Remove o empréstimo do sistema |


### Endpoints de Categoria:
| Método | Link | Descrição |
|--------|------|-----------|
| GET | http://127.0.0.1:8000/api/categorias/ | Lista todas as categorias |
| POST | http://127.0.0.1:8000/api/categorias/ | Cria uma nova categoria |
| GET | http://127.0.0.1:8000/api/categorias/{id}/ | Mostra os dados de uma categoria específica |
| PUT | http://127.0.0.1:8000/api/categorias/{id}/ | Atualiza todos os dados de uma categoria |
| PATCH | http://127.0.0.1:8000/api/categorias/{id}/ | Atualiza alguns dados de uma categoria |
| DELETE | http://127.0.0.1:8000/api/categorias/{id}/ | Remove a categoria do sistema |

### Endpoint de Autor:
| Método | Link | Descrição |
|--------|------|-----------|
| GET | http://127.0.0.1:8000/api/autores/ | Lista todos os autores |
| POST | http://127.0.0.1:8000/api/autores/ | Cria um novo autor |
| GET | http://127.0.0.1:8000/api/autores/{id}/ | Mostra os dados de um autor |
| PUT | http://127.0.0.1:8000/api/autores/{id}/ | Atualiza todos os dados de um autor |
| PATCH | http://127.0.0.1:8000/api/autores/{id}/ | Atualiza alguns dados de um autor |
| DELETE | http://127.0.0.1:8000/api/autores/{id}/ | Remove o autor do sistema |

### Endpoints de Token:
| Método | Link | Descrição |
|--------|------|-----------|
| POST | http://127.0.0.1:8000/api/token/ | gera um token válido por 5 minutos |
| POST | http://127.0.0.1:8000/api/token/refresh/ | faz um token que já passou do período válido se tornar válido novamente |

## Exemplos de Corpo de Requisição/Resposta:
### Resposta do annotate:
``` JSON
[
    {
        "id": 1,
        "titulo": "Teste",
        "total_emprestimos": 1
    }
]
```

### Resposta do api geral:
``` JSON
{
    "livros": "http://127.0.0.1:8000/api/livros/",
    "usuarios": "http://127.0.0.1:8000/api/usuarios/",
    "emprestimos": "http://127.0.0.1:8000/api/emprestimos/",
    "categorias": "http://127.0.0.1:8000/api/categorias/",
    "autores": "http://127.0.0.1:8000/api/autores/"
}
```

### Resposta de livro:
``` JSON
[
    {
        "id": 1,
        "isbn": "123456789",
        "titulo": "Teste",
        "sinopse": "Teste de sinopse",
        "paginas": 1000,
        "disponivel": false,
        "data_publicacao": "2026-09-01",
        "categoria": 1,
        "autor": [
            1
        ]
    }
]
```

### Requisição de livro:
``` JSON
{
    "isbn": "123456789",
    "titulo": "Teste",
    "sinopse": "Teste de sinopse",
    "paginas": 1000,
    "disponivel": false,
    "data_publicacao": "2026-09-01",
    "categoria": 1,
    "autor": [1]
}
```

### Resposta de usuário:
``` JSON
[
    {
        "id": 1,
        "nome": "Haian",
        "idade": 19,
        "cpf": "12345678912"
    }
]
```

### Requisição de usuário:
``` JSON
{
    "nome": "Haian",
    "idade": 19,
    "cpf": "12345678912"
}

```

### Resposta de empréstimo:
``` JSON
{
    "id": 1,
    "livro": {
        "id": 1,
        "isbn": "123456789",
        "titulo": "Teste",
        "sinopse": "Teste de sinopse",
        "paginas": 1000,
        "disponivel": false,
        "data_publicacao": "2026-09-01",
        "categoria": 1,
        "autor": [
            1
        ]
    },
    "usuario_detalhes": {
        "id": 1,
        "nome": "Haian",
        "idade": 19,
        "cpf": "12345678912"
    },
    "data_realizada": "2026-10-01",
    "data_devolucao": "2026-12-30",
    "devolvido": false,
    "usuario": 1
}
```

### Requisição de empréstimo:
``` JSON
{
    "livro_id": 1,
    "usuario": 1,
    "data_devolucao": "2026-12-30",
    "devolvido": false
}
```

### Resposta de categoria:
``` JSON
[
    {
        "id": 1,
        "genero": "Teste"
    }
]
```

### Requisição de categoria:
``` JSON
{
    "genero": "Teste"
}
```

### Resposta de autor:
``` JSON
[
    {
        "id": 1,
        "nome": "Testador",
        "nacionalidade": "Teste"
    }
]
```

### Requisição de autor:
``` JSON
{
    "nome": "Testador",
    "nacionalidade": "Teste"
}
```

### Resposta de token:
``` JSON
{
    "refresh": "{Token de Refresh}",
    "access": "{Token de acesso}"
}
```

### Requisição de token:
``` JSON
{
    "username": "{Usuario}",
    "password": "{Senha}"
}
```
