from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'filter/', views.FilterView.as_view(), name='main_filter'),
    url(r'', views.IndexView.as_view(), name='main_index'),
)
