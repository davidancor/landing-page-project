from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="website-home"),
	path('test/', views.test, name="website-test"),
	path('product/', views.product, name="website-product"),
	path('pricing/', views.pricing, name="website-pricing"),
	path('search/', views.search, name="website-search"),
]
