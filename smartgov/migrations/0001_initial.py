# Generated by Django 2.2.16 on 2020-10-19 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=50, unique=True)),
                ('parameter', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Metode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=50, unique=True)),
                ('nama', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=50, unique=True)),
                ('parameter', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=50, unique=True)),
                ('parameter', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_data', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('output_data', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('outcome_data', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('input_ref', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='smartgov.Input')),
                ('metode', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='smartgov.Metode')),
                ('outcome_ref', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='smartgov.Outcome')),
                ('output_ref', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='smartgov.Output')),
            ],
        ),
    ]
