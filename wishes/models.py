from django.conf import settings
from django.db import models


class Wish(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Wishes"  # Default is "Wishs" :(

    def __str__(self):
        return f"Wish by {self.user}"
