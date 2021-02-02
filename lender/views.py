from .models import LoanPlans
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.core.management import call_command
from django.core.management.commands import loaddata
import os

class HomeView(View):
    _template_name = 'home.html'
    plans = LoanPlans.objects.all()

    def get(self, request):
        return render(request, self._template_name, {'plans': self.plans})

    def post(self, request):

        self.budget = int(request.POST['budget'])

        # If reset_db is set
        if 'reset_db' in request.POST:
            call_command('loaddata', 'db_instance', verbosity=0)
        else:
            # numpy.optimize.lingprog(), simplex method here for optimization
            pass

        return render(request, self._template_name,
                    {'plans':  self.plans})