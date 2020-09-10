# Generated by Django 3.1.1 on 2020-09-10 16:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skn_professionals', '0002_professionalprofile_recommendprofessional'),
    ]

    operations = [
        migrations.AddField(
            model_name='professionalprofile',
            name='institution',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='professionalprofile',
            name='other_field_of_expertise_name',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='professionalprofile',
            name='region_of_residence',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='professionalprofile',
            name='specialties_under_expertise',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='professionalprofile',
            name='job_description',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='professionalprofile',
            name='languages_spoken',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='professionalprofile',
            name='profile',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='professionalprofile',
            name='town_or_city_of_residence',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='RequesterProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requester_full_name', models.CharField(max_length=150)),
                ('requester_organization', models.CharField(max_length=60)),
                ('requester_phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('requester_website', models.CharField(max_length=60)),
                ('requester_photo_id', models.ImageField(upload_to='')),
                ('referee_one_full_name', models.CharField(blank=True, max_length=60, null=True)),
                ('referee_one_phone_number', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('referee_one_email', models.EmailField(blank=True, max_length=150, null=True)),
                ('referee_one_social_media_handle', models.CharField(blank=True, max_length=150, null=True)),
                ('referee_one_workplace', models.CharField(blank=True, max_length=60, null=True)),
                ('referee_two_full_name', models.CharField(blank=True, max_length=60, null=True)),
                ('referee_two_phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('referee_two_email', models.EmailField(blank=True, max_length=150, null=True)),
                ('referee_two_social_media_handle', models.CharField(blank=True, max_length=150, null=True)),
                ('referee_two_workplace', models.CharField(blank=True, max_length=60, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
