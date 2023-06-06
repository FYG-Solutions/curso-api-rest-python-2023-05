from rest_framework import serializers
from myusers.models import MyUser


class MyUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    age = serializers.IntegerField()

    def validate_age(self, age: int):
        if age < 18:
            raise serializers.ValidationError("La edad debe ser mayor o igual a 18")
        return age

    def validate(self, data: dict):
        if "name" in data and len(data["name"]) < 2:
            raise serializers.ValidationError("El nombre debe ser mayor a 2 caracteres.")
        return data
    
    def create(self, validated_data: dict):
        if self.is_valid():
            # name = validated_data["name"]
            # age = validated_data["age"]
            # email = validated_data["email"]
            # user = MyUser.objects.create(name=name, age=age, email=email)
            
            user = MyUser.objects.create(**validated_data)
            return user
        else:
            return None


