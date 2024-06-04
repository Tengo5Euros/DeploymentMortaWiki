from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

from . import views
app_name = 'mortalweb'
urlpatterns = [
    path("", views.index, name="index"),
    path("mortalkombatweb/characters/", views.show_characters, name="characters"),
    path("mortalkombatweb/scenarios/", views.scenarios, name="scenarios"),
    path("mortalkombatweb/contact/", views.contact, name="contact"),
    path('personaje/<str:nombre_personaje>/', views.detalle_personaje, name='detalle_personaje'),
    path("mortalkombatweb/crearpersonaje", views.create_character, name="crear_personajes"),
    path("mortalkombatweb/crearCoach", views.create_coach, name="crear_coach"),
    path("mortalkombatweb/learn", views.choose_character, name="choose_character"),
    path("mortalkombatweb/learn/character", views.learn, name="learn"),
    path('mortalkombatweb/response/', views.response, name='response'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)