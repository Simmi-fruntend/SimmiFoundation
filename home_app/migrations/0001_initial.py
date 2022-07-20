# Generated by Django 4.0.5 on 2022-07-11 07:52

from django.db import migrations, models
import home_app.models.current_incoming_event
import home_app.models.our_partners
import home_app.models.our_success_story
import home_app.models.our_volunteers
import home_app.models.trending_fundraiser
import home_app.models.what_people_say


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carousel_img', models.ImageField(upload_to='carousel_image')),
            ],
        ),
        migrations.CreateModel(
            name='Current_incoming_event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_img', models.ImageField(upload_to=home_app.models.current_incoming_event.Current_incoming_event.nameFile)),
                ('event_name', models.CharField(max_length=50)),
                ('about_event', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Our_partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_logo', models.ImageField(upload_to=home_app.models.our_partners.Our_partners.nameFile)),
                ('partner_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Our_success_story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('success_img', models.ImageField(upload_to=home_app.models.our_success_story.Our_success_story.nameFile)),
                ('success_heading', models.CharField(max_length=100)),
                ('about_success', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Our_volunteers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volunteer_img', models.ImageField(upload_to=home_app.models.our_volunteers.Our_volunteers.nameFile)),
                ('volunteer_name', models.CharField(max_length=100)),
                ('about_volunteer', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Trending_fundraisers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fundraiser_image', models.ImageField(upload_to=home_app.models.trending_fundraiser.Trending_fundraisers.nameFile)),
                ('fundraiser_name', models.CharField(max_length=50)),
                ('fundraise_by_name', models.CharField(max_length=50)),
                ('fundraise_by_image', models.ImageField(upload_to=home_app.models.trending_fundraiser.Trending_fundraisers.nameFile)),
                ('fund_amout_raise', models.IntegerField()),
                ('fund_amount_target', models.IntegerField()),
                ('fund_start_date', models.DateField(null=True)),
                ('fund_end_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='What_people_say',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=50)),
                ('person_image', models.ImageField(upload_to=home_app.models.what_people_say.What_people_say.nameFile)),
                ('person_review', models.TextField(max_length=500)),
            ],
        ),
    ]
