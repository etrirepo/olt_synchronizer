# Copyright 2017-present Open Networking Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-27 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volt', '0011_auto_20190626_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voltservice_decl',
            name='voltha_pass',
        ),
        migrations.RemoveField(
            model_name='voltservice_decl',
            name='voltha_user',
        ),
        migrations.AlterField(
            model_name='voltservice_decl',
            name='voltha_port',
            field=models.IntegerField(default=55555, help_text=b'The Voltha API port. By default 55555'),
        ),
        migrations.AlterField(
            model_name='voltservice_decl',
            name='voltha_url',
            field=models.CharField(default=b'voltha-api.voltha.svc.cluster.local', help_text=b'The Voltha API address. By default voltha-api.default.svc.cluster.local', max_length=256),
        ),
    ]
