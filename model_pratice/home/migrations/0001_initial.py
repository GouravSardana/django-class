# Generated by Django 2.1.2 on 2019-02-09 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medical_library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('causes', models.TextField(blank=True, max_length=10000, null=True)),
                ('symptoms', models.TextField(blank=True, max_length=10000, null=True)),
                ('diagnosis', models.TextField(blank=True, max_length=10000, null=True)),
                ('treatment', models.TextField(blank=True, max_length=10000, null=True)),
            ],
        ),
    ]