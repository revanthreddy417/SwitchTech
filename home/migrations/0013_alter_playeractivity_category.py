# Generated by Django 4.1.6 on 2023-07-11 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_playeractivity_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playeractivity',
            name='category',
            field=models.CharField(default='Null', max_length=50),
        ),
    ]
