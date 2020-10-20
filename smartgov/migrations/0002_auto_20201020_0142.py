# Generated by Django 2.2.16 on 2020-10-20 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smartgov', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='input',
            options={'ordering': ['kode'], 'verbose_name': 'Input', 'verbose_name_plural': 'Input'},
        ),
        migrations.AlterModelOptions(
            name='metode',
            options={'ordering': ['kode'], 'verbose_name': 'Metode', 'verbose_name_plural': 'Metode'},
        ),
        migrations.AlterModelOptions(
            name='outcome',
            options={'ordering': ['kode'], 'verbose_name': 'Outcome', 'verbose_name_plural': 'Outcome'},
        ),
        migrations.AlterModelOptions(
            name='output',
            options={'ordering': ['kode'], 'verbose_name': 'Output', 'verbose_name_plural': 'Output'},
        ),
        migrations.CreateModel(
            name='OutputData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartgov.Output')),
            ],
        ),
        migrations.CreateModel(
            name='OutcomeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartgov.Outcome')),
            ],
        ),
        migrations.CreateModel(
            name='InputData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartgov.Input')),
            ],
        ),
        migrations.CreateModel(
            name='EntryDataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inputs', models.ManyToManyField(to='smartgov.InputData')),
                ('metode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartgov.Metode')),
                ('outcomes', models.ManyToManyField(to='smartgov.OutcomeData')),
                ('outputs', models.ManyToManyField(to='smartgov.OutputData')),
            ],
        ),
    ]