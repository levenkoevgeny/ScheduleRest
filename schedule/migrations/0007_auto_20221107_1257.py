# Generated by Django 3.2.8 on 2022-11-07 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_group_group_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='First name'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='patronymic',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Patronymic'),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='schedule.groupunit', verbose_name=' Group unit'),
        ),
    ]
