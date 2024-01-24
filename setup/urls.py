
from django.contrib import admin
from django.urls import path, include
from escola.views import AlunoViewSet, CursosViewSet, MatriculaViewSet, ListaMatriculasAlunos, ListaAlunosMatriculados
from rest_framework import routers

router = routers.DefaultRouter()
router.register('aluno', AlunoViewSet, basename= 'Alunos')
router.register('curso', CursosViewSet, basename='Cursos')
router.register('matricula', MatriculaViewSet, basename= 'Matriculas')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', ListaMatriculasAlunos.as_view()),
    path('curso/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view()),
]

