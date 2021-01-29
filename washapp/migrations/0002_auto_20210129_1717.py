# Generated by Django 3.1.5 on 2021-01-29 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('washapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boothtocompany',
            name='booth',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='washapp.carwashbooth'),
        ),
        migrations.AlterField(
            model_name='employeetocompany',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='washapp.employee'),
        ),
        migrations.AlterField(
            model_name='ordertocompany',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='washapp.order'),
        ),
    ]
