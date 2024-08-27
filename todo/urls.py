from django.urls import path
from .views import (ItemCreateView, ItemDeleteView, ItemListView, 
                    ItemUpdateView)

urlpatterns = [    
    path('todo/', ItemListView.as_view(), name="todo"),    
    path("item-create/", ItemCreateView.as_view(), name="item-create"),    
    path("item/<int:pk>/delete", ItemDeleteView.as_view(), name="item-delete"),        
    path("item/<int:pk>/update", ItemUpdateView.as_view(), name="item-update"),
]