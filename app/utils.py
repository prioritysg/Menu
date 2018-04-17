from app.models import UserGroup


def add_user_regular_group(user):
    group, _ = UserGroup.objects.get_or_create(user_type=UserGroup.REGULAR)
    group.users.add(user)


def perform_search(organizations, request):
    if request.POST and request.POST.get('search'):
        search = request.POST.get('search')
        return organizations.filter(org_id__icontains=search).order_by('-id')
    return organizations
