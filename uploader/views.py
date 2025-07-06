from django.shortcuts import render
from .models import UploadedFile
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    all_files = UploadedFile.objects.all().order_by('-uploaded_at')
    paginator = Paginator(all_files, 20)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        'files': page_obj,
        'page_obj': page_obj
    }
    return render(request, 'uploader/index.html', context)

# def upload_file(request):
#     if request.method == 'POST':
#         form = 