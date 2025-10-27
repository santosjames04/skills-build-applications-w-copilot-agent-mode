from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', email='test@example.com')
        self.assertEqual(user.email, 'test@example.com')

    def test_activity_creation(self):
        activity = Activity.objects.create(user_email='test@example.com', type='run', duration=10)
        self.assertEqual(activity.type, 'run')

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(team='Test Team', points=50)
        self.assertEqual(lb.points, 50)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', difficulty='Hard')
        self.assertEqual(workout.difficulty, 'Hard')
