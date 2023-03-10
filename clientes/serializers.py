from rest_framework import serializers
from clientes.models import Cliente
from .validetors import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

    def validate(self, data):
        if not cpf_valido(data["cpf"]):
            raise serializers.ValidationError({"cpf": "O CPF informado é inválido. Informe um CPF válido"})

        if not nome_valido(data["nome"]):
            raise serializers.ValidationError(
                {"nome": "O nome deve conter apenas letras"}
            )

        if not rg_valido(data["rg"]):
            raise serializers.ValidationError({"rg": "O rg deve conter 7 digitos"})

        if not numero_cell_valido(data["celular"]):
            raise serializers.ValidationError(
                {
                    "celular": "O telefone celular deve respeitar esse padrão: '(xx) xxxx-xxxx' ou '(xx) xxxxx-xxxx'"
                }
            )

        return data
