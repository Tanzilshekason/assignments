# Generated by Django 3.2.12 on 2022-05-19 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentid', models.IntegerField()),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=70)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
