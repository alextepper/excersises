from django.apps import AppConfig

class ProfileAppConfig(AppConfig):
    name = 'profileApp'

    def ready(self):
        import profiles.signals
