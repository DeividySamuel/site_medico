from django.urls import path

from plataforma.views.PacienteView import  dados_paciente, refeicao, plano_alimentar,plano_alimentar_listar, opcao, pacientes, dados_paciente_listar

urlpatterns = [
    path('pacientes/', pacientes, name="pacientes"),
    path('dados_paciente/', dados_paciente_listar, name="dados_paciente_listar"),
    path('dados_paciente/<str:id>/', dados_paciente, name="dados_paciente"),
    path('plano_alimentar_listar/', plano_alimentar_listar, name="plano_alimentar_listar"),
    path('plano_alimentar/<str:id>/', plano_alimentar, name="plano_alimentar"),
    path('refeicao/<str:id_paciente>/', refeicao, name="refeicao"),
    path('opcao/<str:id_paciente>/', opcao, name="opcao"),
    # path('', index, name='index'),
]

