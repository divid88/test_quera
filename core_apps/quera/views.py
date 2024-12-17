from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.decorators import api_view
from rest_framework import permissions, status
from rest_framework.response import Response
# from django.core.files.storage import default_storage
from drf_spectacular.utils import extend_schema

import os
import subprocess

from .models import LevelUser, ProgramTest, SubjectTestProgram
from .serializers import ProgramSerializer, ProgramSerTestSerializer,\
        SubjectTestProgremSerializer


@api_view(['GET'])
def get_subject_test(request):
    subjects = SubjectTestProgram.objects.prefetch_related('tests')
    serializers = SubjectTestProgremSerializer(subjects, many=True).data
    return Response(serializers, 
                    status=status.HTTP_200_OK)


@api_view(['GET'])
def get_test_program(request, pk):
    query = ProgramTest.objects.get(pk=pk)
    serializers = ProgramSerTestSerializer(query).data
    return Response(serializers, status=status.HTTP_200_OK)

class SaveProgramAPIView(CreateAPIView, RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = LevelUser.objects.all
    serializer_class = ProgramSerializer

    @extend_schema(request=ProgramSerializer, responses=ProgramSerTestSerializer)
    def post(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        # level_user = LevelUser.objects.filter(user=user).last()
        # if level_user:
        #     level = level_user.level + 1
        # else:
        #     level = 0
        code_file = request.data.get('code_program')

        #file test python 
        test_file = ProgramTest.objects.get(pk=1)
        test_code = test_file.test_code
        test = "test.py"
        code = test_code.read()
        file = code_file.read()
        pwd = os.getcwd()
       
        subprocess.run(['mkdir', f'{pwd}/quera_ts/{user.id}'])
        with open(f'{pwd}/quera_ts/{user.id}/{code_file}', 'w') as f:
            f.write(file.decode("utf-8"))
        
        with open(f'{pwd}/quera_ts/{user.id}/{test}', 'w') as f: 
            f.write(code.decode("utf-8"))
        
        os.chdir(f'{pwd}/quera_ts/{user.id}')
        res = subprocess.run(['python3', f'test.py'], 
                             capture_output=True,
                             timeout=5
                             )
        test_file.test_result = res.stdout or res.stderr
        test_file.save()
        subprocess.run(['rm', f'{code_file}'])
        subprocess.run(['rm', f'test.py'])
        
        os.chdir(pwd)
        if res.returncode != 0:
            return Response(ProgramSerTestSerializer(test_file).data,
                        status=status.HTTP_400_BAD_REQUEST)

        # level_user = LevelUser.objects.create(user=user, code_program=code_file,
        #                                       level=level,
        #                                       notes=data.get('notes'),
        #                                       success=True)
        return Response(ProgramSerTestSerializer(test_file).data,
                        status=status.HTTP_200_OK)

    @extend_schema(request=ProgramSerializer, responses=ProgramSerTestSerializer)
    def get(self, request, pk, *args, **kwargs):
        user = request.user
        program_test = ProgramTest.objects.get(pk=pk)

        serializer = ProgramSerTestSerializer(program_test)
        return Response(serializer.data, status=status.HTTP_200_OK)