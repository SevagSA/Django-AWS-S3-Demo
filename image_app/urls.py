from django.urls import path

from .views import ImageUploadView

app_name = 'image_app'

urlpatterns = [
    path('', ImageUploadView.as_view(), name='img_upload_view')
]