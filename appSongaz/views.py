import mimetypes
import os

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.urls import reverse
from django.views.generic import UpdateView

from appSongaz.forms import FileForm
from appSongaz.models import File


def login(request):
    return render(request, 'registration/login.html')


def register(request):
    return render(request, 'registration/register.html')



@login_required
def all_files(request):
    files = File.objects.all()
    all_users = User.objects.all()
    context = {
        'all_files': files,
        'all_users': all_users,
    }
    return render(request, 'appsongaz/index.html', context)


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.user = request.user
            file_instance.save()
            return redirect('all_files')
    else:
        form = FileForm()
    return render(request, 'appsongaz/upload_file.html', {
        'form': form
    })


@login_required
def delete_file(request, id):
    file_instance = get_object_or_404(File, id=id)
    file_instance.delete()
    return redirect('all_files')


@login_required
def download_file(request, pk):
    file_instance = get_object_or_404(File, pk=pk)
    file_path = os.path.join(settings.MEDIA_ROOT, str(file_instance.file))

    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read())

    content_type, encoding = mimetypes.guess_type(file_instance.file.name)
    response['Content-Type'] = content_type
    response['Content-Disposition'] = f'attachment; filename="{file_instance.file.name}"'

    return response


class UpdateFileView(UpdateView):
    model = File
    form_class = FileForm
    template_name = 'appsongaz/update_file.html'

    def get_success_url(self):
        return reverse('all_files')
