#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path

from .views import index, contato

urlpatterns = [
    path('', index),
    path('contato', contato),
]