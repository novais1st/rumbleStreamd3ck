
from .models import Usuario
from  rest_framework import serializers
class UsuarioSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Usuario
        fields = ['id_usuario', 'nome', 'email', 'telefone', 'senha', 'created_at', 'edited_at']

    def create(self, validated_data):
        senha = validated_data.pop('senha')
        usuario = Usuario(**validated_data)
        usuario.set_password(senha)
        usuario.save()
        return usuario
