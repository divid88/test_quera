from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import LevelUser, ProgramTest, SubjectTestProgram


User = get_user_model()


class ProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = LevelUser
        fields = ['code_program', 'level', 'success', 'notes']


class ProgramSerTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramTest
        fields = ['description', 'level', 'test_code', 'test_result',
                  'inputs', 'outputs', 'example_code']


class SubjectTestProgremSerializer(serializers.ModelSerializer):
    tests = ProgramSerTestSerializer(many=True)
    class Meta:
        model = SubjectTestProgram
        fields = ('title', 'tests')
