# Generated by Django 3.1 on 2020-10-27 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_hospital_request'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_attributes',
            old_name='alcoholic',
            new_name='obesity',
        ),
        migrations.RenameField(
            model_name='user_attributes',
            old_name='autoimmune',
            new_name='others',
        ),
        migrations.RemoveField(
            model_name='user_attributes',
            name='bmi',
        ),
        migrations.RemoveField(
            model_name='user_attributes',
            name='cancer',
        ),
        migrations.RemoveField(
            model_name='user_attributes',
            name='cough',
        ),
        migrations.RemoveField(
            model_name='user_attributes',
            name='fever',
        ),
        migrations.RemoveField(
            model_name='user_attributes',
            name='liver',
        ),
        migrations.RemoveField(
            model_name='user_attributes',
            name='spo2',
        ),
    ]