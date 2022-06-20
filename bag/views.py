from multiprocessing import context
from django.shortcuts import render


# Create your views here.
def view_bag(request):
    '''
    A view to access the users shopping bag
    '''
    context = {}
    return render(request, 'bag/bag.html', context)