# Generated by Django 4.1 on 2022-08-14 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('telefone', models.CharField(blank=True, max_length=50, null=True)),
                ('msg', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('nascimento', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
