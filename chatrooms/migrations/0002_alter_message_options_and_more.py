# Generated by Django 5.2.3 on 2025-06-20 20:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatrooms', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-sent_at']},
        ),
        migrations.RemoveField(
            model_name='chatroom',
            name='chatroom_clients',
        ),
        migrations.RemoveField(
            model_name='chatroom',
            name='messages',
        ),
        migrations.AddField(
            model_name='chatroom',
            name='chat_type',
            field=models.CharField(choices=[('DM', 'Direct Message'), ('GROUP', 'Group Chat')], default='GROUP', max_length=10),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='members',
            field=models.ManyToManyField(related_name='chatrooms', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='chatroom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chatrooms.chatroom'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_authored', to=settings.AUTH_USER_MODEL),
        ),
    ]
