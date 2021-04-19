from django.shortcuts import render
from django.db.models import Q
from .models import RealEstate

def real_estate(request):
	real_Estate = RealEstate.objects.all()
	search_estate = request.GET.get('search_estate', '')

	if search_estate:
		real_Estate = RealEstate.objects.filter(Q(name = search_estate) | Q(type = search_estate))
	else:
		real_Estate = RealEstate.objects.all()

	return render(request, 'realestate/listRealEstate.html', {'real_estate': real_Estate, 'search_estate': search_estate})
