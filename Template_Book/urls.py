from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index_book),
    path('create_Book', views.create_Book),
    path('show/<int:pk>', views.view_detail),

    # Creation of Author

    path('index_one', views.index_Author),
    path('create_Author', views.create_authors),
    path('show_author/<int:pk>', views.view_detail_author),
    # add book

    path('add_book/<int:pk>', views.add_Book),
    path('add_author/<int:pk>', views.add_Author),


]
