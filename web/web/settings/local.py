#! -*- coding:utf8 -*-

import settings.base

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'anysell.db')
    }
}
