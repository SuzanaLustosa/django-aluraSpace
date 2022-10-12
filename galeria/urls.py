# isolando urls

from django.urls import path
from galeria.views import index, imagem

# lista com todos os endereços relacionados a nossa aplicação
# isolando as rotas de galeria
urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem'),
]