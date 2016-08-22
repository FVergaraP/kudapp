# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-12 20:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kudapp', '0003_auto_20160812_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.IntegerField()),
                ('trabajo_visita', models.BooleanField()),
                ('recibe_efectivo', models.BooleanField()),
                ('recibe_transferencia', models.BooleanField()),
                ('tipo_servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kudapp.TipoServicio')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='fecha_nacimiento',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='servicio',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kudapp.User'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kudapp.Servicio'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kudapp.User'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kudapp.Servicio'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kudapp.User'),
        ),
    ]
