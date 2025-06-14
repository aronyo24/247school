from django.utils.timezone import now
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from team.models import TeamMember
from visitors_details.models import Visitor
from .serializers import TeamMemberSerializer
from ipware import get_client_ip

class TeamList(ListAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer


class TrackVisitorView(APIView):
    def post(self, request):
        ip, _ = get_client_ip(request)
        if ip is None:
            return Response({"error": "Could not determine IP address"}, status=status.HTTP_400_BAD_REQUEST)

        user_agent = request.META.get("HTTP_USER_AGENT", "Unknown")
        private_ip = request.data.get("private_ip", "Unknown")

        visitor, created = Visitor.objects.get_or_create(ip_address=ip)
        visitor.user_agent = user_agent
        visitor.private_ip = private_ip
        visitor.last_visit = now()
        visitor.visit_count += 1

        # Optional: Try to get location info (only if geoip2 DB is available)
        try:
            import geocoder
            g = geocoder.ip(ip)
            visitor.city = g.city or "Unknown"
            visitor.country = g.country or "Unknown"
        except Exception as e:
            print("GeoIP lookup failed:", e)
            visitor.city = "Unknown"
            visitor.country = "Unknown"

        visitor.save()

        return Response({"message": "Visitor tracked successfully"}, status=status.HTTP_200_OK)


