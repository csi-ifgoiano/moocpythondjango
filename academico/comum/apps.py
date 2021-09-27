from django.apps import AppConfig


class ComumConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comum'
    verbose_name = "Comum"
    description = 'Gerencia as configurações e cadastros gerais para uso de todos os módulos.'
    icon = 'list'
    area = 'Comum'
