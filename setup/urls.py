from django.contrib import admin
from django.urls import path
from TempMonitor.views import (
    todo_list, sobre, Contato, tipo_sensor, adicionar_tipo_sensor, excluir_sensor, exibir_sensor, editar_tipo_sensor , sala
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_list, name='home'),  # Página inicial
    path('sobre/', sobre, name='sobre'),  # Página "Sobre"
    path('Contato/', Contato, name='Contato'),  # Página "Contato"
    path('tipo_sensor/', tipo_sensor, name='Tipo_Sensor'),  # Página "tipo de sensor"
    path('adicionar-tipo-sensor/', adicionar_tipo_sensor, name='adicionar_tipo_sensor'),
    path('excluir/<int:id>/', excluir_sensor, name='excluir_sensor'),  # Página para excluir
    path('exibir/<int:id>/', exibir_sensor, name='exibir_sensor'),  # Página para exibir sensores
    path('editar_tipo_sensor/<int:tipo_sensor_id>/', editar_tipo_sensor, name='editar_tipo_sensor'),
    path('sala/', sala, name='sala'),
]
