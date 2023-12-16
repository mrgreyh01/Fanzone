from django.db import IntegrityError
from rest_framework import serializers
from .models import Support, TeamsList


class SupporterSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    supported_team = serializers.ReadOnlyField(source='supported.team')

    class Meta:
        model = Support
        fields = [
            'id', 'owner', 'supported_team',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})


class TeamsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeamsList
        fields = [
            'id', 'team',
        ]
