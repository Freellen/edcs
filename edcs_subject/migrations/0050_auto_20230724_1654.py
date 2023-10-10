# Generated by Django 3.1.7 on 2023-07-24 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edcs_subject', '0049_auto_20230702_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='demographiccharacteristic',
            name='occupation_details',
            field=models.CharField(blank=True, max_length=85, null=True, verbose_name='Provide more details about the above occupation?'),
        ),
        migrations.AddField(
            model_name='demographiccharacteristic',
            name='occupation_duration',
            field=models.DecimalField(decimal_places=3, help_text='Three month = 0.25, Six month = 0.5, One year = 1 , year and six month = 1.5 etc.', max_digits=6, null=True, verbose_name='How long have you been working on the above occupation?'),
        ),
        migrations.AddField(
            model_name='historicaldemographiccharacteristic',
            name='occupation_details',
            field=models.CharField(blank=True, max_length=85, null=True, verbose_name='Provide more details about the above occupation?'),
        ),
        migrations.AddField(
            model_name='historicaldemographiccharacteristic',
            name='occupation_duration',
            field=models.DecimalField(decimal_places=3, help_text='Three month = 0.25, Six month = 0.5, One year = 1 , year and six month = 1.5 etc.', max_digits=6, null=True, verbose_name='How long have you been working on the above occupation?'),
        ),
    ]