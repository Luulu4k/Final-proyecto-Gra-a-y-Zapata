from django.urls import path
from AppLectores.views import *

urlpatterns = [
    path("", inicio, name="home"),
    path("login", iniciar_sesion, name= "Login"),
    path("registrar", registrar, name= "Registro"),
    path("logout", cierre_sesion, name= "Cierre"),
    path("editar", editar_usuario, name= "Editar"),
    path("contra", CambiarContra.as_view(), name= "Contra"),
    path("avatar", agregar_avatar, name= "Subir Avatar"),
    path("about", acerca, name= "about"),

    path("ver_escritor", ver_escritor, name="Escritor"),
    path("crear_escritor", crear_escritor, name= "Crear Escritor"),
    path("actualizar_escritor/<escritor>", actualizar_escritor, name= "Editar Escritor"),
    path("borrar_escritor/<escritor>", borrar_escritor, name= "Eliminar Escritor"),

    path("ver_lector", ver_lector, name="Lector"),
    path("crear_lector", crear_lector, name= "Crear Lector"),
    path("actualizar_lector/<lector>", actualizar_lector, name= "Editar Lector"),
    path("borrar_lector/<lector>", borrar_lector, name= "Eliminar Lector"),

    
    path("ver_libro", ver_libro, name="Libro"),
    path("crear_libro", crear_libro, name= "Crear Libro"),
    path("actualizar_libro/<libro>", actualizar_libro, name= "Editar Libro"),
    path("borrar_libro/<libro>", borrar_libro, name= "Eliminar Libro"),


    path("buscar_libro", buscar_libro, name= "buscar"),
    path("resultados_libro", resultados_libro),

    
    ] 