from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views

from todolist.settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
        path('tasks/', include('apps.tasks.urls')),
        path('users/', include('apps.tasks.urls')),
    ])),
]

# add session-auth for easier test task without frontend
if DEBUG:
    urlpatterns.append(
        path('api/v1/', include([
            path('session-auth/', include('rest_framework.urls', namespace='rest_framework')),
        ])),
    )
