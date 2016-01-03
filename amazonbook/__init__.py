import boto
from boto.emr.connection import EmrConnection
class AmazonBook():
    def __init__(self, user=EMR_USER, key=EMR_KEY):
        self.conn = EmrConnection(user,key)

    @property
    def connection(self):
        return self.conn
