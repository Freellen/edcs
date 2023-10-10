# Generated by Django 3.1.7 on 2022-05-06 10:06

from django.db import migrations, models
import edcs_model.models.fields.other_charfield


class Migration(migrations.Migration):

    dependencies = [
        ('edcs_lists', '0004_auto_20220506_0956'),
        ('edcs_subject', '0015_auto_20220506_0956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='covidinfectionhistory',
            old_name='other_vaccine_provider',
            new_name='covid_vaccine_other',
        ),
        migrations.RenameField(
            model_name='historicalcovidinfectionhistory',
            old_name='other_vaccine_provider',
            new_name='covid_vaccine_other',
        ),
        migrations.AddField(
            model_name='covidinfectionhistory',
            name='vaccine_provider_other',
            field=edcs_model.models.fields.other_charfield.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If other, please specify ...'),
        ),
        migrations.AddField(
            model_name='historicalcovidinfectionhistory',
            name='vaccine_provider_other',
            field=edcs_model.models.fields.other_charfield.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If other, please specify ...'),
        ),
        migrations.AlterField(
            model_name='covidinfectionhistory',
            name='covid_vaccine',
            field=models.ManyToManyField(blank=True, null=True, to='edcs_lists.CovidVaccine', verbose_name='If yes, what type of vaccination'),
        ),
    ]