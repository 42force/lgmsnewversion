# Generated by Django 2.1.7 on 2019-06-10 03:07

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import lgmssis.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('lgmssis', '0004_auto_20190610_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', lgmssis.models.IntegerRangeField(help_text='Example 2014', unique=True)),
                ('full_name', models.CharField(blank=True, help_text='Example Class of 2014', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ReasonLeft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FamilyAccessUser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'permissions': (('view_ssn_student', 'View student lrn_no'), ('view_mentor_student', 'View mentoring information student'), ('reports', 'View reports'))},
        ),
        migrations.AddField(
            model_name='student',
            name='bday',
            field=models.DateField(blank=True, null=True, verbose_name='Birth Date'),
        ),
        migrations.AddField(
            model_name='student',
            name='date_dismissed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='grad_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='parent_email',
            field=models.EmailField(blank=True, editable=False, max_length=254),
        ),
        migrations.AddField(
            model_name='student',
            name='parent_guardian',
            field=models.CharField(blank=True, editable=False, max_length=150),
        ),
        migrations.AddField(
            model_name='student',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='siblings',
            field=models.ManyToManyField(blank=True, to='lgmssis.Student'),
        ),
        migrations.AddField(
            model_name='student',
            name='streetname',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Street Name'),
        ),
        migrations.AddField(
            model_name='student',
            name='unique_id',
            field=models.IntegerField(blank=True, help_text='For integration with outside databases', null=True, unique=True),
        ),
        migrations.AddField(
            model_name='student',
            name='zip',
            field=models.CharField(blank=True, editable=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='howdidyouhear',
            field=models.CharField(blank=True, choices=[('HOMESTUDY', 'HOMESTUDY'), ('HIGH SCHOOL', 'HIGH SCHOOL'), ('SPED', 'SPED'), ('GRADE SCHOOL', 'GRADE SCHOOL'), ('CASA', 'CASA')], default='FACEBOOK', help_text='How did you hear about us?', max_length=20),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='progoption',
            field=models.CharField(blank=True, choices=[('HOMESTUDY', 'HOMESTUDY'), ('HIGH SCHOOL', 'HIGH SCHOOL'), ('SPED', 'SPED'), ('GRADE SCHOOL', 'GRADE SCHOOL'), ('CASA', 'CASA')], default='CASA', help_text='Please select Program', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lgmssis.GradeLevel'),
        ),
        migrations.AddField(
            model_name='student',
            name='class_of_year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lgmssis.ClassYear'),
        ),
        migrations.AddField(
            model_name='student',
            name='reason_left',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lgmssis.ReasonLeft'),
        ),
    ]
