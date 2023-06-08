from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='javascript')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = [
            'id',
            'title',
            'code',
            'owner',
            'linenos',
            'language',
            'style',
            'created'
        ]

    def validate(self, data: dict):
        # language -> None -> 'javascript'
        if data["language"] == 'javascript':
            data["language"] = 'JAVASCRIPT'
        return data


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
