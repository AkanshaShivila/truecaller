# Generated by Django 4.0.2 on 2022-03-03 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truecaller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone_no',
            field=models.CharField(max_length=50),
        ),
    ]