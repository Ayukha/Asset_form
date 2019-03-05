# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views import View
from .forms import ProfileForm
from django.http import HttpResponse
from .models import Profile
from django.contrib import messages



class ContactView(View):

    def get(self, request):
        form = ProfileForm()
        return render(request, 'form_template.html', {'form': form})

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES) 
  
        if form.is_valid():

            form.save()
            messages.success(request, 'Updated successfully!')
        else:
        	messages.warning(request, 'Please correct the error below.')
        return render(request, 'form_template.html', {'form': form})
