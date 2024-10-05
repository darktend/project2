from django.http import JsonResponse
from django.db import connection
import logging

logger = logging.getLogger(__name__)

def test_connection(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return JsonResponse({'message': 'Connection to Backend RDS is successfuls!!!ECS!!!DEV!!VLAD_RDS!!!'})
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        return JsonResponse({'error': 'Database connection failed'}, status=500)
