# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login_reg_app.models import User
from .models import *


# ======================================================
#                      RENDER
# ======================================================

def index(req):
    if 'user_id' not in req.session:
        return redirect('/')

    user_id = req.session['user_id']
    me = User.objects.get(id = user_id)
    other = Interest.objects.excludingUser(user_id)

    data = {
        'logged_user': me,
        'other_interests': other
    }

    return render(req, 'relationships/home.html', data)


# ======================================================
#                      Process
# ======================================================


def new(req):
    Interest.objects.new(req.POST)
    return redirect('/relationships')

def add(req):
    Interest.objects.add(req.POST, req.session['user_id'])
    return redirect('/relationships')

def delete(req, interest_id):
    Interest.objects.delete(interest_id, req.session['user_id'])
    return redirect('/relationships')