# Generated by Django 4.0 on 2022-06-23 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sys_admin', '0001_initial'),
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='resume', to='sys_admin.employee'),
        ),
    ]
