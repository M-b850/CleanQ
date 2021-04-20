from rest_framework import generics
from rest_framework import generics, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from django.shortcuts import get_list_or_404

from clinic.serializers import ClinicSerializer
from core.models import Clinic

class CreateClinicView(generics.CreateAPIView):
    """Create a new clinic"""
    serializer_class = ClinicSerializer

class WatchClinicView(APIView):
    """Watch the clinic user"""
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()
    authentication_classes = (authentication.TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request, format=None):
        if request.user.type == 'CLINIC':
            clinic = get_list_or_404(Clinic, pk=request.user.pk)
            serializer = ClinicSerializer(clinic, many=True)
            return Response(serializer.data)
        else:
            raise PermissionDenied(
                {
                    "Message": "You don't have permission to access",
                    "Help": "Create a Clinic account." 
                }
            )