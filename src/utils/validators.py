import re

def validate_cpf(cpf):
    if type(cpf) is not str:
        raise ValueError('CPF inválido.')

    cpf = cpf.strip().replace('.', '').replace('-', '')

    if not re.fullmatch(r'[0-9]{11}', cpf):
        raise ValueError('O CPF deve conter exatamente 11 números.')

    return cpf

def validate_phone(phone):
    if type(phone) is not str:
        raise ValueError('Telefone inválido.')

    # +55 (82) 99143-7312
    phone = phone.strip().replace('+', '')
    phone = phone.replace('(', '').replace(')', '')
    phone = phone.replace('-', '').replace(' ', '')
    # 5582991437312

    phone_regex = r'[0-9]{11,13}'

    if not re.fullmatch(phone_regex, phone):
        raise ValueError('O telefone deve conter 11 ou 13 números.')

    return phone

def validate_email(email):
    if email is None:
        return None

    if type(email) is not str:
        raise ValueError('E-mail inválido.')

    email = email.strip()

    if len(email) > 150:
        raise ValueError('O e-mail deve ter no máximo 150 caracteres.')

    email_regex = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

    if not re.fullmatch(email_regex, email):
        raise ValueError('O formato do e-mail é inválido.')

    return email

def validate_chassis(chassis):
    if type(chassis) is not str:
        raise ValueError('Chassis inválido.')

    chassis = chassis.strip().upper()

    chassis_regex = r'[A-HJ-NPR-Z0-9]{17}'

    if not re.fullmatch(chassis_regex, chassis):
        raise ValueError('O chassi deve conter 17 caracteres válidos.')

    return chassis

def validate_plate(plate):
    if plate is None:
        return None

    if type(plate) is not str:
        raise ValueError('Placa inválido.')

    plate = plate.strip().upper().replace('-', '')

    if plate == '':
        return None

    old_plate_regex = r'[A-Z]{3}[0-9]{4}'
    mercosul_plate_regex = r'[A-Z]{3}[0-9][A-Z][0-9]{2}'

    if not re.fullmatch(old_plate_regex, plate) and not re.fullmatch(mercosul_plate_regex, plate):
        raise ValueError('O formato da placa é inválido.')

    return plate