from django.shortcuts import render, redirect, get_object_or_404
from .models import todo, TipoSensor , Sala
from .forms import TipoSensorForm

def todo_list(request):
    TempMonitor = todo.objects.all()
    return render(request, "TempMonitor/todo_list.html", {"TempMonitor": TempMonitor})

def sobre(request):
    return render(request, 'TempMonitor/sobre.html')

def Contato(request):
    return render(request, 'TempMonitor/contato.html')

def tipo_sensor(request):
    sensores = TipoSensor.objects.all()
    return render(request, 'TempMonitor/tipo_sensor.html', {'sensores': sensores})

def adicionar_tipo_sensor(request):
    if request.method == 'POST':
        form = TipoSensorForm(request.POST)
        if form.is_valid():
            form.save()  # Salva no banco de dados
            return redirect('Tipo_Sensor')  # Redireciona para a página inicial
    else:
        form = TipoSensorForm()  # Formulário vazio

    return render(request, 'TempMonitor/adicionar_tipo_sensor.html', {'form': form})

def excluir_sensor(request, id):
    tipo_sensor = get_object_or_404(TipoSensor, pk=id)  # Usando get_object_or_404 para simplificar

    if request.method == 'POST':
        tipo_sensor.delete()  # Exclui o tipo de sensor
        return redirect('Tipo_Sensor')  # Redireciona para a lista de tipos de sensores

    return render(request, 'TempMonitor/excluir.html', {'tipo_sensor': tipo_sensor})


def exibir_sensor(request, id):
    # Recupera o sensor específico com base no ID ou retorna um erro 404
    sensor = get_object_or_404(TipoSensor, id=id)
    return render(request, 'TempMonitor/exibir.html', {'sensor': sensor})


def editar_tipo_sensor(request, tipo_sensor_id):
    # Recupera o TipoSensor com o ID fornecido
    tipo_sensor = get_object_or_404(TipoSensor, id=tipo_sensor_id)

    if request.method == "POST":
        # Aqui você pode alterar os campos do tipo_sensor com os novos dados
        tipo_sensor.tipo = request.POST.get('tipo', tipo_sensor.tipo)
        tipo_sensor.Sigla = request.POST.get('Sigla', tipo_sensor.Sigla)
        tipo_sensor.descricao = request.POST.get('descricao', tipo_sensor.descricao)

        # Salva as alterações no banco de dados
        tipo_sensor.save()

        # Redireciona para a página de lista ou onde desejar
        return redirect('Tipo_Sensor')  # Corrigido para o nome correto da URL.

    return render(request, 'TempMonitor/editar.html', {'tipo_sensor': tipo_sensor})

def sala(request): # Example, replace with actual query
    salas = Sala.objects.all().select_related('id_pavimento', 'id_orientacao')
    return render(request, 'TempMonitor/sala.html', {'salas': salas})


