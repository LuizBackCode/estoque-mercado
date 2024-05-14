# Generated by Django 5.0.6 on 2024-05-13 23:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_produto_quantidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnidadeMedida',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('unidade', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='produto',
            name='medida',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='medida_produto', to='estoque.unidademedida'),
            preserve_default=False,
        ),
    ]