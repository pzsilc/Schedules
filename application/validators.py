import os
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.xlsx',]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Niewłaściwy typ pliku. Wymagany .xlsx (standardowy plik Excela)')