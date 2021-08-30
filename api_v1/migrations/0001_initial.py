# Generated by Django 2.2.10 on 2021-08-30 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('date_start', models.DateField(auto_now_add=True, verbose_name='data start')),
                ('date_end', models.DateField(verbose_name='date_end')),
                ('description', models.TextField(verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='text_questions')),
                ('type_of_question', models.CharField(choices=[('text', 'Ответ текстом'), ('one_option', 'Один вариант'), ('multiple_choice', 'Выбор нескольких вариантов')], max_length=30, verbose_name='type of question')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v1.Survey', verbose_name='survey')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Вариант ответа')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='api_v1.Questions')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('self_text', models.TextField(null=True)),
                ('many_choice', models.ManyToManyField(null=True, to='api_v1.Choice')),
                ('one_choice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers_one_choice', to='api_v1.Choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='api_v1.Questions')),
            ],
        ),
    ]