import random
import string

LISTA_PRIMEIROS_NOMES = [
    "Lara", "Alice", "Arthur", "João", "Bárbara", "Beatriz", "Pedro",
    "Lucas", "Rafael", "Paulo", "Fernanda", "Thiago", "Camila",
]

LISTA_SOBRENOMES = [
    "Silva", "Souza", "Oliveira", "Santos", "Pereira",
    "Costa", "Almeida", "Rodrigues", "Gomes", "Barbosa",
]

LISTA_DOMINIOS_EMAIL = [
    "exemplo.com",
    "email.com",
    "teste.com",
    "mail.com",
]


def gerar_primeiro_nome() -> str:
    """
    Retorna um primeiro nome.

    Exemplo de chamada:
        gerar_primeiro_nome()

    Retorno:
        'Lara'
    """
    return random.choice(LISTA_PRIMEIROS_NOMES)


def gerar_sobrenome() -> str:
    """
    Retorna apenas um sobrenome.

    Exemplo de chamada:
        gerar_sobrenome()

    Retorno:
        'Silva'
    """
    return random.choice(LISTA_SOBRENOMES)


def gerar_nome_completo() -> str:
    """
    Retorna um nome completo falso no formato 'Nome Sobrenome'.

    Exemplo de chamada:
        gerar_nome_completo()

    Retorno:
        'João Souza'
    """
    return f"{gerar_primeiro_nome()} {gerar_sobrenome()}"


def _normalizar_usuario(texto: str) -> str:
    """
    Transforma um texto em um formato aceitável para username:
    - deixa tudo minúsculo
    - remove espaços
    - mantém apenas letras e números

    Exemplo interno (não deve ser chamada diretamente):
        _normalizar_usuario("Lara Silva") -> "larasilva"
    """
    texto = texto.lower()
    permitidos = string.ascii_lowercase + string.digits
    return "".join(ch for ch in texto if ch in permitidos or ch == " ").replace(" ", "")


def gerar_usuario(
    nome: str | None = None,
    tamanho_minimo: int = 6,
    tamanho_maximo: int = 12,
) -> str:
    """
    Gera um nome de usuário falso.

    Parâmetros:
        nome (opcional):
            Se informado, o username será baseado nesse nome.
            Se não informado, será usado um nome completo aleatório.

        tamanho_minimo:
            Quantidade mínima de caracteres no username.

        tamanho_maximo:
            Quantidade máxima de caracteres permitidos.

    Exemplo de chamada:
        gerar_usuario("Lara Souza")
        gerar_usuario()  # usa nome completo aleatório

    Retorno:
        'larasouza12'
    """
    #Tratamento de erros de parâmetros
    if not isinstance(tamanho_minimo, int) or not isinstance(tamanho_maximo, int):
        raise TypeError("tamanho_minimo e tamanho_maximo devem ser inteiros.")
    if tamanho_minimo < 1:
        raise ValueError("tamanho_minimo deve ser pelo menos 1.")
    if tamanho_maximo < tamanho_minimo:
        raise ValueError("tamanho_maximo deve ser maior ou igual a tamanho_minimo.")

    if nome is None:
        nome = gerar_nome_completo()
    else:
        if not isinstance(nome, str):
            raise TypeError("O parâmetro 'nome' deve ser uma string ou None.")

    base = _normalizar_usuario(nome)
    if not base:
        base = "usuario"

    #Completa com números se for curto
    while len(base) < tamanho_minimo:
        base += str(random.randint(0, 9))

    #Corta se for grande demais
    base = base[:tamanho_maximo]

    #Vai ter 50% de chance de colocar números no final
    if random.random() < 0.5:
        sufixo = str(random.randint(0, 9999))
        resultado = base + sufixo
        return resultado[:tamanho_maximo]

    return base


def gerar_email(nome: str | None = None, dominio: str | None = None) -> str:
    """
    Gera um e-mail falso baseado no nome da pessoa.

    Parâmetros:
        nome:
            Nome que será usado para gerar o e-mail.
            Se None, um nome completo aleatório será usado.

        dominio:
            Domínio do e-mail (ex: mail.com)
            Se None, escolhe aleatoriamente da lista LISTA_DOMINIOS_EMAIL.

    Exemplo de chamada:
        gerar_email("Lara Silva")
        gerar_email()

    Retorno:
        'larasilva123@email.com'
    """
    if nome is None:
        nome = gerar_nome_completo()
    else:
        if not isinstance(nome, str):
            raise TypeError("O parâmetro 'nome' deve ser uma string ou None.")

    #Pequena variação com número no final
    usuario = _normalizar_usuario(nome)
    if random.random() < 0.7:
        usuario += str(random.randint(1, 9999))

    if dominio is None:
        dominio = random.choice(LISTA_DOMINIOS_EMAIL)
    else:
        # Validação simples do domínio informado
        if "@" in dominio:
            raise ValueError("O domínio não deve conter '@'. Use apenas a parte após '@'.")
        if "." not in dominio:
            raise ValueError("O domínio deve conter pelo menos um ponto (ex.: 'exemplo.com').")

    return f"{usuario}@{dominio}"


def gerar_senha(
    tamanho: int = 12,
    usar_minusculas: bool = True,
    usar_maiusculas: bool = True,
    usar_digitos: bool = True,
    usar_especiais: bool = False,
    minimo_minusculas: int | None = None,
    minimo_maiusculas: int | None = None,
    minimo_digitos: int | None = None,
    minimo_especiais: int | None = None,
    caracteres_especiais: str = "!@#$%^&*",
) -> str:
    """
    Gera uma senha aleatória com opções configuráveis pelo usuário.

    Parâmetros principais:
        tamanho: tamanho total da senha.
        usar_minusculas / usar_maiusculas / usar_digitos / usar_especiais:
            Define que tipos de caracteres podem aparecer.
        minimo_xxx:
            Define quantos caracteres mínimos cada tipo deve ter.
            Se None, não exige mínimo.
        caracteres_especiais:
            Define quais caracteres contam como especiais.

    Exemplo de chamada:
        gerar_senha()
        gerar_senha(tamanho=8, usar_especiais=True, minimo_especiais=1)

    Retorno:
        Exemplo: 'Ab7$k2LmQ9!3'
    """
     # Tratamento de tipos e valores
    if not isinstance(tamanho, int):
        raise TypeError("O parâmetro 'tamanho' deve ser um inteiro.")
    if tamanho <= 0:
        raise ValueError("O tamanho da senha deve ser maior que zero.")

        # validar mínimos
    for nome_param, valor in [
        ("minimo_minusculas", minimo_minusculas),
        ("minimo_maiusculas", minimo_maiusculas),
        ("minimo_digitos", minimo_digitos),
        ("minimo_especiais", minimo_especiais),
    ]:
        if valor is not None and (not isinstance(valor, int) or valor < 0):
            raise ValueError(f"{nome_param} deve ser um inteiro >= 0 ou None.")

    # Pelo menos um tipo de caractere precisa estar habilitado
    if not (usar_minusculas or usar_maiusculas or usar_digitos or usar_especiais):
        raise ValueError(
            "Pelo menos um tipo de caractere deve estar habilitado "
            "(minusculas, maiusculas, digitos ou especiais)."
        )

    minusculas = string.ascii_lowercase
    maiusculas = string.ascii_uppercase
    digitos = string.digits

    senha_chars: list[str] = []

    def adicionar_minimos(quantidade: int | None, pool: str, habilitado: bool):
        """
        Função auxiliar que adiciona 'quantidade' de caracteres obrigatórios.
        Usada internamente para montar a base da senha.
        """
        if not habilitado or quantidade is None or quantidade <= 0:
            return 0
        for _ in range(quantidade):
            senha_chars.append(random.choice(pool))
        return quantidade

    total_minimos = 0
    total_minimos += adicionar_minimos(minimo_minusculas, minusculas, usar_minusculas)
    total_minimos += adicionar_minimos(minimo_maiusculas, maiusculas, usar_maiusculas)
    total_minimos += adicionar_minimos(minimo_digitos, digitos, usar_digitos)
    total_minimos += adicionar_minimos(minimo_especiais, caracteres_especiais, usar_especiais)

    if total_minimos > tamanho:
        senha_chars = senha_chars[:tamanho]
        random.shuffle(senha_chars)
        return "".join(senha_chars)

    permitidos = ""
    if usar_minusculas:
        permitidos += minusculas
    if usar_maiusculas:
        permitidos += maiusculas
    if usar_digitos:
        permitidos += digitos
    if usar_especiais:
        permitidos += caracteres_especiais

    if not permitidos:
        permitidos = minusculas

    restantes = tamanho - len(senha_chars)
    for _ in range(restantes):
        senha_chars.append(random.choice(permitidos))

    random.shuffle(senha_chars)
    return "".join(senha_chars)
