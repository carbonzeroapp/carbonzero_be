from django.core.validators import RegexValidator

username_validator = RegexValidator(regex=r'^\S*$', message='Username should not included with space',
                                    code='invalid_username')
