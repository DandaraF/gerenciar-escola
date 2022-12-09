def general_roundtrip(obj):
    json = obj.to_json()
    return obj.from_json(json)
