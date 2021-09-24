from django.urls import path
from core.views import category_api_view, category_slug_api_view
from core.views import box_api_view,box_slug_api_view
from core.views import activity_api_view, activity_slug_api_view

urlpatterns = [
    path('categories/',category_api_view,name ='category_api'),
    path('categories/<slug:slug>',category_slug_api_view,name ='category_slug_api'),
    path('boxes/',box_api_view,name ='box_api'),
    path('boxes/<slug:slug>',box_slug_api_view,name ='box_slug_api'),
    path('activities/',activity_api_view,name ='activity_api'),
    path('activities/<slug:slug>',activity_slug_api_view,name ='activity_slug_api')
]
