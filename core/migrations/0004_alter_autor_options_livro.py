# Generated by Django 4.0.6 on 2022-07-07 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_autor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name_plural': 'Autores'},
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=32)),
                ('quantidade', models.IntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7)),
                ('Editora', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='livros', to='core.editora')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='livros', to='core.categoria')),
            ],
        ),
    ]
