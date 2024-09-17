import random
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from tasks.models import Tag, Task  # Update with your actual app and model imports
from users.models import BaseUser

fake = Faker()
class Command(BaseCommand):
    help = "Generate fake data for users, tasks, and tags"

    def add_arguments(self, parser):
        parser.add_argument("--users", type=int, default=5, help="Number of users to create")
        parser.add_argument("--tasks", type=int, default=20, help="Number of tasks to create")
        parser.add_argument("--tags", type=int, default=10, help="Number of tags to create")

    def handle(self, *args, **kwargs):
        num_users = kwargs["users"]
        num_tasks = kwargs["tasks"]
        num_tags = kwargs["tags"]

        self.stdout.write(f"Creating {num_tags} tags...")

        self.stdout.write(f"Creating {num_users} users...")
        users = self.create_users(num_users)
        tags = self.create_tags(users, num_tags)

        self.stdout.write(f"Creating {num_tasks} tasks...")
        self.create_tasks(users, tags, num_tasks)

        self.stdout.write(self.style.SUCCESS("Data population complete."))



    def create_users(self, num_users):
        users = []
        for _ in range(num_users):
            username = fake.unique.user_name()
            email = fake.email()
            password = "password123"
            user = BaseUser.objects.create_user(username=username, email=email, password=password)
            users.append(user)
        return users

    def create_tags(self,users, num_tags):
        tags = []
        for _ in range(num_tags):
            name = fake.word().capitalize()
            created_by = random.choice(users)

            tag, created = Tag.objects.get_or_create(name=name, created_by=created_by )
            tags.append(tag)
        return tags

    def create_tasks(self, users, tags, num_tasks):
        statuses = ["not_started", "in_progress", "completed", "on_hold", "cancelled"]

        for _ in range(num_tasks):
            owner = random.choice(users)
            title = fake.sentence(nb_words=4)
            description = fake.sentence(nb_words=10)
            status = random.choice(statuses)
            hours = random.uniform(1, 100)

            # Make the planned and actual dates timezone-aware
            planned_start_date = timezone.make_aware(fake.date_time_between(start_date="-2y", end_date="now"))
            planned_end_date = planned_start_date + timedelta(days=random.randint(1, 10))

            # Simulate actual start/end date with some variability
            actual_start_date = planned_start_date + timedelta(days=random.randint(-2, 2))
            actual_end_date = actual_start_date + timedelta(days=random.randint(1, 10))

            task = Task.objects.create(
                title=title,
                owner=owner,
                description=description,
                status=status,
                hours=hours,
                planned_start_date=planned_start_date,
                planned_end_date=planned_end_date,
                actual_start_date=actual_start_date,
                actual_end_date=actual_end_date,
                content=fake.text(),
            )

            # Add random tags to tasks
            task.tags.add(*random.sample(tags, k=random.randint(1, len(tags))))

            # Optionally create sub-tasks for each task
            if random.choice([True, False]):
                sub_task = Task.objects.create(
                    title=f"Subtask of {task.title}",
                    owner=owner,
                    description=f"Subtask description for {task.title}",
                    status=random.choice(statuses),
                    hours=random.uniform(1, 10),
                    content=fake.text(),
                )
                task.sub_tasks.add(sub_task)
