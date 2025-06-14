from django.db import models
from django.utils.timezone import now


class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()  # Public IP
    private_ip = models.CharField(max_length=50, blank=True, null=True)  # Private IP (optional)
    user_agent = models.TextField()  # User-Agent string
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    last_visit = models.DateTimeField(default=now)  # Last visit time
    visit_count = models.PositiveIntegerField(default=1)  # Default to 1 on first visit

    def update_location(self):
        """
        Fetch city and country based on the visitor's IP address using geocoder.
        """
        try:
            import geocoder
            g = geocoder.ip(self.ip_address)
            self.city = g.city or "Unknown"
            self.country = g.country or "Unknown"
        except Exception as e:
            self.city = "Unknown"
            self.country = "Unknown"
            print(f"GeoIP failed for {self.ip_address}: {e}")

    def __str__(self):
        return f"{self.ip_address} - {self.visit_count} visits"
