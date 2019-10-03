# Generated by Django 2.2.6 on 2019-10-03 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=255)),
                ('edad', models.IntegerField()),
                ('telefono', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('edad', models.IntegerField()),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Persona')),
            ],
        ),
    ]
