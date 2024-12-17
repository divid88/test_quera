from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Subject
from .serializers import ReadSubjectSerializer
from .selected import get_subsubject

class SubjectAPIView(APIView):

    def get(self, request):
        queries = Subject.objects.all()
        serializers = ReadSubjectSerializer(queries, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class SubSubjectAPIView(APIView):

    def get(self, request, subject_id):
        queries = get_subsubject(subject=subject_id)
        