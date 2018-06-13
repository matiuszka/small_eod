# Generated by Django 2.0.5 on 2018-06-13 08:42

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0003_auto_20180608_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('type', models.IntegerField(choices=[(1, 'Whose case'), (2, 'What scope'), (3, 'Inaction scope'), (4, 'Decision scope'), (5, 'The moment of providing information'), (6, 'Proceedings interrupted'), (7, 'Status')])),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Dictionary',
                'verbose_name_plural': 'Dictinaries',
            },
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='case',
            name='decision_scope',
            field=models.ManyToManyField(blank=True, limit_choices_to={'type': 4}, related_name='case_decision_scope', to='cases.Dictionary', verbose_name='Decision scope'),
        ),
        migrations.AddField(
            model_name='case',
            name='inaction_scope',
            field=models.ManyToManyField(blank=True, limit_choices_to={'type': 3}, related_name='case_inaction_scope', to='cases.Dictionary', verbose_name='Inaction scope'),
        ),
        migrations.AddField(
            model_name='case',
            name='proceddings_interrupted',
            field=models.ManyToManyField(blank=True, limit_choices_to={'type': 6}, related_name='case_proceedings_interrupted', to='cases.Dictionary', verbose_name='Proceedings interrupted'),
        ),
        migrations.AddField(
            model_name='case',
            name='status',
            field=models.ManyToManyField(blank=True, limit_choices_to={'type': 7}, related_name='case_status', to='cases.Dictionary', verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='case',
            name='time_of_info_provide',
            field=models.ManyToManyField(blank=True, limit_choices_to={'type': 5}, related_name='case_time_of_info_provide', to='cases.Dictionary', verbose_name='The moment of providing information'),
        ),
        migrations.AddField(
            model_name='case',
            name='what_scope',
            field=models.ManyToManyField(blank=True, limit_choices_to={'type': 2}, related_name='case_what_scope', to='cases.Dictionary', verbose_name='What scope'),
        ),
        migrations.AddField(
            model_name='case',
            name='whose_case',
            field=models.ManyToManyField(blank=True, limit_choices_to={'type': 1}, related_name='case_whose_case', to='cases.Dictionary', verbose_name='Whose case'),
        ),
    ]
