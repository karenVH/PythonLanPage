# Generated by Django 2.2 on 2020-05-20 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuarioid', models.CharField(max_length=20, verbose_name='Identificación')),
                ('nombuser', models.CharField(max_length=256, verbose_name='Nombres')),
                ('apeluser', models.CharField(max_length=256, verbose_name='Apellidos')),
                ('emailuser', models.CharField(max_length=256, verbose_name='Correo Electrónico')),
                ('fotouser', models.ImageField(upload_to='img/perfiles', verbose_name='Imagen de Usuario')),
                ('teleuser', models.CharField(max_length=25, verbose_name=' Teléfono de contácto')),
                ('estauser', models.CharField(default='Activo', max_length=20, verbose_name='Estado')),
                ('creadoel', models.DateTimeField(auto_now_add=True, verbose_name='Registrado el:')),
                ('modificado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Datos personales',
                'verbose_name_plural': 'Datos de Usuario',
            },
        ),
        migrations.CreateModel(
            name='HabilUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombhabil', models.CharField(max_length=45, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades',
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roleName', models.CharField(max_length=50, verbose_name='Nombre de Rol')),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
            },
        ),
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Calificación')),
                ('idhabil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdata.HabilUser', verbose_name='Habilidad')),
                ('iduser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdata.DatosUser', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Rate',
                'verbose_name_plural': 'Nivel de Habilidad',
            },
        ),
        migrations.CreateModel(
            name='DetaRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estarol', models.CharField(default='Activo', max_length=50, verbose_name='Status')),
                ('agregado', models.DateTimeField(auto_now_add=True)),
                ('idrol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdata.Roles', verbose_name='Rol')),
                ('iduser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdata.DatosUser', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Detalle de perfil',
                'verbose_name_plural': 'Perfiles de Usuario',
            },
        ),
    ]
