from django.urls import path

from parking_api.apps.parking import views

urlpatterns = [
    path("parking", views.ParkingView.as_view({"post": "enter"})),
    path("parking/<int:pk>/out", views.ParkingView.as_view({"get": "out"})),
    path(
        "parking/<int:pk>/pay", views.ParkingView.as_view({"get": "payment"})
    ),
    path("parking/<str:plate>", views.ParkingView.as_view({"get": "history"})),
]
