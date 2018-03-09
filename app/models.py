from django.contrib.auth.models import User
from django.db import models


class UserGroup(models.Model):
    ADMIN = 'admin'
    MANAGER = 'manager'
    ASSISTANT = 'assistant'
    REGULAR = 'regular'
    CLIENT = 'client'

    USER_TYPES = (
        (ADMIN, 'Admin User'),
        (MANAGER, 'Manager User'),
        (ASSISTANT, 'Assistant User'),
        (REGULAR, 'Regular User'),
        (CLIENT, 'Client User'),

    )

    users = models.ManyToManyField(User)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default=REGULAR)

    def __str__(self):
        return self.user_type


class GroupAccess(models.Model):
    NO_ACCESS = '0'
    READ = 'R'
    READ_WRITE = 'RW'
    ACCESSES = (
        (NO_ACCESS, 'No Access'),
        (READ, 'Read'),
        (READ_WRITE, 'Read Write'),
    )
    user_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)
    receiving = models.CharField(max_length=5, choices=ACCESSES, default=NO_ACCESS)
    shipping = models.CharField(max_length=5, choices=ACCESSES, default=NO_ACCESS)
    mobile = models.CharField(max_length=5, choices=ACCESSES, default=NO_ACCESS)
    inventory = models.CharField(max_length=5, choices=ACCESSES, default=NO_ACCESS)
    items = models.CharField(max_length=5, choices=ACCESSES, default=NO_ACCESS)
    reports = models.CharField(max_length=5, choices=ACCESSES, default=NO_ACCESS)
    organization = models.CharField(max_length=5, choices=ACCESSES, default=NO_ACCESS)
    security = models.CharField(max_length=5, choices=ACCESSES, default=NO_ACCESS)
    client = models.CharField(max_length=5, choices=ACCESSES, default=NO_ACCESS)

    def __str__(self):
        return self.user_group.user_type
