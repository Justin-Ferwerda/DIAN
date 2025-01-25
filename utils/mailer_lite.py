import mailerlite as MailerLite
from .get_env import get_env

class MailerLiteService:
    """Class to Interact with the Mailerlite sdk
    """

    def __init__(self):
        self.env = get_env(__file__)
        self.client = MailerLite.Client({
          'api_key': self.env("MAILER_LITE_AUTH_TOKEN")
        })

    def create_subscriber(self, email, name):
        """creates a subscriber and adds them to the group for daily devotions
        Args:
            email (string):
            name (string):
        Returns:
            dict: the subscriber object from mailerlite
        """
        
        fields={
          'name': name
        }
        group_ids = [int(self.env("MAILER_LITE_GROUP_ID"))]
        subscriber = self.client.subscribers.create(email, fields=fields, groups=group_ids)
        return subscriber
