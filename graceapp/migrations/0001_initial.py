# Generated by Django 4.1.4 on 2022-12-19 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identite', models.CharField(max_length=20)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre_livre', models.CharField(max_length=50)),
                ('numeroserie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graceapp.client')),
            ],
        ),
    ]
