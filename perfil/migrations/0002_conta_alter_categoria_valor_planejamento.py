# Generated by Django 4.2.3 on 2023-07-05 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apelido', models.CharField(max_length=25)),
                ('banco', models.CharField(choices=[('NU', 'Nubank'), ('CE', 'Caixa Econômica'), ('IT', 'Itaú'), ('BB', 'Banco do Brasil')], max_length=2)),
                ('tipo', models.CharField(choices=[('PF', 'Pessoa Física'), ('PJ', 'Pessoa Jurídica')], max_length=2)),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('icone', models.ImageField(upload_to='icones')),
            ],
        ),
        migrations.AlterField(
            model_name='categoria',
            name='valor_planejamento',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]