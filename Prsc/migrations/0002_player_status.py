# Generated by Django 5.2.1 on 2025-06-13 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prsc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10),
        ),
    ]
