# Generated by Django 2.1.7 on 2019-06-08 14:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lgmssis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=255, null=True, verbose_name='First Name')),
                ('lname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last Name')),
                ('streetname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Street Name')),
                ('cityname', models.CharField(blank=True, max_length=255, null=True, verbose_name='City Name')),
                ('zip', models.IntegerField(blank=True, null=True, verbose_name='Zip Code')),
                ('mobilenumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='MOBILE FORMAT : +639178888888', max_length=128, verbose_name='Mobile Number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('progoption', models.CharField(blank=True, choices=[('SPED', 'SPED'), ('GRADE SCHOOL', 'GRADE SCHOOL'), ('HOMESTUDY', 'HOMESTUDY'), ('CASA', 'CASA'), ('HIGH SCHOOL', 'HIGH SCHOOL')], default='CASA', help_text='Please select Program', max_length=20, verbose_name='Program Option')),
                ('howdidyouhear', models.CharField(blank=True, choices=[('FACEBOOK', 'FACEBOOK'), ('FRIENDS', 'FRIENDS'), ('RADIO', 'RADIO'), ('NEWS', 'NEWS')], default='FACEBOOK', help_text='How did you hear about us?', max_length=20, verbose_name='How did you heard about us?')),
                ('country_of_birth', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lgmssis.CountryOption')),
            ],
        ),
        migrations.CreateModel(
            name='ParentsProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio_parents', models.TextField(blank=True, max_length=500)),
                ('image_parents', models.ImageField(default='default.jpg', upload_to='profile_pics_parents')),
                ('streetname_parents', models.CharField(blank=True, max_length=255, null=True, verbose_name='Street Name')),
                ('cityname_parents', models.CharField(blank=True, max_length=255, null=True, verbose_name='City Name')),
                ('zip_parents', models.IntegerField(blank=True, null=True, verbose_name='Zip Code')),
                ('mobilenumber_parents', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='MOBILE FORMAT : +639178888888', max_length=128, verbose_name='Mobile Number')),
                ('birth_date_parents', models.DateField(default=datetime.date.today, verbose_name='Date of Birth')),
                ('country_of_birth_parents', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lgmssis.CountryOption')),
                ('user_parents', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('streetname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Street Name')),
                ('cityname', models.CharField(blank=True, max_length=255, null=True, verbose_name='City Name')),
                ('zip', models.IntegerField(blank=True, null=True, verbose_name='Zip Code')),
                ('mobilenumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='MOBILE FORMAT : +639178888888', max_length=128, verbose_name='Mobile Number')),
                ('birth_date', models.DateField(default=datetime.date.today, verbose_name='Date of Birth')),
                ('country_of_birth', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lgmssis.CountryOption')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_student', models.ImageField(default='default.jpg', upload_to='profile_pics_student')),
                ('lrn_no', models.CharField(blank=True, default='', max_length=64, verbose_name='Learners Number')),
                ('birth_date', models.DateField(default=datetime.date.today, verbose_name='Date of Birth')),
                ('country_of_birth', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lgmssis.CountryOption')),
                ('user_student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeachersProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_teachers', models.ImageField(default='default.jpg', upload_to='profile_pics_teachers')),
                ('faculty_id', models.IntegerField(default='1234', verbose_name='Faculty ID No.')),
                ('bio_teachers', models.TextField(blank=True, max_length=500)),
                ('user_teachers', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
