from django.urls import path
from products.views import OwnerListView, DogListView


urlpatterns = [
    path('/owners', OwnerListView.as_view()),
    path('/dogs', DogListView.as_view())
]
