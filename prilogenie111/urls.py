from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.title_page_my, name='title_page_my'),
    url(r'^add_people_to_table/', views.add_people_to_table, name='add_people_to_table'),
    url(r'^add_one_man/', views.add_one_man, name='add_one_man'),
    url(r'^get_people/', views.get_people, name='get_people'),
]



