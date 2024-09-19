from rest_framework import status as rest_status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import SessionInfo
from .serializers import SessionInfoSerializer

# Create your views here.

@api_view(["GET"])
def get_sessions_info(request):
    sessions = SessionInfo.objects.all()
    if len(sessions) == 0:
        return Response(
            data = "Не найдено сеансов",
            status = rest_status.HTTP_404_NOT_FOUND
        )
    
    serialized_data = SessionInfoSerializer(sessions, many=True)
    return Response(serialized_data.data, status = rest_status.HTTP_200_OK)