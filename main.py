from pyDecor import *

class Test:

    def __init__(self):
        print("init")
    
    @strict
    def run(self, name: str, speed: int, isRunning: bool = False) -> bool:
        if isRunning:
            print(f"{name} is running at {speed} mph")
            return True
        
        print(f"{name} is not running")
        return False


# The parameter and arguments must be specified
# run(name="Josh",speed=10,isRunning=True)

T = Test()
T.run(name="Josh",speed=10,isRunning=True)