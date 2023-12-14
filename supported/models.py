from django.db import models
from django.contrib.auth.models import User


class Support(models.Model):

    owner = models.ForeignKey(
        User, related_name='supporting', on_delete=models.CASCADE
    )
    supported = models.ForeignKey(
        User, related_name='supported', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'supported']

    def __str__(self):
        return f'{self.owner} {self.supported}'
