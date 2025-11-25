# Gen N Ver – Biblioteca Python para Geração e Validação de Dados Fictícios

**Gen N Ver** é uma biblioteca Python simples, didática e sem dependências externas, criada para gerar dados fictícios comuns em sistemas reais, como:

- nomes (completo, primeiro nome e sobrenome)  
- e-mails fictícios  
- nomes de usuário (username)  
- senhas configuráveis  

Além disso, oferece **validadores de e-mail, senha e username**, com suporte a regras configuráveis.

A biblioteca é ideal para:

- testes de software  
- protótipos  
- atividades acadêmicas  
- geração de massa de dados  
- simulações  
- preenchimento automático de campos  

---

# Instalação (via TestPyPI)

```bash
pip install -i https://test.pypi.org/simple/ gen-n-ver
```

Após instalar, importe normalmente:

```python
from gen_n_ver import *
```

---

# Funcionalidades

A biblioteca é composta por dois conjuntos principais:

### **1. Geradores**
| Função | Descrição |
|--------|-----------|
| `gerar_primeiro_nome()` | Gera somente o primeiro nome. |
| `gerar_sobrenome()` | Gera somente o sobrenome. |
| `gerar_nome_completo()` | Gera nome + sobrenome. |
| `gerar_usuario(nome, ...)` | Gera um username baseado em um nome. |
| `gerar_email(nome, dominio)` | Gera um e-mail fictício. |
| `gerar_senha(...)` | Gera uma senha configurável. |

### **2. Validadores**
| Função | Descrição |
|--------|-----------|
| `validar_email(email)` | Verifica se o e-mail segue regras básicas. |
| `validar_usuario(usuario)` | Checa mínimo/máximo e caracteres permitidos. |
| `validar_senha(senha, ...)` | Valida a força da senha. |

---

# Documentação Completa das Funções

A seguir estão todas as funções disponíveis, seus parâmetros e exemplos de uso.

---

## **1. Geração de Nomes**

---

### `gerar_primeiro_nome()`

**Retorno:** `str`  
Gera um primeiro nome aleatório.

**Exemplo:**
```python
nome = gerar_primeiro_nome()
print(nome)  # ex.: "Camila"
```

---

### `gerar_sobrenome()`

**Retorno:** `str`  
Gera um sobrenome aleatório.

**Exemplo:**
```python
sob = gerar_sobrenome()
print(sob)  # ex.: "Oliveira"
```

---

### `gerar_nome_completo()`

**Retorno:** `str`  
Gera nome + sobrenome.

**Exemplo:**
```python
nome = gerar_nome_completo()
print(nome)  # "Lucas Almeida"
```

---

# **2. Geração de Username**

---

### `gerar_usuario(nome, tamanho_minimo=5, tamanho_maximo=12)`

**Parâmetros:**

| Parâmetro | Tipo | Descrição |
|----------|------|------------|
| `nome` | `str` ou `None` | Nome base para gerar o usuário. Se `None`, a função gera automaticamente. |
| `tamanho_minimo` | `int` | Tamanho mínimo do username. |
| `tamanho_maximo` | `int` | Tamanho máximo do username. |

**Erros Tratados:**
- `TypeError` se `nome` não for string ou None  
- `ValueError` se `tamanho_maximo < tamanho_minimo`  

**Exemplo:**
```python
usuario = gerar_usuario("Lara Souza")
print(usuario)  # "larasouza23"
```

---

# **3. Geração de Email**

---

### `gerar_email(nome, dominio="exemplo.com")`

**Parâmetros:**

| Parâmetro | Tipo | Descrição |
|----------|------|------------|
| `nome` | `str` ou `None` | Nome base. |
| `dominio` | `str` | Deve conter **apenas a parte após o @** (ex.: `"gmail.com"`). |

**Erros Tratados:**
- `TypeError` se nome não for string  
- `ValueError` se domínio tiver `@`  
- `ValueError` se domínio não possuir ponto  

**Exemplo:**
```python
email = gerar_email("Carlos Pereira", dominio="teste.com")
print(email)  # "carlospereira91@teste.com"
```

---

# **4. Geração de Senha**

---

### `gerar_senha(tamanho=10, usar_minusculas=True, usar_maiusculas=True, usar_digitos=True, usar_especiais=True, minimo_minusculas=None, minimo_maiusculas=None, minimo_digitos=None, minimo_especiais=None)`

**Parâmetros principais:**

| Parâmetro | Tipo | Descrição |
|----------|------|------------|
| `tamanho` | `int` | Tamanho total da senha. |
| `usar_minusculas` | `bool` | Incluir letras minúsculas? |
| `usar_maiusculas` | `bool` | Incluir letras maiúsculas? |
| `usar_digitos` | `bool` | Incluir números? |
| `usar_especiais` | `bool` | Incluir símbolos especiais? |
| `minimo_*` | `int` ou `None` | Mínimo de cada tipo de caractere. |

**Erros Tratados:**
- `ValueError` se tamanho <= 0  
- `ValueError` se mínimos forem negativos  
- `ValueError` se nenhum tipo de caractere estiver habilitado  
- `ValueError` se soma dos mínimos > tamanho  

**Exemplo:**
```python
senha = gerar_senha(
    tamanho=12,
    minimo_especiais=2,
    usar_especiais=True
)

print(senha)   # Ex.: "Ab9#!ks82X@1"
```

---

# **5. Validadores**

---

## `validar_email(email)`

**Retorno:** `True` ou `False`  
**Erros Tratados:** `TypeError` se email não for string

**Regras:**
- deve conter `@`
- deve ter domínio com pelo menos 1 ponto

**Exemplo:**
```python
print(validar_email("teste@gmail.com"))  # True
```

---

## `validar_usuario(usuario, tamanho_minimo=3, tamanho_maximo=15)`

**Erros Tratados:**
- `TypeError` se usuário não for string  
- `ValueError` se tamanhos forem inválidos  

**Exemplo:**
```python
print(validar_usuario("joaosilva"))  # True
```

---

## `validar_senha(senha, tamanho_minimo=8, exigir_minusculas=True, exigir_maiusculas=True, exigir_digitos=True, exigir_especiais=False)`

**Erros Tratados:**
- `TypeError` se senha não for string
- `ValueError` se tamanho_minimo <= 0

**Exemplo:**
```python
validar_senha("Senha123!")  # True
```

---

# Tratamento de Erros

A biblioteca implementa validações para garantir uso seguro.  
Ela pode levantar:

- `TypeError`
- `ValueError`

Exemplos de erros tratados:

```python
gerar_usuario(123)        # TypeError
gerar_email("Lara", "a@b") # ValueError
gerar_senha(tamanho=-3)   # ValueError
```

---

# Exemplo Completo

```python
from gen_n_ver import *

nome = gerar_nome_completo()
email = gerar_email(nome)
usuario = gerar_usuario(nome)
senha = gerar_senha(tamanho=12, minimo_especiais=1)

print(nome)
print(email)
print(usuario)
print(senha)

print(validar_email(email))
print(validar_usuario(usuario))
print(validar_senha(senha))
```

---

# Licença

Uso livre para fins educacionais.

---

