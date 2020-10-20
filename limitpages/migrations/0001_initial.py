# Generated by Django 3.0.10 on 2020-10-20 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0028_auto_20201018_0834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='limitpages_document_related', related_query_name='limitpages_documents', to='core.Document')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
