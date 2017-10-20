# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def login(self, post):

        email = post['email'].lower()
        password = post['password']

        users = User.objects.filter(email = email)
        if len(users):
            user = users[0]
            if user.password == password:
                return user

        return False

    def userIsValid(self, post):
        email = post['email'].lower()
        password = post['password']
        cpassword = post['cpassword']
        errors = []

        if len(email) < 6 or len(email) > 32:
            errors.append('Email must be 6-32 characters')

        if len(password) < 8:
            errors.append('Password must be more then 8 characters long')
        elif password != cpassword:
            errors.append('Passwords are not equal')

        if not errors:
            users = self.filter(email=email)
            if users:
                errors.append('Email invalid')

        return {'status': len(errors) == 0, 'errors':errors}


    def newUser(self, post):
        email = post['email'].lower()
        password = post['password']
        return self.create(email = email, password = password)


# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=32)
    password = models.CharField(max_length=255)
    objects = UserManager()
    def __str__(self):
        return "email: {}".format(self.email)
    def __repr__(self):
        return self.__str__()