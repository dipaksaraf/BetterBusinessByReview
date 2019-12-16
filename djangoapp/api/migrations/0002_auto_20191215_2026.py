# Generated by Django 3.0 on 2019-12-16 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='high_rating_score',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='low_rating_score',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
    ]
