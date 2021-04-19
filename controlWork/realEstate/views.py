from django.shortcuts import render
from .models import RealEstate

def real_estate(request):
	real_Estate = RealEstate.objects.all()
	return render(request, 'realestate/listRealEstate.html', {'real_estate': real_Estate})

