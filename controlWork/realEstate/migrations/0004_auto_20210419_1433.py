# Generated by Django 3.2 on 2021-04-19 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realEstate', '0003_auto_20210416_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adcategory',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
