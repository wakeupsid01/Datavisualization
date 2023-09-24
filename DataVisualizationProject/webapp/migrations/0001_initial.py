# Generated by Django 4.1.7 on 2023-03-30 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('emailid', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'NewUser',
            },
        ),
    ]