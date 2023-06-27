# Generated by Django 4.2.2 on 2023-06-23 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainname', models.CharField(max_length=30, null=True)),
                ('train_no', models.IntegerField(null=True)),
                ('from_city', models.CharField(max_length=30, null=True)),
                ('to_city', models.CharField(max_length=30, null=True)),
                ('departuretime', models.CharField(max_length=30, null=True)),
                ('arrivaltime', models.CharField(max_length=30, null=True)),
                ('trevaltime', models.CharField(max_length=100, null=True)),
                ('distance', models.IntegerField(null=True)),
                ('img', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Asehi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fare', models.IntegerField(null=True)),
                ('train_name', models.CharField(max_length=30, null=True)),
                ('date3', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('add', models.CharField(max_length=100, null=True)),
                ('dob', models.DateField(null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=30, null=True)),
                ('route', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(max_length=30, null=True)),
                ('date1', models.DateField(null=True)),
                ('fare', models.IntegerField(null=True)),
                ('train', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='railway.add_train')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='railway.register')),
            ],
        ),
        migrations.CreateModel(
            name='Book_ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', models.CharField(max_length=100, null=True)),
                ('date2', models.DateField(null=True)),
                ('fare', models.IntegerField(null=True)),
                ('passenger', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='railway.passenger')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='railway.register')),
            ],
        ),
        migrations.CreateModel(
            name='Add_route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', models.CharField(max_length=100, null=True)),
                ('distance', models.IntegerField(null=True)),
                ('fare', models.IntegerField(null=True)),
                ('train', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='railway.add_train')),
            ],
        ),
    ]
