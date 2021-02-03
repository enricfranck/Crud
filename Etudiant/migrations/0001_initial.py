# Generated by Django 3.1.5 on 2021-02-03 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
                ('nom', models.CharField(max_length=40)),
                ('prenom', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('adresse', models.CharField(max_length=40)),
            ],
        ),
    ]