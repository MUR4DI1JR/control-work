from django.core.management.base import BaseCommand, CommandError
from realEstate.models import RealEstate
from faker import Faker
import random

class Command(BaseCommand):
	help = 'Command to generate data for database'

	def handle(self, *args, **kwargs):
		fake = Faker(['ru_RU'])

		for _ in range(30):
			try:
				title = fake.sentence(nb_words=10)
				text = fake.paragraph(nb_sentences=6)
				phone_number = fake.phone_number()
				owner_name = fake.name()
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
					rating = rating,
					address = address,
					number_of_rooms = number_of_rooms,
					area = area,
					furnuture = furnuture,
					city = city,
				)
			except:
				print('Error')
				continue
