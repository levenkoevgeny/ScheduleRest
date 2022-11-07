# Generated by Django 3.2.8 on 2022-11-07 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_groupunit'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='schedule.groupunit', verbose_name=' Group unit'),
            preserve_default=False,
        ),
    ]