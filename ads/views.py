from django.shortcuts import render, redirect, get_object_or_404
from .models import Ad
from .forms import AdForm

def home(request):
    recent_ads = Ad.objects.all().order_by('-created_at')[:6]  # Најнови 6 огласи
    return render(request, 'ads/home.html', {'recent_ads': recent_ads})

def ad_list(request):
    category = request.GET.get('category')
    if category:
        ads = Ad.objects.filter(category=category)
    else:
        ads = Ad.objects.all()
    return render(request, 'ads/ad_list.html', {'ads': ads, 'category': category})

def ad_detail(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    return render(request, 'ads/ad_detail.html', {'ad': ad})

def ad_create(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ad_list')
    else:
        form = AdForm()
    return render(request, 'ads/ad_create.html', {'form': form})