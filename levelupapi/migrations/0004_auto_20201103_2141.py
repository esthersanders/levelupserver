# Generated by Django 3.1.2 on 2020-11-03 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0003_auto_20201103_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_game', to='levelupapi.game'),
        ),
    ]