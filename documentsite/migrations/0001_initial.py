# Generated by Django 3.1.7 on 2021-03-11 15:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.datetime_safe


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=800)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('createDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('editDate', models.DateTimeField(auto_now=True, null=True)),
                ('link', models.FileField(upload_to='resources')),
                ('image', models.ImageField(upload_to='images')),
                ('type', models.CharField(choices=[('Vd', 'Video'), ('Ebook', 'Ebook'), ('Audio', 'Audio')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=800)),
                ('image', models.ImageField(upload_to='images')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TopicDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idDocument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentsite.document')),
                ('idTopic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentsite.topic')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=300)),
                ('phonenumber', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=300, unique=True)),
                ('address', models.CharField(max_length=300)),
                ('dob', models.DateField(blank=True, null=True)),
                ('rate', models.IntegerField(default=0)),
                ('fullname', models.CharField(max_length=300)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(blank=True, default=django.utils.datetime_safe.datetime.now)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]