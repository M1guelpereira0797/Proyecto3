from django.shortcuts import render, get_object_or_404
from vehiculo.models import Vehiculo
from vehiculo.forms import Buscar_carro, CarrosForm
from django.views import View


def index(request):
    return render(request, "autos/Presentacion_de_carros.html")

def buscar_carros(resquest):
    lista_de_marca_de_carros=["Mercedes", "Ferrari", "Lamborgini", "Mclaren", "Chevrolet"]
    query=resquest.GET["q"]
    if query in lista_de_marca_de_carros:
        indice_de_resultado = lista_de_marca_de_carros.index(query)
        resultado=lista_de_marca_de_carros[indice_de_resultado]
    else: 
        resultado= "no hay registro en la base de datos"
    return render(resquest, 
    "autos/buscar_carros.html",
    {"resultado": resultado})

def mostrar_carros(request):
  lista_carros = Vehiculo.objects.all()
  return render(request, "autos/Presentacion_de_carros.html", {"lista_carros": lista_carros})

class Buscar(View):
    form_class = Buscar_carro
    template_marca_del_carro = 'autos/buscar_carros.html'
    initial = {"marca_del_carro":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_marca_del_carro, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            marca_del_carro = form.cleaned_data.get("marca_del_carro")
            Carros = Vehiculo.objects.filter(marca_del_carro__icontains=marca_del_carro).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_marca_del_carro, {'form':form, 
                                                        'Carros': Carros})
        return render(request, self.template_marca_del_carro, {"form": form})
class AltaCarros(View):

    form_class = CarrosForm
    template_name = 'autos/Alta_Carros.html'
    initial = {"marca_del_carro":"", "modelos_del_carro":"", "color_del_carro":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el nuevo carro {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ActualizarCarro(View):
  form_class = CarrosForm
  template_name = 'autos/Actualizar_familiar.html'
  initial = {"marca_del_carro":"", "modelos_del_carro":"", "color_del_carro":"",}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      Vehiculo = get_object_or_404(Vehiculo, pk=pk)
      form = self.form_class(instance=Vehiculo)
      return render(request, self.template_name, {'form':form,'Vehiculo': Vehiculo})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
      Vehiculo = get_object_or_404(Vehiculo, pk=pk)
      form = self.form_class(request.POST ,instance=Vehiculo)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el Carro {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'Vehiculo': Vehiculo,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})