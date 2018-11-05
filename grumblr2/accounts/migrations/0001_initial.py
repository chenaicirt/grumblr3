# Generated by Django 2.1.1 on 2018-10-07 02:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('bio', models.CharField(default='', max_length=100)),
                ('age', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='profile_image')),
            ],
        ),
    ]