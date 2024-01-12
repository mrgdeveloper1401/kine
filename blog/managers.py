from django.db.models import Manager


class ActivePost(Manager):
    def active(self):
        return self.filter(is_active=True)