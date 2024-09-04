from django.urls import path


from .views import HomePageView, ProductView, ProductsDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('products/', ProductView.as_view(), name="products"),
    path('products/<int:id>/',ProductsDetailView.as_view(), name="detail")
]
