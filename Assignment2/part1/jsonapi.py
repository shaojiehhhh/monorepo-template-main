import json

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        # Handle custom objects that need special encoding
        if isinstance(obj, complex):
            return {'__complex__': True, 'real': obj.real, 'imag': obj.imag}
        if isinstance(obj, range):
            return {'__range__': True, 'start': obj.start, 'stop': obj.stop, 'step': obj.step}
        return super().default(obj)

class CustomJSONDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.custom_object_hook, *args, **kwargs)

    def custom_object_hook(self, dct):
        if '__complex__' in dct:
            return complex(dct['real'], dct['imag'])
        if '__range__' in dct:
            return range(dct['start'], dct['stop'], dct['step'])
        return dct

def dumps(obj, **kwargs):
    return json.dumps(obj, cls=CustomJSONEncoder, **kwargs)

def loads(s, **kwargs):
    return json.loads(s, cls=CustomJSONDecoder, **kwargs)
