# Generated by Django 4.1.6 on 2023-08-12 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reassessment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizquestion',
            name='code_snippet',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quizquestion',
            name='difficulty',
            field=models.CharField(choices=[('BG', 'Beginner'), ('IN', 'Intermediate'), ('AD', 'Advanced')], default='', max_length=2),
        ),
    ]
