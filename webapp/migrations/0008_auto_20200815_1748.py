# Generated by Django 3.0.5 on 2020-08-15 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20200815_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='webapp.Member'),
        ),
    ]
