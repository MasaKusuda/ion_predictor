# Generated by Django 3.2.12 on 2022-04-05 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chemical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('obtained_date', models.DateField(blank=True, null=True)),
                ('SMILES', models.TextField(blank=True, max_length=4000, null=True)),
                ('mol_ratio', models.CharField(blank=True, max_length=400, null=True)),
                ('wt_ratio', models.CharField(blank=True, max_length=400, null=True)),
                ('Mw', models.FloatField(blank=True, max_length=400, null=True)),
                ('Mn', models.FloatField(blank=True, max_length=400, null=True)),
                ('MwMn', models.FloatField(blank=True, max_length=400, null=True)),
                ('Polymn_deg', models.FloatField(blank=True, max_length=400, null=True)),
                ('Structure', models.CharField(blank=True, max_length=400, null=True)),
                ('melting_temp', models.CharField(blank=True, max_length=400, null=True)),
                ('Tg', models.CharField(blank=True, max_length=400, null=True)),
                ('reference', models.CharField(blank=True, max_length=400, null=True)),
                ('special_memo', models.TextField(blank=True, max_length=4000, null=True)),
            ],
            options={
                'verbose_name': 'Chemical',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Composite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('obtained_date', models.DateField(blank=True, null=True)),
                ('temperature', models.FloatField(max_length=400)),
                ('conductivity', models.FloatField(max_length=400)),
                ('mol_ratio', models.CharField(blank=True, max_length=400, null=True)),
                ('wt_ratio', models.CharField(blank=True, max_length=400, null=True)),
                ('melting_temp', models.CharField(blank=True, max_length=400, null=True)),
                ('inorg_name', models.CharField(blank=True, max_length=400, null=True)),
                ('inorg_contain_ratio', models.FloatField(blank=True, max_length=400, null=True)),
                ('crystallinity', models.FloatField(blank=True, max_length=400, null=True)),
                ('Tg', models.FloatField(blank=True, max_length=400, null=True)),
                ('mp', models.FloatField(blank=True, max_length=400, null=True)),
                ('reference', models.CharField(blank=True, max_length=400, null=True)),
                ('special_memo', models.TextField(blank=True, max_length=4000, null=True)),
                ('component1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chem_component1', to='ion_manager.chemical')),
                ('component2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chem_component2', to='ion_manager.chemical')),
                ('component3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chem_component3', to='ion_manager.chemical')),
                ('component4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chem_component4', to='ion_manager.chemical')),
                ('component5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chem_component5', to='ion_manager.chemical')),
                ('component6', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chem_component6', to='ion_manager.chemical')),
                ('tags', models.ManyToManyField(blank=True, null=True, to='ion_manager.Tag')),
            ],
            options={
                'verbose_name': 'Composite',
            },
        ),
        migrations.AddField(
            model_name='chemical',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='ion_manager.Tag'),
        ),
    ]
