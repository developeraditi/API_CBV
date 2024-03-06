from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from app.serializers import *
from app.models import *

# Create your views here.
class Productjsondata(APIView):
    def get(self,request,id):
        POD = Product.objects.all()
        PJO = ProductModeSerializer(POD,many=True)
        return Response(PJO.data)


    def post(self,request,id):
        JSO =request.data
        POD =ProductModeSerializer(data=JSO)
        if POD.is_valid():
            POD.save()
            return Response({"insert":"INSERTED"})

        else :
            return Response({"Not":"NoT INSERTED"})


    def put(self,request,id):
        POD=Product.models.get(id=id)
        PDO=ProductModeSerializer(PDO,data=request.data)
        if PDO.is_valid():
            PDO.save()
            return Response({"update":"Updated data"})
        return Response({"notupdated":"update not done"})

    def post(self,request,id):
        POD=Product.models.get(id=id)
        PDO=ProductModeSerializer(POD,data=request.data,partial=True)
        if PDO.is_valid():
            PDO.save()
            return Response({"update":"Updated data"})
        return Response({"notupdated":"update not done"})

    def delete(self,request,id):
        Product.models.get(id=id).delete()
        return Response({"delete":"DELETED"})
