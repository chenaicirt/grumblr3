# Generated by Django 2.1.1 on 2018-10-07 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20181007_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_image'),
        ),
    ]
