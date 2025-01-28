from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/user/')
async def get_user(db: Session = Depends(get_db)):
    try:
        return await service.get_user(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user/id')
async def get_user_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_user_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/user/')
async def post_user(raw_data: schemas.PostUser, db: Session = Depends(get_db)):
    try:
        return await service.post_user(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/user/id/')
async def put_user_id(raw_data: schemas.PutUserId, db: Session = Depends(get_db)):
    try:
        return await service.put_user_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/user/id')
async def delete_user_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_user_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

