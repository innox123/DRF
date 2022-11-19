from django.contrib import admin
from django.urls import path
from todos import views as todosviews
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', todosviews.todos_list),
    path('todos/<int:id>/', todosviews.todo_detail),
]

# to get json data in the browser then we add (format=None) to views
urlpatterns = format_suffix_patterns(urlpatterns)
