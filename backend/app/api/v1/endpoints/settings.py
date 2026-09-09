"""
MedPredict AI — System Settings Endpoints
"""

from typing import Dict, Any, List
from fastapi import APIRouter, Depends, Path as FPath, Body
from sqlalchemy.orm import Session
from sqlalchemy import select

from backend.app.core.database import get_db
from backend.app.core.errors import ResourceNotFoundError
from backend.app.models.user import User
from backend.app.models.setting import SystemSetting
from backend.app.security.deps import require_roles

router = APIRouter()

@router.get("")
def list_system_settings(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["admin"]))
) -> List[Dict[str, Any]]:
    """List all dynamic system settings and configuration parameters."""
    settings = db.execute(select(SystemSetting)).scalars().all()
    return [
        {
            "key": s.key,
            "value": s.value,
            "description": s.description,
            "updated_at": s.updated_at.isoformat() if s.updated_at else None
        }
        for s in settings
    ]

@router.put("/{key}")
def update_system_setting(
    key: str = FPath(..., description="Setting key"),
    value: str = Body(..., embed=True, description="New setting value"),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["admin"]))
) -> Dict[str, Any]:
    """Updates a system setting value."""
    setting = db.execute(select(SystemSetting).where(SystemSetting.key == key)).scalar_one_or_none()
    if not setting:
        raise ResourceNotFoundError("SystemSetting", key)

    setting.value = value
    db.commit()
    db.refresh(setting)

    return {
        "key": setting.key,
        "value": setting.value,
        "description": setting.description,
        "updated_at": setting.updated_at.isoformat() if setting.updated_at else None
    }
