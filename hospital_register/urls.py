from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('empreg/', views.empreg, name='empreg'),
    path('insertEmp/', views.insertEmp, name='insertEmp'),
    path('delete/', views.delete, name='delete'),
    path('delrecord/', views.delete_by_id, name='delete_by_empid'),
    path('patient/', views.patreg, name='patreg'),
    path('insertPat/',views.insertPat, name='insertPat'),
    path('genbill/',views.genbill, name='genbill'),
    path('insertBill/',views.insertBill, name='insertBill'),
    path('update/<int:id>', views.update, name = 'update'),
    path('deletebill/<int:id>', views.deletebill, name ='deletebill'),
    path('updatedetails/<int:id>', views.updatedetails, name='updatedetails'),
    path('appointment/',views.appointment, name="appointment"),
]