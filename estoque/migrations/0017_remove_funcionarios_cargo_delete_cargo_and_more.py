# Generated by Django 5.0.6 on 2024-05-18 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0016_cargo_alter_funcionarios_cargo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionarios',
            name='cargo',
        ),
        migrations.DeleteModel(
            name='Cargo',
        ),
        migrations.DeleteModel(
            name='Funcionarios',
        ),
    ]