# Generated by Django 3.0.5 on 2020-04-15 23:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Restaurante', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Montaje', '0001_initial'),
        ('Salon', '0001_initial'),
        ('Contrato', '0001_initial'),
        ('Menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato_menu',
            name='Menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MenuContrato', to='Menu.Menu'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='Cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cliente', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contrato',
            name='Gerente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Gerente', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contrato',
            name='Menu',
            field=models.ManyToManyField(through='Contrato.Contrato_Menu', to='Menu.Menu'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='Montaje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Montaje', to='Montaje.Montaje'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='Restaurante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Restaurante', to='Restaurante.Restaurante'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='Salon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Salon', to='Salon.Salon'),
        ),
    ]
