from django.core.files.storage import FileSystemStorage
import time, datetime, random


class FileNameSystem(FileSystemStorage):
    def get_available_name(self, name, **kwargs):
        now = time.time()
        stamp = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d-%H-%M-%S') + str(random.random()) + '.xlsx'
        return '{0}_{1}'.format(name, str(stamp))