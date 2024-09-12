from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from allauth.account.views import login, logout, signup

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('profile/', user_views.profile, name='profile'),    
    path("login/", login, name="login"),  
    path("logout/", logout, name="logout"), 
    path("signup/", signup, name="signup"), 
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='account/password_reset.html'
         ),
         name='password_reset'),    
    path('blog/', include('blog.urls')),
    path('', include('blog.urls')), # de esta manera el blog es la pagina por defecto
    path('todo/', include('todo.urls')),
    path('accounts/', include('allauth.urls')),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

