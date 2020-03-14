from viber.utils import load_app_configuration


class Common:
    def __init__(self):
        self.app_config = load_app_configuration()
        self.viber_auth_token = self.app_config.get("viber", "auth_token")
        self.viber_web_hook_url = self.app_config.get("viber", "webhook_uri")
        self.viber_name = self.app_config.get("viber", "name")
        self.viber_avatar = self.app_config.get("viber", "avatar")


ViberCommon = Common()
