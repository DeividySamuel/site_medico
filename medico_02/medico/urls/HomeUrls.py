from django.urls import path
from medico.views.HomeView import home, cadastro, login_view, logout_view, pacientes


urlpatterns = [
    path('', home, name="home"),
    path('cadastro', cadastro, name="cadastro" ),
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout"),
    # path('pacientes', pacientes, name="pacientes")
   
   

]
