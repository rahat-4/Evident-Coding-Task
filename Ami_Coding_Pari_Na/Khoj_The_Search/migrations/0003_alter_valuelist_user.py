# Generated by Django 4.1.3 on 2022-11-07 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Khoj_The_Search', '0002_alter_valuelist_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valuelist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payload', to=settings.AUTH_USER_MODEL),
        ),
    ]
