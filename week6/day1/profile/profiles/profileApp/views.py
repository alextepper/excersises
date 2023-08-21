import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Profile


@csrf_exempt
@require_http_methods(["POST"])
def create_profile(request):
    try:
        name = request.POST.get('name')
        email = request.POST.get('email')

        if not name or not email:
            return JsonResponse({'status': 'error', 'message': 'name or email missing'}, status=400)

        profile = Profile.objects.create(name=name, email=email)
        profile.save()

        return JsonResponse({'status': 'success', 'message': 'Profile created successfully'}, status=201)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_profile(request, profile_id):
    try:
        profile = Profile.objects.get(id=profile_id)
        profile.delete()
        return JsonResponse({'status': 'success', 'message': 'Profile deleted successfully'}, status=200)
    except Profile.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Profile not found'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
