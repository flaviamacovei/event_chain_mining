class Event:
    def init(self, action: str, **kwargs):
        assert action
        assert kwargs
        self.action = action
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_action(self):
        return self.action