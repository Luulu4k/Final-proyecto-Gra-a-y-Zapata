from django.shortcuts import render
from AppLectores.models import Escritor, Lector, Libro, avatar
from AppLectores.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def inicio(request):

    return render(request, "inicio.html", {"mensaje": "Disfruta"})

def acerca(request):

    return render(request, "acerca.html")
#Inicio y Registro

def iniciar_sesion(request):

    if request.method == "POST":

        formulario = AuthenticationForm(request, data = request.POST)

        if formulario.is_valid():

            info_dic = formulario.cleaned_data

            usuario = authenticate(username = info_dic["username"], password=info_dic["password"])

            if usuario is not None:

                login(request, usuario)
                
                return render(request, "inicio.html", {"mensaje": f"Bienvenid@ {usuario} a la Biblioteca"})
        
        else: 

            return render(request, "inicio.html", {"mensaje": "Error al iniciar sesión"})
    
    else:  

        formulario = AuthenticationForm()

    return render(request,"registro/login.html", {"formu": formulario})


def registrar(request):

    if request.method == "POST":
        
        formulario = RegistroUsuario (request.POST)

        if formulario.is_valid():

            formulario.save()

            return render(request, "inicio.html", {"mensaje":"Te has registrado correctamente."})

    else: 
        formulario = RegistroUsuario()       

    return render(request, "registro/registrar.html", {"formu": formulario})

@login_required 
def editar_usuario(request):
     
    usuario = request.user

    if request.method == 'POST':

       miFormulario = EditarUsuario(request.POST)
       
       if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            
            usuario.save()

            return render(request, "inicio.html")

    else:

        miFormulario = EditarUsuario(initial={ "first_name": usuario.first_name,
                                                "last_name": usuario.last_name,
                                                'email': usuario.email})


    return render(request, "registro/editar_usuario.html", {"formu": miFormulario})


@login_required
def agregar_avatar(request):

    if request.method =="POST":

        formulario= AvatarFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            
            info = formulario.cleaned_data
           
            usuario_actual = User.objects.get(username=request.user)
            nuevo_avatar = avatar (usuario= usuario_actual, imagen=info ["imagen"])
            
            nuevo_avatar.save()

            return render(request, "inicio.html", {"mensaje": "Creaste tu avatar"})
    
    else: 

        formulario = AvatarFormulario()

    return render (request, "registro/nuevo_avatar.html", {"formu": formulario})




def cierre_sesion(request):

    logout(request)

    return render (request,"inicio.html", {"mensaje": "Hasta pronto"})



#CRUD ESCRITOR

@login_required 
def crear_escritor(request):
    
    if request.method == "POST":

        formulario = EscritorForm(request.POST)

        if formulario.is_valid():

            info_dic = formulario.cleaned_data

            Escritor_nuevo = Escritor(nombre=info_dic["nombre"], 
                                  nacionalidad= info_dic["nacionalidad"],
                                  genero_preferido= info_dic ["genero_preferido"],
                                  )
            Escritor_nuevo.save()

            return render(request, "inicio.html")
        
    else: 

        formulario = EscritorForm()
        
    return render(request,"escritor/crear_escritor.html", {"formu":formulario})


def ver_escritor(request):
    
    todos_escritor = Escritor.objects.all()

    return render(request, "escritor/ver_escritor.html",{"total": todos_escritor})

@login_required     
def actualizar_escritor(request, escritor):

    escritor_elegido = Escritor.objects.get(id=escritor)

    if request.method == "POST":

        formulario = EscritorForm(request.POST)

        if formulario.is_valid():

            info_dic = formulario.cleaned_data

            escritor_elegido.nombre = info_dic["nombre"]
            escritor_elegido.nacionalidad = info_dic["nacionalidad"]
            escritor_elegido.genero_preferido = info_dic["genero_preferido"]

            escritor_elegido.save()
            
            return render(request,"inicio.html")

    else: 
            
            formulario = EscritorForm(initial={"nombre":escritor_elegido.nombre, 
                                               "nacionalidad": escritor_elegido.nacionalidad,
                                               "genero_preferido": escritor_elegido.genero_preferido})
    
            
    return render(request,"escritor/actualizar_escritor.html", {"formu": formulario})

@login_required  
def borrar_escritor(request, escritor):

    escritor_elegido = Escritor.objects.get(id=escritor)

    escritor_elegido.delete()

    return render(request, "inicio.html")




#CRUD LIBRO
@login_required 
def crear_libro(request): 
    
    if request.method == "POST":

        formulario = LibroForm(request.POST)

        if formulario.is_valid():

            info_dic = formulario.cleaned_data

            libro_nuevo = Libro(titulo=info_dic["titulo"], 
                                  autor= info_dic["autor"],
                                  genero= info_dic ["genero"],
                                  )
            libro_nuevo.save()

            return render(request, "inicio.html")
        
    else: 

        formulario = LibroForm()
        
    return render(request,"libro/crear_libro.html", {"formu":formulario})

     

def ver_libro(request):

    todos_libros = Libro.objects.all()

    return render(request, "libro/ver_libro.html",{"total": todos_libros})


@login_required  
def actualizar_libro(request, libro):

    Libro_elegido = Libro.objects.get(id=libro)

    if request.method == "POST":

        formulario = LibroForm(request.POST)

        if formulario.is_valid():

            info_dic = formulario.cleaned_data

            Libro_elegido.titulo = info_dic["titulo"]
            Libro_elegido.autor = info_dic["autor"]
            Libro_elegido.genero = info_dic["genero"]

            Libro_elegido.save()
            
            return render(request,"inicio.html")

    else: 
            
            formulario = LibroForm(initial={"titulo":Libro_elegido.titulo, 
                                            "autor": Libro_elegido.autor,
                                            "genero": Libro_elegido.genero})
    
            
    return render(request,"libro/actualizar_libro.html", {"formu": formulario})

@login_required  
def borrar_libro(request, libro):

    libro_elegido = Libro.objects.get(id=libro)

    libro_elegido.delete()

    return render(request, "inicio.html")


#CRUD LECTOR


@login_required 
def crear_lector(request):
    
    if request.method == "POST":

        formulario = LectorForm(request.POST)

        if formulario.is_valid():

            info_dic = formulario.cleaned_data

            lector_nuevo = Lector(nombre=info_dic["nombre"], 
                                  edad= info_dic["edad"],
                                  genero= info_dic ["genero"],
                                  preferencias_genero_literario=info_dic["preferencias_genero_literario"],
                                  )
            lector_nuevo.save()

            return render(request, "inicio.html")
        
    else: 

        formulario = LectorForm()
        
    return render(request,"lector/crear_lector.html", {"formu":formulario})
        


def ver_lector(request):
    
    todos_lector = Lector.objects.all()

    return render(request, "lector/ver_lector.html",{"total": todos_lector})

@login_required  
def actualizar_lector(request, lector):

    lector_elegido = Lector.objects.get(id=lector)

    if request.method == "POST":

        formulario = LectorForm(request.POST)

        if formulario.is_valid():

            info_dic = formulario.cleaned_data

            lector_elegido.nombre = info_dic["nombre"]
            lector_elegido.edad = info_dic["edad"]
            lector_elegido.genero = info_dic["genero"]
            lector_elegido.preferencias_genero_literario = info_dic["preferencias_genero_literario"]

            lector_elegido.save()
            
            return render(request,"inicio.html")

    else: 
            
            formulario = LectorForm(initial={"nombre":lector_elegido.nombre, 
                                              "edad": lector_elegido.edad,
                                              "genero": lector_elegido.genero,
                                              "preferencias_genero_literario":lector_elegido.preferencias_genero_literario})
    
            
    return render(request,"lector/actualizar_lector.html", {"formu": formulario})

@login_required  
def borrar_lector(request, lector):

    lector_elegido = Lector.objects.get(id=lector)

    lector_elegido.delete()

    return render(request, "inicio.html")

#Busquedas


def buscar_libro(request):

    return render(request, "libro/buscar_libro.html")

def resultados_libro(request):

    libro = request.GET["libro"]

    resultados = Libro.objects.filter(titulo__icontains=libro)

    return render(request, "libro/resultados_libro.html", {"resultados": resultados})

    
    

class CambiarContra(LoginRequiredMixin, PasswordChangeView):
    template_name= "registro/cambiar_contra.html"
    success_url = "/AppLectores/"