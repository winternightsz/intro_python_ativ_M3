import string

def validar_email(email: str) -> bool:
    """
    Verifica se um e-mail é válido.

    Regras:
        - Deve ter 1 '@'
        - Deve ter '.' após o '@'
        - Não pode começar ou terminar com '@' ou '.'

    Exemplo de chamada:
        validar_email("teste@gmail.com")

    Erros:
        TypeError se 'email' não for string.
        
    Retorno:
        True ou False
    """
    if not isinstance(email, str):
        raise TypeError("O parâmetro 'email' deve ser uma string.")

    if "@" not in email or email.count("@") != 1:
        return False

    usuario, dominio = email.split("@", 1)
    if not usuario or not dominio:
        return False

    if "." not in dominio:
        return False

    if email[0] in "@." or email[-1] in "@.":
        return False

    return True


def validar_usuario(
    usuario: str,
    tamanho_minimo: int = 3,
    tamanho_maximo: int = 20,
) -> bool:
    """
    Valida um nome de usuário.

    Regras:
        - Tamanho mínimo e máximo configurável
        - Apenas letras, números, '_' e '.'
        - Não pode ser só números
    Erros:
        TypeError se 'usuario' não for string.
        TypeError se tamanhos não forem inteiros.
        ValueError se tamanhos forem inválidos.
        
    Exemplo:
        validar_usuario("lara123")
        validar_usuario("joao.silva")

    Retorno:
        True ou False
    """
    if not isinstance(usuario, str):
        raise TypeError("O parâmetro 'usuario' deve ser uma string.")

    if not isinstance(tamanho_minimo, int) or not isinstance(tamanho_maximo, int):
        raise TypeError("tamanho_minimo e tamanho_maximo devem ser inteiros.")

    if tamanho_minimo < 1:
        raise ValueError("tamanho_minimo deve ser pelo menos 1.")
    if tamanho_maximo < tamanho_minimo:
        raise ValueError("tamanho_maximo deve ser maior ou igual a tamanho_minimo.")


    if not (tamanho_minimo <= len(usuario) <= tamanho_maximo):
        return False

    permitidos = string.ascii_letters + string.digits + "_."
    if any(ch not in permitidos for ch in usuario):
        return False

    if usuario.isdigit():
        return False

    return True


def validar_senha(
    senha: str,
    tamanho_minimo: int = 8,
    exigir_minusculas: bool = True,
    exigir_maiusculas: bool = True,
    exigir_digitos: bool = True,
    exigir_especiais: bool = False,
    caracteres_especiais: str = "!@#$%^&*",
) -> bool:
    """
    Valida uma senha com regras configuráveis.

    Parâmetros:
        senha: texto da senha
        tamanho_minimo: comprimento mínimo
        exigir_minusculas: exige pelo menos 1 letra minúscula
        exigir_maiusculas: exige pelo menos 1 letra maiúscula
        exigir_digitos: exige pelo menos 1 número
        exigir_especiais: exige pelo menos 1 símbolo especial
        caracteres_especiais: conjunto de símbolos válidos
    Erros:
        TypeError se 'senha' não for string.
        TypeError se caracteres_especiais não for string.
        TypeError se tamanho_minimo não for inteiro.
        ValueError se tamanho_minimo <= 0.

    Exemplo:
        validar_senha("Abc123!")
        validar_senha("Senha123", exigir_especiais=True)

    Retorno:
        True ou False
    """
    if not isinstance(senha, str):
        raise TypeError("O parâmetro 'senha' deve ser uma string.")

    if not isinstance(tamanho_minimo, int):
        raise TypeError("tamanho_minimo deve ser um inteiro.")
        
    if tamanho_minimo <= 0:
        raise ValueError("tamanho_minimo deve ser maior que zero.")
        
    #Tratamento de tipo dos caracteres especiais
    if not isinstance(caracteres_especiais, str):
        raise TypeError("caracteres_especiais deve ser uma string.")

    if len(senha) < tamanho_minimo:
        return False

    if exigir_minusculas and not any(ch.islower() for ch in senha):
        return False

    if exigir_maiusculas and not any(ch.isupper() for ch in senha):
        return False

    if exigir_digitos and not any(ch.isdigit() for ch in senha):
        return False

    if exigir_especiais and not any(ch in caracteres_especiais for ch in senha):
        return False

    return True
