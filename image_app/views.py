from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .forms import ImageUploadForm
from .models import Image


class ImageUploadView(FormView):
    template_name = 'image_app/home.html'
    form_class = ImageUploadForm
    success_url = reverse_lazy("image_app:img_upload_view")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Image.objects.all()
        return context