import re
from validate_docbr import CPF


def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)


def nome_valido(nome):
    return nome.isalpha()


def rg_valido(rg):
    return len(rg) == 7


def numero_cell_valido(numero_cell):
    padrao = "^\(\d{2}\)\s\d{4,5}\-\d{4}$"
    resposta = re.findall(padrao, numero_cell)
    return resposta
