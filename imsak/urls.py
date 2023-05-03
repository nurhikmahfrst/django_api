from django.urls import path
from . import views

app_name='restApi'

urlpatterns = [
    path('',views.readJadwal),
    path('detail/<int:id>',views.detailJadwal),
    path('create/',views.createJadwal),
    path('update/<int:id>',views.updateJadwal),
    path('delete/<int:id>',views.deletJadwal),
]