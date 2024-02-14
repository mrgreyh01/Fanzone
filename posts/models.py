from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    """
    supported_teams_choices = {
        ('SELECT_TEAM', 'Select team'),
        ('ARSENAL', 'Arsenal'), ('ASTON_VILLA', 'Aston Villa'),
        ('BOURNEMOUTH_AFC', 'Bournemouth AFC'), ('BRENTFORD', 'Brentford'),
        ('BRIGHTON_&_HOVE_ALBION', 'Brighton & Hove Albion'), ('BURNLEY', 'Burnley'),
        ('CHELSEA', 'Chelsea'), ('CRYSTAL_PALACE', 'Crystal Palace'),
        ('EVERTON', 'Everton'), ('FULHAM', 'Fulham'),
        ('LIVERPOOL', 'Liverpool'), ('LUTON_TOWN', 'Luton Town'),
        ('MAN_CITY', 'Man City'), ('MAN_UTD', 'Manchester Utd'),
        ('NEWCASTLE_UTD', 'Newcastle Utd'), ('NOTTINGHAM_FOREST', 'Nottingham Forest'),
        ('SHEFFIELD_UTD', 'Sheffield Utd'), ('TOTTENHAM_HOTSPUR', 'Tottenham Hotspur'),
        ('WEST_HAM_UTD', 'West Ham Utd'), ('WOLVERHAMPTON_WANDERERS', 'Wolverhampton Wanderers')
    }

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_uxb6vu', blank=True
    )
    supported_teams_choices = models.CharField(
        max_length=24, choices=supported_teams_choices, default='SELECT_TEAM'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
