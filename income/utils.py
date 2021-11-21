from django.utils.text import slugify
import random
import string

# Random string generator
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# Unique Slug Generator 
def unique_slug_generator(instance, new_slug=None):
    """
    It assumes your instance has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug  
    elif instance.description is not None:
        slug = slugify(instance.description[0:30])  
    else:
        slug = slugify(instance.name)  

    Klass = instance.__class__

    qs_exists = Klass.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(slug=slug, randstr=random_string_generator(size=4))
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

