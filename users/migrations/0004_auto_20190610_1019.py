# Generated by Django 2.1.7 on 2019-06-10 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190609_0838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='cityname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='country_of_birth',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='mobilenumber',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='streetname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='zip',
        ),
        migrations.AlterField(
            model_name='application',
            name='howdidyouhear',
            field=models.CharField(blank=True, choices=[('FACEBOOK', 'FACEBOOK'), ('NEWS', 'NEWS'), ('FRIENDS', 'FRIENDS'), ('RADIO', 'RADIO')], default='FACEBOOK', help_text='How did you hear about us?', max_length=20, verbose_name='How did you heard about us?'),
        ),
        migrations.AlterField(
            model_name='application',
            name='progoption',
            field=models.CharField(blank=True, choices=[('HOMESTUDY', 'HOMESTUDY'), ('SPED', 'SPED'), ('GRADE SCHOOL', 'GRADE SCHOOL'), ('CASA', 'CASA'), ('HIGH SCHOOL', 'HIGH SCHOOL')], default='CASA', help_text='Please select Program', max_length=20, verbose_name='Program Option'),
        ),
    ]
