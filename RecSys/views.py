# RecSys/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .products import give_rec  # Ensure this import is correct

@csrf_exempt
def recommend(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_name = data.get('product_name')
        recommendations = give_rec(product_name)
        return JsonResponse({'recommendations': recommendations})
    return JsonResponse({'error': 'Invalid request method.'}, status=400)
