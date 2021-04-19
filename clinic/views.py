from rest_framework import generics
from rest_framework import generics, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from clinic.serializers import ClinicSerializer
from core.models import Clinic

class CreateClinicView(generics.CreateAPIView):
    """Create a new clinic"""
    serializer_class = ClinicSerializer

class WatchClinicView(APIView):
    """Watch the clinic user"""
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_object(self, pk):
        try:
            return Clinic.objects.get(pk=pk)
        except Clinic.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        if request.user.type == 'CLINIC':
            clinic_pk = Clinic.objects.filter(user_id=request.user.pk)
            clinic = self.get_object(request.user.pk)
            serializer = ClinicSerializer(clinic)
            return Response(serializer.data)
        else:
            raise PermissionDenied(
                {
                    "Message": "You don't have permission to access",
                    "Help": "Create and Clinic account." 
                }
            )