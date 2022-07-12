# Generated by Django 3.0.5 on 2022-07-11 11:21

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
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/Donor/')),
                ('bloodgroup', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BloodDonate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(default='Nothing', max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('bloodgroup', models.CharField(max_length=10)),
                ('unit', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('date', models.DateField(auto_now=True)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donor.Donor')),
            ],
        ),
    ]
