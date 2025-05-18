from typing import Optional

def find_user(id: int) -> Optional[str]:
    if id == 1:
        return "Admin"
    return None
