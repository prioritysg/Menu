from django.core.management.base import BaseCommand
from app.models import UserGroup, GroupAccess


class Command(BaseCommand):
    help = "Adding Init data"

    def handle(self, *args, **options):
        UserGroup.objects.create(user_type=UserGroup.ADMIN)
        UserGroup.objects.create(user_type=UserGroup.ASSISTANT)
        UserGroup.objects.create(user_type=UserGroup.MANAGER)
        UserGroup.objects.create(user_type=UserGroup.REGULAR)
        UserGroup.objects.create(user_type=UserGroup.CLIENT)

        groups = UserGroup.objects.all()

        GroupAccess.objects.create(user_group=groups[0])
        GroupAccess.objects.create(user_group=groups[1])
        GroupAccess.objects.create(user_group=groups[2])
        GroupAccess.objects.create(user_group=groups[3])
        GroupAccess.objects.create(user_group=groups[4])
