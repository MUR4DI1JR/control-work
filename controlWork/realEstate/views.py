from django.shortcuts import render
from django.db.models import Q
from .models import RealEstate

def real_estate(request):
	real_estate = RealEstate.objects.all()
	search_text = request.GET.get('search-text', '')
	search_price_min = request.GET.get('search-price-min', '')
	search_price_max = request.GET.get('search-price-max', '')
	search_type = request.GET.get('search-type', '')
	search_rooms = request.GET.get('search-rooms', '')
	search_furniture = request.GET.get('search-furniture', '')
	search_category = request.GET.get('search-category', '')

	if search-text:
		real_estate = real_estate.filter(Q(title__icontains = search_estate) | Q(text__icontains = search_estate))

	if search_price_min:
		real_estate = real_estate.filter(price__gte = int(search_price_min))

	if search_price_max:
		real_estate = real_estate.filter(price__gte = int(search_price_max))

	if search_type:
		real_estate = real_estate.filter(estate_type = search_type)

	if search_furniture:
		real_estate = real_estate.filter(furnuture = search-furniture)

	if search_rooms:
		real_estate = real_estate.filter(number_of_rooms = search_rooms)

	if search_price_max:
		real_estate = real_estate.filter(price__gte = int(search_price_max))


	return render(request, 'realestate/listRealEstate.html', {'real_estate': real_estate, 'search_estate': search_estate})


def detailsRealEstate(request, id):
	estate = RealEstate.objects.get(id = id)
	context = {
		"estate": estate
	}
	return render(request, 'realestate/detailsRealEstate.html', context)

