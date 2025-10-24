
from django.contrib import admin
from django.urls import path , include

from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="KeyValue API",
        default_version="v1",
        description="Api for manage KeyValuePairs",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[],

)




urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/login/',TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('auth/refresh/',TokenRefreshView.as_view(), name="token_refresh"),

    path('api/',include("kvmanage.urls")),


    path("swagger/" , schema_view.with_ui("swagger", cache_timeout=0) , name="schema-swagger-ui"),


]
