from django.core.management.base import BaseCommand, CommandError
from realEstate.models import RealEstate, AdCategory
from faker import Faker
import random


CATEGORIES = [
	'Покупка-Продажа',
	'Аренда',
]


class Command(BaseCommand):
	help = 'Command to generate data for database'

	def handle(self, *args, **kwargs):
		fake = Faker(['ru_RU'])

		for category in CATEGORIES:
			AdCategory.objects.create(name = category)

		for _ in range(30):
			try:
				title = fake.sentence(nb_words=10)
				text = fake.paragraph(nb_sentences=6)
				phone_number = fake.phone_number()
				owner_name = fake.name()
				price = random.randint(2000,100000)
				estate_type = random.choice(RealEstate.ESTATE_TYPES)[0]
				rating = random.randint(1,6)
				address = fake.address()
				number_of_rooms = random.randint(1,6)
				area = number_of_rooms * random.randint(100, 300)/10
				furnuture = random.choice([True, False])
				city = fake.city()
				RealEstate.objects.create(
					title = title,
					text = text,
					phone_number = phone_number,
					owner_name = owner_name,
					price = price,
					estate_type = estate_type,
					rating = rating,
					address = address,
					number_of_rooms = number_of_rooms,
					area = area,
					furnuture = furnuture,
					city = city,
					category_id = random.randint(1,2)
				)
			except:
				print('Error')
				continue
