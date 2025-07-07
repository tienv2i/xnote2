from django.shortcuts import render


def index(request):
    context = {
        
    }
    return render(request, "onthi_gp/index.html", context)

# Create your views here.
def onthi(request, chu_de):
    template_name = f"onthi_gp/crawl_data/{chu_de}.html"
    context = {
        "template_name": template_name,
    }
    return render(request, "onthi_gp/onthi.html", context)