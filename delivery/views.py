from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import numpy as np
# Create your views here.

@api_view(["POST"])
def add_contsiners(request):
    lst = []
    por=None
    con=None
    a=1
    for k,v in request.data.items():
        port=k
        con = v
    if 'containers' not in request.session:
        containers = []
    else:
        containers = request.session['containers']

    for i in range(5):
        col=[]
        if a > con:
            break
        for j in range(5):
            row = []
            if a > con:
                break
            for k in range(10):
                row.append(port)
                a+=1
                if a > con:
                    break
            col.append(row)
        containers.append(col)
    request.session['containers'] = containers

    return Response({"message":"containers added"})
@api_view(["GET"])
def get_pos(request,port):
    loc=[]
    containers=request.session['containers']

    for i, lst1 in enumerate(containers, start=0):
        for j, lst2 in enumerate(lst1, start=0):
            for k, lst3 in enumerate(lst2, start=0):
                if lst3 == port:
                    loc.append([i,j,k])
    return Response({port:loc})

@api_view(['GET'])
def del_containers(request):
    del request.session['containers']
    return Response({'message':'successfully deleted all containers'})

@api_view(['GET'])
def get_containers(request):
    # request.session['containers']
        if request.session['containers']:
            return Response({'message':request.session['containers']})
        else:
            return Response({'message': 'No containers'})
