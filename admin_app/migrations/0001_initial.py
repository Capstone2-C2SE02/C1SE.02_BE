# Generated by Django 5.0.3 on 2024-04-24 13:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='academic_intake_session',
            fields=[
                ('ACADEMIC_INTAKE_SESSION_ID', models.AutoField(primary_key=True, serialize=False)),
                ('ACADEMIC_INTAKE_SESSION_NAME', models.CharField(max_length=50)),
                ('START_DATE', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='academic_level_type',
            fields=[
                ('ACADEMIC_LEVEL_TYPE_ID', models.AutoField(primary_key=True, serialize=False)),
                ('ACADEMIC_LEVEL_TYPE_NAME', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='degree',
            fields=[
                ('DEGREE_ID', models.AutoField(primary_key=True, serialize=False)),
                ('DEGREE_NAME', models.CharField(max_length=50)),
                ('DEGREE_CODE', models.CharField(max_length=20)),
                ('DEGREE_STATUS', models.CharField(max_length=50)),
                ('DESCRIPTON', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='learning_status_type',
            fields=[
                ('LEARNING_STATUS_TYPE_ID', models.AutoField(primary_key=True, serialize=False)),
                ('LEARNING_STATUS_TYPE_NAME', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='academic_program',
            fields=[
                ('ACADEMIC_PROGRAM_ID', models.AutoField(primary_key=True, serialize=False)),
                ('ACADEMIC_PROGRAM_CODE', models.CharField(max_length=20)),
                ('ACADEMIC_PROGRAM_NAME', models.CharField(max_length=50)),
                ('MODE_OF_STUDY', models.CharField(max_length=50)),
                ('DEGREE_DURATION', models.CharField(max_length=50)),
                ('DESCRIPTION', models.CharField(max_length=255)),
                ('ACADEMIC_LEVEL_TYPE_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.academic_level_type')),
                ('DEGREE_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.degree')),
            ],
        ),
        migrations.CreateModel(
            name='curriculum',
            fields=[
                ('CURRICULUM_ID', models.AutoField(primary_key=True, serialize=False)),
                ('CURRICULUM_NAME', models.CharField(max_length=50)),
                ('DESCRIPTION', models.CharField(max_length=255)),
                ('CURRICULUM_STATUS_NAME', models.BooleanField(default=True)),
                ('ACADEMIC_PROGRAM_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.academic_program')),
            ],
        ),
        migrations.CreateModel(
            name='academic_intake_session_academic_program_curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STATUS_NAME', models.CharField(default=True, max_length=50)),
                ('ACADEMIC_INTAKE_SESSION_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.academic_intake_session')),
                ('ACADEMIC_PROGRAM_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.academic_program')),
                ('CURRICULUM_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.curriculum')),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('STUDENT_ID_NUMBER', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('LAST_NAME', models.CharField(max_length=20)),
                ('FIRST_NAME', models.CharField(max_length=20)),
                ('MIDDLE_NAME', models.CharField(max_length=20)),
                ('GENDER', models.BooleanField()),
                ('BIRTH_DATE', models.DateField()),
                ('BIRTH_PLACE', models.CharField(max_length=100)),
                ('PEOPLE_ID_NUMBER', models.CharField(max_length=50)),
                ('NATION', models.CharField(max_length=50)),
                ('NATIONALITY', models.CharField(max_length=50)),
                ('PHONE_NUMBER', models.CharField(max_length=50, null=True)),
                ('EMAIL', models.CharField(max_length=50, null=True)),
                ('COMMENTS', models.CharField(max_length=255)),
                ('LEARNING_STATUS_TYPE_ID', models.CharField(max_length=50)),
                ('ACADEMIC_LEVEL_TYPE_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.academic_level_type')),
            ],
        ),
        migrations.CreateModel(
            name='diploma_management_profile',
            fields=[
                ('DIPLOMA_MANAGEMENT_PROFILE_ID', models.AutoField(primary_key=True, serialize=False)),
                ('GRADUATION_YEAR', models.CharField(max_length=20)),
                ('MODE_OF_STUDY', models.CharField(max_length=50)),
                ('CLASSIFIED_BY_ACADEMIC_RECORDS', models.CharField(max_length=50)),
                ('CERTIFICATE_NUMBER', models.CharField(max_length=50)),
                ('NUMBER_ENTERED_INTO_THE_DEGREE_TRACKING_BOOK', models.CharField(max_length=50)),
                ('DATE_OF_DECISION_ANNOUNCEMENT', models.DateField()),
                ('COMMENT', models.CharField(max_length=255)),
                ('DATE_UPDATED', models.DateField()),
                ('ACADEMIC_PROGRAM_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.academic_program')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('STUDENT_ID_NUMBER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.student')),
            ],
        ),
        migrations.CreateModel(
            name='student_academic_intake_session_academic_program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ACADEMIC_INTAKE_SESSION_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.academic_intake_session')),
                ('ACADEMIC_PROGRAM_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.academic_program')),
                ('LEARNING_STATUS_TYPE_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.learning_status_type')),
                ('STUDENT_ID_NUMBER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.student')),
            ],
        ),
        migrations.AddConstraint(
            model_name='academic_intake_session_academic_program_curriculum',
            constraint=models.UniqueConstraint(fields=('ACADEMIC_INTAKE_SESSION_ID', 'ACADEMIC_PROGRAM_ID', 'CURRICULUM_ID'), name='PK_intake_session_program_curriculum'),
        ),
        migrations.AddConstraint(
            model_name='student_academic_intake_session_academic_program',
            constraint=models.UniqueConstraint(fields=('STUDENT_ID_NUMBER', 'ACADEMIC_INTAKE_SESSION_ID', 'ACADEMIC_PROGRAM_ID'), name='PK_student_c_intake_session_program'),
        ),
    ]
