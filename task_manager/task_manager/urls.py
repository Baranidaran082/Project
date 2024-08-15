"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from tasks import views as tasks_views  # Import views from the tasks app

urlpatterns = [
    # path('', tasks_views.index, name='index'),  # URL pattern for the index view
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # Include the URLs from the tasks app
    path('api/', include('tasks.api_urls')),  # Add this line for the API
]
