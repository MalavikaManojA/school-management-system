# Generated by Django 4.1.3 on 2023-03-02 04:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.CharField(default='', max_length=20, verbose_name='Subject')),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin.standard')),
            ],
        ),
        migrations.CreateModel(
            name='StaffDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_taught', models.CharField(max_length=20)),
                ('qualification', models.TextField(blank=True, null=True)),
                ('class_taught', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin.standard', unique=True)),
                ('staff_name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
