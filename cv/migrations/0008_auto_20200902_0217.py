# Generated by Django 2.2.15 on 2020-09-02 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0007_auto_20200902_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='proficiency',
            field=models.IntegerField(blank=True, choices=[(1, '1/5'), (2, '2/5'), (3, '3/5'), (4, '4/5'), (5, '5/5')], null=True),
        ),
    ]
