# Generated by Django 4.0.6 on 2022-07-15 08:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('streets', '0001_initial'),
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('house', models.CharField(max_length=10)),
                ('timeopen', models.IntegerField()),
                ('timeclose', models.IntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cities.city')),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='streets.street')),
            ],
        ),
    ]
