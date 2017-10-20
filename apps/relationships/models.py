# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_reg_app.models import User

class InterestManager(models.Manager):
    def new(self, post):
        name = post['name'].lower()
        if not self.filter(name = name).exists():
            self.create(name = name)

    def add(self, post, user_id):
        interests = self.filter(id=post['interest_id'])
        if interests:
            interest = interests[0]
            user = User.objects.get(id=user_id)
            user.interests.add(interest)

    def excludingUser(self, user_id):
        me = User.objects.get(id = user_id)
        my_interests_ids = me.interests.all().values_list('id', flat=True)
        return self.all().exclude(id__in=my_interests_ids)

    def delete(self, interest_id, user_id):
        user = User.objects.get(id=user_id)
        interests = self.filter(id=interest_id)
        if interests:
            interest = interests[0]
            user.interests.remove(interest)
            # interest.users.remove(user)

class Interest(models.Model):
    name = models.CharField(max_length=32)
    users = models.ManyToManyField(User, related_name='interests')
    objects = InterestManager()
