from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def profile(request):
    profile = get_object_or_404(User, pk=request.user.id)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)



