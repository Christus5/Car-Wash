# Generated by Django 3.1.5 on 2021-01-31 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('washapp', '0006_auto_20210131_0345'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='share',
            field=models.PositiveSmallIntegerField(default=45),
        ),
    ]
