from pathlib import Path
from viber.utils import load_app_configuration


class Common:
    def __init__(self):
        self.app_config = load_app_configuration()
        self.db = Path("viber/working_dir/db.json")
        self.viber_auth_token = self.app_config.get("viber", "auth_token")
        self.viber_web_hook_url = self.app_config.get("viber", "webhook_uri")
        self.viber_name = self.app_config.get("viber", "name")
        self.viber_avatar = self.app_config.get("viber", "avatar")
        self.unsplash_key = self.app_config.get("unsplash", "client_secret")
        self.pixbay_key = self.app_config.get("pixbay", "key")


ViberCommon = Common()
