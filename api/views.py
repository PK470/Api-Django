from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from .serializer import Companyserializer
from .models import Company
from rest_framework.views import APIView

# Create your views here.
@api_view(['GET','POST'])
def compemp(request):
    if request.method == 'GET':
        cmp = Company.objects.all()
        serializer = Companyserializer(cmp, many = True)
        return JsonResponse(serializer.data, safe = False)
    elif request.method == 'POST':
        serializer = Companyserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
@api_view(['GET','PUT','DELETE'])
def compempgetone(request, id):
    try:
        cmp = Company.objects.get(pk = id)
    except:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = Companyserializer(cmp)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Companyserializer(cmp , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status = status.HTTP_202_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        cmp.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
class CmpApi(APIView):
    def get(self, request,*args, **kwargs):
        try:
            k = kwargs.get('k')
            if k is not None:
                company = Company.objects.get(company_id = k)
                serilizer = Companyserializer(company)
                return Response({
                    'data': serilizer.data,
                    'status': 'Done'
                })
            else:
                company = Company.objects.all()
                serilizer = Companyserializer(company, many =True)
                return Response({
                    'data': serilizer.data,
                    'status': 'Done'
                })
        except Exception as e:
            return Response(
                {
                    'error':'Bad Request',
                    'message':str(e)
                })
        