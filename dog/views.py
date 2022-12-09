from django.http import JsonResponse
from .models import Dog


# safe=False allows us to give a dictionary response

def endpoints(request):
    data = ['/dogs', 'dogs/:id']
    return JsonResponse(data, safe=False)


def get_dogs(request):
    dog_list = ['dog1', 'dog2', 'dog3']
    return JsonResponse(dog_list, safe=False)
