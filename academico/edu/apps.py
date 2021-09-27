from django.apps import AppConfig


class EduConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'edu'
    verbose_name = 'Ensino'
    area = 'Ensino'
    description = 'Realiza o controle acadêmico.'
    icon = 'chalkboard-teacher'
