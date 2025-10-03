import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from users.models import User
from collects.models import Collect
from payments.models import Payment

fake = Faker()

class Command(BaseCommand):
    help = 'Наполняет базу данными'

    def add_arguments(self, parser):
        parser.add_argument(
            '--users',
            type=int,
            default=10,
            help='Количество пользователей'
        )
        parser.add_argument(
            '--collects',
            type=int,
            default=100,
            help='Количество сборов'
        )
        parser.add_argument(
            '--payments',
            type=int,
            default=1000,
            help='Количество пожертвований'
        )

    def handle(self, *args, **options):
        user_count = options['users']
        collect_count = options['collects']
        payment_count = options['payments']

        users = []
        for _ in range(user_count):
            user = User(
                email=fake.unique.email(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                patronymic=fake.first_name()
            )
            users.append(user)
        User.objects.bulk_create(users)
        users = list(User.objects.all())

        reasons = [r[0] for r in Collect.ReasonChoices.choices]
        collects = []
        for _ in range(collect_count):
            collect = Collect(
                user=random.choice(users),
                name=fake.sentence(nb_words=4)[:Collect._meta.get_field('name').max_length],
                reason=random.choice(reasons),
                description=fake.text(max_nb_chars=200),
                total_goal_amount=random.randint(1000, 1000000),
                date_end=timezone.now() + timezone.timedelta(days=random.randint(1, 60)),
                target_amount=random.randint(1, 500)
            )
            collects.append(collect)
        Collect.objects.bulk_create(collects)
        collects = list(Collect.objects.all())

        payments = []
        for _ in range(payment_count):
            payment = Payment(
                user=random.choice(users),
                collect=random.choice(collects),
                amount=random.randint(10, 5000),
                is_anonymous=random.choice([True, False])
            )
            payments.append(payment)
        Payment.objects.bulk_create(payments)
