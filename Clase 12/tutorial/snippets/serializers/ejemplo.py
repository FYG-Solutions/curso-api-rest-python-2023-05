from rest_framework import serializers
from snippets.models import MyUser


class MyUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    age = serializers.IntegerField()

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("La edad debe ser mayor o igual a 18.")
        return value

    def validate(self, data):
        if "name" in data and len(data["name"]) < 2:
            raise serializers.ValidationError("El nombre debe tener al menos 2 caracteres.")
        return data

    def create(self, validated_data):
        if self.is_valid():
            # Crear un nuevo usuario utilizando los datos validados
            user = MyUser.objects.create(**validated_data)
            return user
        else:
            # Realizar acciones en caso de datos no válidos
            return None
