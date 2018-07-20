from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied


from app.models import UserGroup, GroupAccess


def permission_required_for_item(perm, login_url=None, raise_exception=False):
    """
    Decorator for views that checks whether a user has a particular permission
    enabled, redirecting to the log-in page if necessary.
    If the raise_exception parameter is given the PermissionDenied exception
    is raised.
    """
    def check_perms(user):
        group = UserGroup.objects.filter(users=user).first()
        group_access = GroupAccess.objects.filter(user_group=group).first()
        if group_access:
            if group_access.__dict__.get(perm) == GroupAccess.READ:
                return True
            if raise_exception:
                raise PermissionDenied
        return False

    return user_passes_test(check_perms, login_url=login_url)
