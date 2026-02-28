from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.middleware.cors import CORSMiddleware

from . import models, schemas, database

# 自动创建数据库表 (如果在本地运行，会自动生成 director.db)
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="AI Director API")

# 允许跨域 (CORS)，这样你的 Vue 前端 (localhost:5173) 才能访问 FastAPI (localhost:8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # 生产环境要改为具体的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 项目 API ---

@app.post("/projects/", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(database.get_db)):
    db_project = models.Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@app.get("/projects/", response_model=List[schemas.Project])
def read_projects(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    projects = db.query(models.Project).offset(skip).limit(limit).all()
    return projects

@app.get("/projects/{project_id}", response_model=schemas.Project)
def read_project(project_id: int, db: Session = Depends(database.get_db)):
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

# --- 分镜 API ---

@app.post("/projects/{project_id}/shots/", response_model=schemas.Shot)
def create_shot_for_project(
    project_id: int, shot: schemas.ShotCreate, db: Session = Depends(database.get_db)
):
    # 检查项目是否存在
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
        
    db_shot = models.Shot(**shot.dict(), project_id=project_id)
    db.add(db_shot)
    db.commit()
    db.refresh(db_shot)
    return db_shot

@app.get("/projects/{project_id}/shots/", response_model=List[schemas.Shot])
def read_shots(project_id: int, db: Session = Depends(database.get_db)):
    shots = db.query(models.Shot).filter(models.Shot.project_id == project_id).order_by(models.Shot.order_index).all()
    return shots