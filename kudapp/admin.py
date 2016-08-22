from django.contrib import admin

from .models import Comuna, TipoServicio, Evento, User, Servicio, Comentario, Calificacion, Categoria

admin.site.register(Comuna)
admin.site.register(TipoServicio)
admin.site.register(Evento)
admin.site.register(User)
admin.site.register(Servicio)
admin.site.register(Comentario)
admin.site.register(Calificacion)
admin.site.register(Categoria)

# Register your models here.
