def validate_bid(value, old_value):
    if value > old_value:
        return value
    else:
        return False
