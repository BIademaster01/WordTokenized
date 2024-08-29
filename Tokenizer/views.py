from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pythainlp.tokenize import word_tokenize

# Create your views here.

@api_view(['POST'])
def tokenize_text(request):
    text = request.data.get('text', '')

    if not text:
        return Response({"error": "No text provided"}, status=400)

    # ตัดคำโดยใช้ PyThaiNLP
    TokenizedOut = word_tokenize(text, engine='newmm')
    
    return Response({"words": TokenizedOut}, status=200)


