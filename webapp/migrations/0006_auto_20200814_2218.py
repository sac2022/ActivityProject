# Generated by Django 3.0.5 on 2020-08-14 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20200813_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_periods', to='webapp.Member'),
        ),
    ]
