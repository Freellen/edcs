# Generated by Django 4.2 on 2024-01-30 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("edcs_subject", "0003_alter_diagnostictests_culture_a_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="diagnostictests",
            name="culture_a",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("positive", "positive"),
                    ("negative", "negative"),
                    ("no_result", "no result"),
                ],
                max_length=45,
                verbose_name="Culture MGIT/LJ",
            ),
        ),
        migrations.AlterField(
            model_name="diagnostictests",
            name="culture_b",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("positive", "positive"),
                    ("negative", "negative"),
                    ("no_result", "no result"),
                ],
                max_length=45,
                verbose_name="Culture MGIT/LJ",
            ),
        ),
        migrations.AlterField(
            model_name="diagnostictests",
            name="mods_a",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("positive", "positive"),
                    ("negative", "negative"),
                    ("no_result", "no result"),
                ],
                max_length=45,
                verbose_name="MODS",
            ),
        ),
        migrations.AlterField(
            model_name="diagnostictests",
            name="mods_b",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("positive", "positive"),
                    ("negative", "negative"),
                    ("no_result", "no result"),
                ],
                max_length=45,
                verbose_name="MODS",
            ),
        ),
        migrations.AlterField(
            model_name="diagnostictests",
            name="other_test_result_a",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("positive", "positive"),
                    ("negative", "negative"),
                    ("no_result", "no result"),
                ],
                max_length=45,
                verbose_name="Test result",
            ),
        ),
        migrations.AlterField(
            model_name="diagnostictests",
            name="other_test_result_b",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("positive", "positive"),
                    ("negative", "negative"),
                    ("no_result", "no result"),
                ],
                max_length=45,
                verbose_name="Test result",
            ),
        ),
        migrations.AlterField(
            model_name="diagnostictests",
            name="smear_microscopy_a",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("positive", "positive"),
                    ("negative", "negative"),
                    ("no_result", "no result"),
                ],
                max_length=45,
                verbose_name="Smear microscopy\tdirect ZN/FM",
            ),
        ),
        migrations.AlterField(
            model_name="diagnostictests",
            name="smear_microscopy_b",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("positive", "positive"),
                    ("negative", "negative"),
                    ("no_result", "no result"),
                ],
                max_length=45,
                verbose_name="Smear microscopy\tdirect ZN/FM",
            ),
        ),
        migrations.AlterField(
            model_name="diagnostictests",
            name="truenat_mtb_plus_a",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("positive", "positive"),
                    ("negative", "negative"),
                    ("no_result", "no result"),
                ],
                max_length=45,
                verbose_name="Truenat MTB Plus",
            ),
        ),
        migrations.AlterField(
            model_name="diagnostictests",
            name="truenat_mtb_plus_b",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("positive", "positive"),
                    ("negative", "negative"),
                    ("no_result", "no result"),
                ],
                max_length=45,
                verbose_name="Truenat MTB Plus",
            ),
        ),
        migrations.AlterField(
            model_name="diagnostictests",
            name="xpert_mtb_rif_a",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("positive", "positive"),
                    ("negative", "negative"),
                    ("no_result", "no result"),
                ],
                max_length=45,
                verbose_name="Xpert MTB/RIF (Ultra)",
            ),
        ),
        migrations.AlterField(
            model_name="diagnostictests",
            name="xpert_mtb_rif_b",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("positive", "positive"),
                    ("negative", "negative"),
                    ("no_result", "no result"),
                ],
                max_length=45,
                verbose_name="Xpert MTB/RIF (Ultra)",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldiagnostictests",
            name="culture_a",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("positive", "positive"),
                    ("negative", "negative"),
                    ("no_result", "no result"),
                ],
                max_length=45,
                verbose_name="Culture MGIT/LJ",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldiagnostictests",
            name="culture_b",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("positive", "positive"),
                    ("negative", "negative"),
                    ("no_result", "no result"),
                ],
                max_length=45,
                verbose_name="Culture MGIT/LJ",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldiagnostictests",
            name="mods_a",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("positive", "positive"),
                    ("negative", "negative"),
                    ("no_result", "no result"),
                ],
                max_length=45,
                verbose_name="MODS",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldiagnostictests",
            name="mods_b",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("positive", "positive"),
                    ("negative", "negative"),
                    ("no_result", "no result"),
                ],
                max_length=45,
                verbose_name="MODS",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldiagnostictests",
            name="other_test_result_a",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("positive", "positive"),
                    ("negative", "negative"),
                    ("no_result", "no result"),
                ],
                max_length=45,
                verbose_name="Test result",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldiagnostictests",
            name="other_test_result_b",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("positive", "positive"),
                    ("negative", "negative"),
                    ("no_result", "no result"),
                ],
                max_length=45,
                verbose_name="Test result",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldiagnostictests",
            name="smear_microscopy_a",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("positive", "positive"),
                    ("negative", "negative"),
                    ("no_result", "no result"),
                ],
                max_length=45,
                verbose_name="Smear microscopy\tdirect ZN/FM",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldiagnostictests",
            name="smear_microscopy_b",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("positive", "positive"),
                    ("negative", "negative"),
                    ("no_result", "no result"),
                ],
                max_length=45,
                verbose_name="Smear microscopy\tdirect ZN/FM",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldiagnostictests",
            name="truenat_mtb_plus_a",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("positive", "positive"),
                    ("negative", "negative"),
                    ("no_result", "no result"),
                ],
                max_length=45,
                verbose_name="Truenat MTB Plus",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldiagnostictests",
            name="truenat_mtb_plus_b",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("positive", "positive"),
                    ("negative", "negative"),
                    ("no_result", "no result"),
                ],
                max_length=45,
                verbose_name="Truenat MTB Plus",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldiagnostictests",
            name="xpert_mtb_rif_a",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("positive", "positive"),
                    ("negative", "negative"),
                    ("no_result", "no result"),
                ],
                max_length=45,
                verbose_name="Xpert MTB/RIF (Ultra)",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldiagnostictests",
            name="xpert_mtb_rif_b",
            field=models.CharField(
                choices=[
                    ("N/A", "Not applicable"),
                    ("positive", "positive"),
                    ("negative", "negative"),
                    ("no_result", "no result"),
                ],
                max_length=45,
                verbose_name="Xpert MTB/RIF (Ultra)",
            ),
        ),
    ]
