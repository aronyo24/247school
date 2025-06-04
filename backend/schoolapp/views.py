from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from team.models import TeamMember
from .serializers import TeamMemberSerializer





class TeamList(ListAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
