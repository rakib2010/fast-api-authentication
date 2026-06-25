import datetime
from typing import Any

BD_TZ = datetime.timezone(datetime.timedelta(hours=6))

def success_response(data: Any = None, status: str = "successful",
                     created_at=None, updated_at=None):
    now = datetime.datetime.now(tz=BD_TZ).isoformat()
    return {
        "status": status,
        "data": data,
        "created_at": created_at.isoformat() if created_at else now,
        "updated_at": updated_at.isoformat() if updated_at else now,
    }

def error_response(message: str, status: str = "error"):
    now = datetime.datetime.now(tz=BD_TZ).isoformat()
    return {
        "status": status,
        "data": message,
        "created_at": now,
        "updated_at": now,
    }