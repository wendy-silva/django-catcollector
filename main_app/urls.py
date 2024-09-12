from django.urls import path
from .views import Home, CatList, CatDetail, FeedingListCreate, FeedingDetail # additional imports

urlpatterns = [
  path('', Home.as_view(), name='home'),
  # new routes below 
  path('cats/', CatList.as_view(), name='cat-list'),
  path('cats/<int:id>/', CatDetail.as_view(), name='cat-detail'),
  path('cats/<int:cat_id>/feedings/', FeedingListCreate.as_view(), name='feeding-list-create'),
	path('cats/<int:cat_id>/feedings/<int:id>/', FeedingDetail.as_view(), name='feeding-detail'),
]
