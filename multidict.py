class MultiDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._count = 0

    def __setitem__(self, key, value):        
        try:
            _ = super().__getitem__(key)            
        except KeyError:
            super().__setitem__(key, [value])
            self._count += 1
        else:
            super().__getitem__(key).append(value)
            self._count += 1
   
    def __delitem__(self, key):
        self._count -= len(self[key])
        _ = super().pop(key)

    def __len__(self):
        return self._count
     
    def __repr__(self):
        return f"{self.__class__.__name__}({super().__repr__()})"