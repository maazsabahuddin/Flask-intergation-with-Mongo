def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__
