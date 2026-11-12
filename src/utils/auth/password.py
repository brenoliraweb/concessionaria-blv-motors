import bcrypt

def hash_password(password):
    """
        Gera e retorna o hash da senha usando bcrypt.
    """
    password = password.encode('utf-8')
    password_hash = bcrypt.hashpw(password, bcrypt.gensalt())

    return password_hash.decode('utf-8')

def verify_password(password, password_hash):
    """
        Verifica se a senha informada corresponde ao hash armazenado.
    """
    password = password.encode('utf-8')
    password_hash = password_hash.encode('utf-8')

    return bcrypt.checkpw(password, password_hash)
