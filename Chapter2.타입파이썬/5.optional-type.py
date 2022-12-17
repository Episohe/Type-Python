from typing import Union, Optional


def foo(name: str) -> Optional[str]:
    if name == "Sunny":
        return None
    else:
        return name


xxx: Optional[str] = foo("Sunny")
