from sqlalchemy import Column, Integer, String, Text, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    resolution = Column(String, default="1920x1080")
    model_name = Column(String, default="Runway Gen-3")
    created_at = Column(DateTime, default=datetime.utcnow)

    # 关联：一个项目有多个分镜
    shots = relationship("Shot", back_populates="project", cascade="all, delete-orphan")

class Shot(Base):
    __tablename__ = "shots"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    
    # 排序或时间线位置
    order_index = Column(Integer, default=0) 
    duration = Column(Float, default=5.0) # 秒
    
    prompt = Column(Text, nullable=True)
    
    # 关联
    project = relationship("Project", back_populates="shots")
    generated_videos = relationship("GeneratedVideo", back_populates="shot")

class GeneratedVideo(Base):
    __tablename__ = "generated_videos"

    id = Column(Integer, primary_key=True, index=True)
    shot_id = Column(Integer, ForeignKey("shots.id"))
    
    video_url = Column(String) # 本地路径或S3 URL
    status = Column(String, default="pending") # pending, processing, completed, failed
    is_selected = Column(Integer, default=0) # 0: 备用, 1: 选中
    
    shot = relationship("Shot", back_populates="generated_videos")