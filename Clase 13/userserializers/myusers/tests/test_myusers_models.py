import unittest

from rest_framework.serializers import ValidationError
from myusers.serializers.myusers import MyUserSerializer



class MyUserSerializerTestCase(unittest.TestCase):

    def test_valid_user_data(self):
        # Objeto con la información Válida del usuario a probar
        user_data = {
            "name": "Jhon Doe",
            "email": "jhon.doe@example.com",
            "age": 25
        }

        serializer = MyUserSerializer(data=user_data)
        self.assertTrue(serializer.is_valid()) # True

    def test_invalid_user_data(self):
        # Objeto con la información inválida del usuario a probar
        user_data = {
            "name": "Jhon Smith",
            "email": "jhon.smith@example.com",
            "age": 15
        }

        serializer = MyUserSerializer(data=user_data)
        self.assertFalse(serializer.is_valid()) # False

        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_valid_curp(self):
        # Objeto con la información inválida del usuario a probar
        user_data = {
            "name": "Jhon Smith",
            "email": "jhon.smith@example.com",
            "curp": "123IOU123OIU",
            "age": 15
        }

        serializer = MyUserSerializer(data=user_data)
        self.assertTrue(serializer.is_valid()) # True


    def test_invalid_curp(self):
        # Objeto con la información inválida del usuario a probar
        user_data = {
            "name": "Jhon Smith",
            "email": "jhon.smith@example.com",
            "curp": "123IOU123OIU",
            "age": 15
        }

        serializer = MyUserSerializer(data=user_data)
        self.assertFalse(serializer.is_valid()) # False

        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
