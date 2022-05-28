from typing import Any, Callable, Optional

LAZY_GETTER_CACHE: dict[Callable, Any] = {}


def lazy_getter(func: Callable, *args: Any, **kwargs: Any) -> Callable:
    def wrapper() -> Any:
        if args or kwargs:
            raise ValueError("Lazy getter must not have arguments")

        if func not in LAZY_GETTER_CACHE:
            value: Callable = func()
            LAZY_GETTER_CACHE[func] = value

        return LAZY_GETTER_CACHE[func]

    return wrapper
