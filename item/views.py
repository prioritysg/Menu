from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/login/')
def items(request):
    return render(request, 'items.html', {'tab': 'item'})


@login_required(login_url='/login/')
def item_details(request):
    return render(request, 'item_details.html', {'tab': 'item_details'})
