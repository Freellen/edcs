# Generated by Django 3.1.7 on 2022-09-15 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edcs_lists', '0008_auto_20220915_0311'),
        ('edcs_subject', '0039_auto_20220915_0242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicaloccupationalhistory',
            name='industries_worked',
        ),
        migrations.RemoveField(
            model_name='occupationalhistory',
            name='industries_worked',
        ),
        migrations.AddField(
            model_name='occupationalhistory',
            name='industries_worked',
            field=models.ManyToManyField(to='edcs_lists.Industries', verbose_name='If yes, what kind of industry did you work?'),
        ),
    ]
