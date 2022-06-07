from django.db.models import Q
from .models import Address


def getAddresses(request):
    addresses = Address.objects.distinct().filter(
        Q(user__exact=request.user)
    )

    return addresses