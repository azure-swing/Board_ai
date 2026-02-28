from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# --- Shot (分镜) 模型 ---
class ShotBase(BaseModel):
    prompt: Optional[str] = None
    duration: float = 5.0
    order_index: int = 0

class ShotCreate(ShotBase):
    pass

class Shot(ShotBase):
    id: int
    project_id: int
    
    class Config:
        from_attributes = True

# --- Project (项目) 模型 ---
class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None
    resolution: str = "1920x1080"
    model_name: str = "Runway Gen-3"

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    created_at: datetime
    shots: List[Shot] = []

    class Config:
        from_attributes = True