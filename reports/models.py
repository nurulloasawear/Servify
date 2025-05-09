from django.db import models
from users.models import Users

class Report(models.Model):
    reporter = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='reports_sent')
    reported_user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='reports_received')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
# -