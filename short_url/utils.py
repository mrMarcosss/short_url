import random
import string

from django.conf import settings

SHORT_LEN_MIN = getattr(settings, 'SHORT_LEN_MIN', 6)


def generate_code(size=SHORT_LEN_MIN, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_short_url(instance, size=SHORT_LEN_MIN):
    new_code = generate_code(size=size)
    cls = instance.__class__
    qs = cls.objects.filter(short=new_code)
    if qs:
        return generate_short_url(size=size)
    return new_code
