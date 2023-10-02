from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import platFormforViewSet, api_root
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.

router = DefaultRouter()
router.register(r'platform', views.platFormforViewSet,basename="PlatForm")
#router.register(r'movie', views.WatchListViewSet,basename="movie")


# platform_list = platFormforViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# platform_detail = platFormforViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'

#     # write these code in path
#     path('platform/',platform_list, name="PlatForm_list"),
#     path('platform/<int:pk>/',platform_detail, name="PlatForm_list"),
# })
from . import views

urlpatterns = [
    path('list/',views.movie_list,name="WatchList_list"),
    path('list/<int:pk>',views.movie_detail, name="WatchList_detail"),
    path('list/<int:pk>/review/',views.ReviewList.as_view(), name="ReviewList"),
    path('list/<int:pk>/review_create/',views.ReviewCreate.as_view(), name="ReviewCreate"),
    path('list/review/<int:pk>',views.ReviewDetail.as_view(), name="ReviewDetail"),

    # path('platform/',views.platform_list.as_view(), name="PlatForm_list"),
    # path('platform/<int:pk>/',views.platform_detail.as_view(), name="PlatForm_list"),
    path('', include(router.urls)),
    path('',views.api_root),
  


    #

    # path('list/',views.movie_list,name="movie_list"),
    # path('list/<int:myid>',views.movie_detail, name="movie_detail"),
    # path('platform/',views.platform_list, name="plateform_list"),
    # path('platform/<int:myid>',views.platform_detail, name="platform_detail"),


]
#urlpatterns = format_suffix_patterns(urlpatterns)