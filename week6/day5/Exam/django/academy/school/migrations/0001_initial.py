# Generated by Django 4.2.4 on 2023-08-20 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200)),
                ('course_code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolFacility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility_name', models.CharField(max_length=200)),
                ('usage_purpose', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('schoolfacility_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='school.schoolfacility')),
                ('equipment_list', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Laboratories',
            },
            bases=('school.schoolfacility',),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('courses', models.ManyToManyField(related_name='teachers', to='school.course')),
            ],
        ),
    ]
