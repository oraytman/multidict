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
        self._count = 0

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
        self._count += 1

    def __delitem__(self, key):
        """
        Delete the key and all its associated values from the dictionary.

        Args:
            key: The key to delete.
        """
        self._count -= len(self[key])
        _ = super().pop(key)

    def __len__(self):
        """
        Return the total number of values in the dictionary.

        Returns:
            int: The total count of values.
        """
        return self._count

    def __repr__(self):
        """
        Return a string representation of the MultiDict.

        Returns:
            str: The string representation of the MultiDict.
        """
        return f"{self.__class__.__name__}({super().__repr__()})"