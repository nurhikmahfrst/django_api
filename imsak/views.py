from django.shortcuts import render
from . models import Jadwal
from . serializers import jadwalSerializer
# rest framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics 


def error_404(request, exception):
    return render(request, '404.html')

@api_view(['GET']) 
def readJadwal(request):
    jadwalimsyak = Jadwal.objects.all() 
    serializer = jadwalSerializer(jadwalimsyak, many=True)
    return Response(serializer.data)

# menampilkan 1 data atau detail
@api_view(['GET'])
def detailJadwal(request,id):
    jadwalimsyak = Jadwal.objects.get(pk=id) #mengambil 1 data
    serializer = jadwalSerializer(jadwalimsyak, many=False)
    return Response(serializer.data)

# menambah/input data
@api_view(['POST'])
def createJadwal(request):
    serializer = jadwalSerializer(data=request.data)# konversi ke dlm bentuk format serializer
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# mengedit/update data
@api_view(['PUT'])
def updateJadwal(request,id):
    jadwalimsyak = Jadwal.objects.get(pk=id)
    serializer=jadwalSerializer(instance=jadwalimsyak, data=request.data)# mengupdate data 1, merubah kedalam bntuk format serializer
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# meghapus/delet
@api_view(['DELETE'])
def deletJadwal(request,id):
    jadwalimsyak = Jadwal.objects.get(pk=id)
    jadwalimsyak.delete()

    return Response('Data berhasil di Hapus')


# MENAMPILKAN SEMUA DATA
#method request data ,me mastikan request menggunakan methode yg di tentukan
#megambil semua data di db (ORM)
# validasi untuk mengambil semua data
# mengembalikan data yang sudah diubah olh serializer menjdi format json

