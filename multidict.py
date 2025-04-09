class MultiDict(dict):
    """
    A dictionary subclass that allows multiple values for a single key.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the MultiDict instance.

        Args:
            *args: Positional arguments to initialize the dictionary.
            **kwargs: Keyword arguments to initialize the dictionary.
        """
        super().__init__(*args, **kwargs)
        
        for key, value in self.items():
            if not isinstance(value, list):
                raise TypeError(f"Value for key '{key}' must be a list.")

    def __setitem__(self, key, value):
        """
        Add a value to the list of values for the given key. If the key does not exist, 
        create a new list with the value.

        Args:
            key: The key to add the value to.
            value: The value to add.
        """
        try:
            _ = super().__getitem__(key)
        except KeyError:
            super().__setitem__(key, [value])
        else:
            super().__getitem__(key).append(value)

    def __delitem__(self, key):
        """
        Delete the key and all its associated values from the dictionary.

        Args:
            key: The key to delete.
        """
        _ = super().pop(key)

    def __repr__(self):
        """
        Return a string representation of the MultiDict.

        Returns:
            str: The string representation of the MultiDict.
        """
        return f"{self.__class__.__name__}({super().__repr__()})"