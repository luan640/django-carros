# Generated by Django 4.2.11 on 2024-04-09 22:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=200)),
                ('factory_year', models.IntegerField()),
                ('model_year', models.IntegerField()),
                ('value', models.FloatField()),
                ('km', models.FloatField()),
                ('auction', models.BooleanField()),
                ('color', models.CharField(blank=True, choices=[('Az', 'Azul'), ('Am', 'Amarelo'), ('Ve', 'Verde'), ('Br', 'Branco'), ('Pr', 'Preto'), ('Vm', 'Vermelho'), ('N/A', 'N/A')], max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cars_brand', to='cars.brand')),
            ],
        ),
    ]
