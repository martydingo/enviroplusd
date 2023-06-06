from .sensors import sensors
from .mqtt import mqtt

__all__ = ['sensors', 'mqtt']


def testModule() -> None:
    print("mainModuleTest")

