
from django.contrib import admin
from django.urls import path, include
from user import views as user_views
from .defaut_view import start_screen

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register,name='register'),
    path('blog/', include('blog.urls')),
    path('', start_screen,name='start-screen')

]
