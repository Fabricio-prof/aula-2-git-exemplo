# Redis Dump Script

Este projeto contém um script em **Python** para realizar o **dump dos dados do Redis** em formato JSON.  
Ele percorre todas as chaves do banco, identifica o tipo de cada chave, coleta o valor e a TTL (tempo de expiração).

---

## 📌 Funcionalidades

- Conexão com Redis usando variáveis de ambiente.
- Suporte aos principais tipos de dados do Redis:
  - **string**
  - **hash**
  - **list**
  - **set**
  - **zset**
  - **stream**
- Exporta todos os dados em **JSON formatado** no `stdout`.

---

## ⚙️ Pré-requisitos

- **Python 3.8+**
- Biblioteca [redis-py](https://pypi.org/project/redis/)

Instalação das dependências:

```bash
pip install redis
