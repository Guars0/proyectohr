# Generated by Django 5.0.6 on 2024-06-05 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_departamento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departamento',
            old_name='id_depa',
            new_name='id',
        ),
    ]