from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)

        # Create activities
        Activity.objects.create(user=ironman, type='Running', duration=30, calories=300, date=date.today())
        Activity.objects.create(user=captain, type='Cycling', duration=45, calories=400, date=date.today())
        Activity.objects.create(user=batman, type='Swimming', duration=60, calories=500, date=date.today())
        Activity.objects.create(user=superman, type='Yoga', duration=20, calories=100, date=date.today())

        # Create workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity for heroes', difficulty='Hard')
        Workout.objects.create(name='Power Yoga', description='Yoga for super strength', difficulty='Medium')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=700)
        Leaderboard.objects.create(team=dc, points=600)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
