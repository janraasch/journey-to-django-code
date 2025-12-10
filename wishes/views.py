from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Wish

@login_required
def home(request):
    wish = Wish.objects.get_or_create(
        user=request.user,
        defaults={"text": "I want to be a Django developer"}
    )[0]
    if request.method == "POST":
        wish.text = request.POST.get("text", "")
        wish.save()
        return redirect('wishes:home')
    return render(request, 'wishes/home.html', {'wish': wish})
