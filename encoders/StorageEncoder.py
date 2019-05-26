from pojo.Storage import Storage as pojo_class
import json


class ProcessorsEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, pojo_class):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)