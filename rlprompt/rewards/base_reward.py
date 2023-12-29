class BaseReward: 

    # It allows instances of that class to be called as if they were functions.
    def __call__(self, *args, **kwargs): 
        return self.forward(*args, **kwargs)

    def forward(self, *args, **kwargs): 
        raise NotImplementedError  # This method needs to be defined in a subclass.
    