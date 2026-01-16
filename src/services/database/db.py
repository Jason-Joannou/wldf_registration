from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, Type, TypeVar


class BaseDB(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    async def connect(self):
        raise NotImplementedError("Connect method not implemented")

    @abstractmethod
    async def __enter__(self):
        raise NotImplementedError("Enter method not implemented")

    @abstractmethod
    async def __exit__(self):
        raise NotImplementedError("Exit Method not implemented")
