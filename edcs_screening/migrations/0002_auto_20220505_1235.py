# Generated by Django 3.1.7 on 2022-05-05 12:35

from django.db import migrations, models
import edcs_model.models.fields.other_charfield


class Migration(migrations.Migration):

    dependencies = [
        ('edcs_screening', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalsubjectscreening',
            name='nationality',
            field=models.CharField(choices=[('tanzanian', 'Tanzanian'), ('ugandan', 'Ugandan'), ('OTHER', 'Other')], default='null', max_length=60, verbose_name='Nationality'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalsubjectscreening',
            name='nationality_other',
            field=edcs_model.models.fields.other_charfield.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If other, please specify ...'),
        ),
        migrations.AddField(
            model_name='subjectscreening',
            name='nationality',
            field=models.CharField(choices=[('tanzanian', 'Tanzanian'), ('ugandan', 'Ugandan'), ('OTHER', 'Other')], default='null', max_length=60, verbose_name='Nationality'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subjectscreening',
            name='nationality_other',
            field=edcs_model.models.fields.other_charfield.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If other, please specify ...'),
        ),
    ]
