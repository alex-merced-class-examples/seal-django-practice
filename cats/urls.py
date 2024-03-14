from django.urls import path
from cats.views import index_create, update_delete_show, edit, new


urlpatterns = [
    path("", index_create), ## /cats
    path("new/", new), ## /cats/new
    path("<int:id>/", update_delete_show), ## /cats/<id> (get, put, delete)
    path("<id>/edit", edit) ## /cats/<id>/edit
]