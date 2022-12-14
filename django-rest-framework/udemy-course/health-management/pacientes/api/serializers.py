from agendamentos.api.serializers import AgendamentosDetalhesSerializer
from pacientes.models import Pacientes
from rest_framework import serializers


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = '__all__'


class PacientesDetalhesSerializer(serializers.ModelSerializer):
    agendamentos = AgendamentosDetalhesSerializer(many=True, read_only=True)

    class Meta:
        model = Pacientes
        fields = [
            "id_paciente",
            "nome",
            "data_nasc",
            "endereco",
            "num_endereco",
            "bairro_endereco",
            "cep",
            "data_cadastro",
            "rg",
            "agendamentos"
        ]
