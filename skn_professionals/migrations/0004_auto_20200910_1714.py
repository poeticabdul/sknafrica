# Generated by Django 3.1.1 on 2020-09-10 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skn_professionals', '0003_auto_20200910_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionalprofile',
            name='other_field_of_expertise_name',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]