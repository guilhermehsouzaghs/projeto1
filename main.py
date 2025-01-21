from faker import Faker
fake = Faker('pt_BR')

def GerarNomes():
    nomes = {
        'primeiro_nome': fake.first_name(),
        'segundo_nome': fake.last_name(),
        'id': fake.random_number(digits=2, fix_len=True)
    }

    return nomes
