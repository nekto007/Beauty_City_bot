import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beautycity.settings')
django.setup()

from beautycitybot.dispatcher import run_pooling

if __name__ == "__main__":
    run_pooling()