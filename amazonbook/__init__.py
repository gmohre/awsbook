import boto
from boto.emr.connection import EmrConnection
EMR_USER='AKIAJCFQSDVJY4TG4GPA'
EMR_KEY='ngwnuMqdEh9xTPWFsK2/AmdeBNse8VwqlBFB9sbe'
class AmazonBook():
    def __init__(self, user=EMR_USER, key=EMR_KEY):
        self.conn = EmrConnection(user,key)

    @property
    def connection(self):
        return self.conn
