import mailerlite as MailerLite
from .get_env import get_env

class MailerLiteService:

    def __init__(self):
        self.env = get_env(__file__)
        self.client = MailerLite.Client({
          'api_key': self.env("MAILER_LITE_AUTH_TOKEN")
        })

    def create_subscriber(self, email, name):
        fields={
          'name': name
        }
        subscriber = self.client.subscribers.create(email, fields=fields)
        return subscriber

    def add_subscriber_to_group(self, subscriber):
        group_id = int(self.env("MAILER_LITE_GROUP_ID"))
        subscriber_id  = int(subscriber["data"]["id"])
        self.client.subscribers.assign_subscriber_to_group(subscriber_id=subscriber_id, group_id=group_id)
