from app.models import UserGroup


def add_user_regular_group(user):
    group, _ = UserGroup.objects.get_or_create(user_type=UserGroup.REGULAR)
    group.users.add(user)
