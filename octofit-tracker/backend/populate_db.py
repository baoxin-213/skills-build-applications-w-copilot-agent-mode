import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from django.contrib.auth.models import User
from octofit.models import Team, Activity  # Assumes you will create these models

# Create test users
def create_users():
    users = [
        {'username': 'paul', 'email': 'paul@mergington.edu', 'password': 'testpass123'},
        {'username': 'jessica', 'email': 'jessica@mergington.edu', 'password': 'testpass123'},
        {'username': 'student1', 'email': 'student1@mergington.edu', 'password': 'testpass123'},
    ]
    for u in users:
        if not User.objects.filter(username=u['username']).exists():
            User.objects.create_user(**u)

# Create test teams
def create_teams():
    paul = User.objects.get(username='paul')
    jessica = User.objects.get(username='jessica')
    Team.objects.get_or_create(name='Red Rockets', coach=paul)
    Team.objects.get_or_create(name='Blue Blazers', coach=jessica)

# Create test activities
def create_activities():
    student = User.objects.get(username='student1')
    team = Team.objects.first()
    Activity.objects.get_or_create(user=student, team=team, type='Running', duration=30, points=10)
    Activity.objects.get_or_create(user=student, team=team, type='Walking', duration=60, points=8)

if __name__ == '__main__':
    create_users()
    create_teams()
    create_activities()
    print('Test data populated!')
