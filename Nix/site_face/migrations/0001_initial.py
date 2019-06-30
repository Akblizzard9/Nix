# Generated by Django 2.1.7 on 2019-06-10 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snowfall', models.IntegerField()),
                ('bottom_mintemp', models.IntegerField()),
                ('bottom_maxtemp', models.IntegerField()),
                ('mid_mintemp', models.IntegerField()),
                ('mid_maxtemp', models.IntegerField()),
                ('top_mintemp', models.IntegerField()),
                ('top_maxtemp', models.IntegerField()),
                ('todays_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resorts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resort_name', models.CharField(max_length=200, unique=True)),
                ('location', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='reports',
            name='resort_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_face.Resorts', to_field='resort_name', unique=True),
        ),
    ]
