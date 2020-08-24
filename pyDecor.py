import inspect

def strict(function):
    """ 
    Check the type for each parameter. This decorator will raise an exception if 
    the type does not match what was expected.

    This decorator will definitely slow down the execution of the method so 
    use it during debugging and remove it once you're ready to deploy/publish.
    """
    def wrapper(*args, **kwargs):
        functionDetails = inspect.getfullargspec(function)
        
        """
        TODO Need to update this decorator so that specifying params aren't necessary.
        """

        # Make sure that the parameter's are specified
        if len(args) > 1:
            raise Exception("When using the decorator '@strict', you must specify the parameter and argument when you call the function. Example: myFunction(x=5)")
        

        # Check the type for the functions parameters
        for parameter in functionDetails.args:
            try:
                functionType = function.__annotations__[parameter]
                functionValue = kwargs[parameter]
                if not isinstance(functionValue,functionType):
                    raise TypeError(f"The parameter '{parameter}' has to be of type {functionType}, the value given was of type {type(functionValue)}")
            except KeyError:
                pass

        # If the type check succeeds, execute the function and check return value if it exists
        returnVal = function(*args, **kwargs)

        if returnVal and "return" in function.__annotations__:
            functionType = function.__annotations__["return"]
            if not isinstance(returnVal,functionType):
                raise TypeError(f"The return value has to be of type {functionType}, the value returned was of type {type(returnVal)}")

        return returnVal

    return wrapper