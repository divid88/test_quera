from rest_framework import serializers

from .models import Subject, SubSubject, Concept


class ReadSubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ('id', 'title')


class ConceptReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Concept
        fields = ('id', 'describe', 'code')

class ReadSubSubjectSerializer(serializers.ModelSerializer):
    subject = ReadSubjectSerializer()
    concept = ConceptReadSerializer(many=True)

    class Meta:
        model = SubSubject
        fields = ['id', 'title', 'subject', 'concept']
