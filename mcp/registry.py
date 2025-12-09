import uuid
from typing import Any


class ObjectRegistry:
    def __init__(self):
        self._objects: dict[str, Any] = {}

    def register(self, object: Any) -> str:
        id = str(uuid.uuid4())
        self._objects[id] = object
        return id

    def register_by_name(self, name: str, object: Any) -> str:
        self._objects[name] = object
        return name

    def unregister(self, id: str):
        del self._objects[id]

    def get(self, id: str) -> Any | None:
        return self._objects.get(id)

    def list(self) -> list[str]:
        return list(self._objects.keys())

    def clear(self):
        self._objects.clear()


object_registry = ObjectRegistry()
