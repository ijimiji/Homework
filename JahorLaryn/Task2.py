class HistoryDict:
    def __init__(self, d):
        self.changed_keys = []
        self.d = d

    def set_value(self, key, value):
        if key in self.changed_keys:
            self.changed_keys.remove(key)
        self.changed_keys.append(key)
        self.d[key] = value

    def get_history(self):
        return self.changed_keys
