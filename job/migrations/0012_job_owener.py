# Generated by Django 4.2.3 on 2023-07-22 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0011_apply_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='owener',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='job_owner', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
