from django.urls import path
from .views import tokenize_text

urlpatterns = [
    path('Tokenize/', tokenize_text, name='Tokenizer_text'),
]
