# Generated by Django 4.1.5 on 2023-01-30 21:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2)])),
                ('first_name', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[A-Z].*', 'Your name must start with a capital letter!')])),
                ('last_name', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[A-Z].*', 'Your name must start with a capital letter!')])),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_type', models.CharField(choices=[('Outdoor Plants', 'Outdoor Plants'), ('Indoor Plants', 'Indoor Plants')], max_length=14)),
                ('name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.RegexValidator('[a-zA-Z]', 'Plant name should contain only letters!')])),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('to_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plants.profile')),
            ],
        ),
    ]