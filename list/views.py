from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Startup
from .serializers import StartupSerializer

@csrf_exempt
def startups(request):
    startups = Startup.objects.order_by('-niche_score')
    serializer = StartupSerializer(startups, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def startup_by_id(request, id):
    startup = Startup.objects.get(pk=id)
    serializer = StartupSerializer(startup)
    return JsonResponse(serializer.data)

@csrf_exempt
def startup_add_fire(request, id):
    startup = Startup.objects.get(pk=id)
    startup.fire_score += 1
    startup.niche_score += 1
    startup.save()
    return JsonResponse({})

@csrf_exempt
def startup_remove_fire(request, id):
    startup = Startup.objects.get(pk=id)
    startup.fire_score -= 1
    startup.niche_score -= 1
    startup.save()
    return JsonResponse({})

@csrf_exempt
def startup_add_snooze(request, id):
    startup = Startup.objects.get(pk=id)
    startup.snooze_score += 1
    startup.niche_score -= 1
    startup.save()
    return JsonResponse({})

@csrf_exempt
def startup_remove_snooze(request, id):
    startup = Startup.objects.get(pk=id)
    startup.snooze_score -= 1
    startup.niche_score += 1
    startup.save()
    return JsonResponse({})