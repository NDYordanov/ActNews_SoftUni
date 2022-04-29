from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            # Invalid case
            raise ValidationError('Value must contain only letters')


def validate_only_percentage(value):
    if value > 100 or value < 0:
        raise ValidationError('Value must be percentage. Please enter a number between 0 and 100!')
