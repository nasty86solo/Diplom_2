import uuid
from typing import Dict
from faker import Faker

_fake = Faker()

def unique_email() -> str:
    return f"user_{uuid.uuid4().hex[:8]}@example.com"

def user_payload() -> Dict[str, str]:
    return {
        "email": unique_email(),
        "password": _fake.password(length=10, special_chars=False),
        "name": _fake.first_name(),
    }
