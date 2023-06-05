import unittest
from rest_framework.serializers import ValidationError
from snippets.serializers import MyUserSerializer


class MyUserSerializerTestCase(unittest.TestCase):

    def test_valid_user_data(self):
        # Datos de ejemplo para un usuario válido
        user_data = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "age": 25
        }

        serializer = MyUserSerializer(data=user_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_user_data(self):
        # Datos de ejemplo para un usuario inválido (edad menor a 18)
        user_data = {
            "name": "Jane Smith",
            "email": "jane.smith@example.com",
            "age": 15
        }

        serializer = MyUserSerializer(data=user_data)
        self.assertFalse(serializer.is_valid())

        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

if __name__ == '__main__':
    unittest.main()
