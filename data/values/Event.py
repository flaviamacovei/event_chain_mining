class Event:
    def __init__(self, action: str, **kwargs):
        assert action
        assert kwargs
        self.action = action
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f"{self.action}({', '.join([f'{key}={value}' for key, value in self.__dict__.items() if key != 'action'])})"

    def __repr__(self):
        return self.action