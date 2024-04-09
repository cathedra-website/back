from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(openapi.Info(
    title='ISS Cathedra Website API',
    default_version='v1',
    description='Swagger docs by students that made this site',
    terms_of_service='https://www.example.com/policies/terms/',
    contact=openapi.Contact(email='andreyzhevagin@knu.ua'),
    license=openapi.License(name='BSD License')
), public=True, permission_classes=(permissions.AllowAny,))