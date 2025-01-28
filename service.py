from sqlalchemy.orm import Session
from typing import List
from fastapi import Request, UploadFile
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_user(db: Session):

    user_all = db.query(models.User).order_by(models.User.id).all()
    res = {
        'user_all': user_all,
    }
    return res

async def get_user_id(db: Session, id: int):

    user_one = db.query(models.User).filter(models.User.id == 'id').first()


    import requests

    headers = {}
    
    payload = {}
    apiResponse = requests.get(
        'https://jsonplaceholder.typicode.com/posts',
        headers=headers,
        json=payload if 'params' == 'raw' else None
    )
    user_get_api = apiResponse.json() if 'dict' == 'raw' else apiResponse.text


    import requests

    headers = {}
    
    payload = {'userId': 'Test', 'id': 'test', 'userId': '1', 'body': 'test'}
    apiResponse = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        headers=headers,
        json=payload if 'raw' == 'raw' else None
    )
    user_post_api = apiResponse.json() if 'dict' == 'raw' else apiResponse.text


    import requests

    headers = {}
    
    payload = {}
    apiResponse = requests.get(
        'https://jsonplaceholder.typicode.com/posts',
        headers=headers,
        json=payload if 'params' == 'raw' else None
    )
    user_get_api1 = apiResponse.json() if 'dict' == 'raw' else apiResponse.text
    res = {
        'user_one': user_one,
    }
    return res

async def post_user(db: Session, raw_data: schemas.PostUser):
    id:int = raw_data.id
    first_name:str = raw_data.first_name
    last_name:str = raw_data.last_name



    import requests

    headers = {'user_id': '1'}
    
    payload = {'mobile': '9140734577'}
    apiResponse = requests.post(
        'https://dev-api.ruloans.com/b2c/v1/user/send-otp/v2',
        headers=headers,
        json=payload if 'raw' == 'raw' else None
    )
    post_api = apiResponse.json() if 'dict' == 'raw' else apiResponse.text


    import requests

    headers = {}
    
    payload = {}
    apiResponse = requests.get(
        'https://api-qa.rupeek.co/rpkweb/api/public/getcities',
        headers=headers,
        json=payload if 'params' == 'raw' else None
    )
    post_api1 = apiResponse.json() if 'dict' == 'raw' else apiResponse.text


    import requests

    headers = {}
    
    payload = {'userId': '1', 'id': '1', 'title': 'test', 'body': 'This is a test post'}
    apiResponse = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        headers=headers,
        json=payload if 'raw' == 'raw' else None
    )
    post_api4 = apiResponse.json() if 'dict' == 'raw' else apiResponse.text


    import requests

    headers = {}
    
    payload = {}
    apiResponse = requests.get(
        'https://dummyjson.com/products',
        headers=headers,
        json=payload if 'params' == 'raw' else None
    )
    post_api_test = apiResponse.json() if 'dict' == 'raw' else apiResponse.text


    import requests

    headers = {}
    
    payload = {}
    apiResponse = requests.get(
        'https://dummyjson.com/carts',
        headers=headers,
        json=payload if 'params' == 'raw' else None
    )
    post_api_test3 = apiResponse.json() if 'dict' == 'raw' else apiResponse.text


    import requests

    headers = {}
    
    payload = {}
    apiResponse = requests.get(
        'https://dummyjson.com/users',
        headers=headers,
        json=payload if 'params' == 'raw' else None
    )
    post_api_test4 = apiResponse.json() if 'list' == 'raw' else apiResponse.text

    record_to_be_added = {'first_name': first_name, 'last_name': last_name, 'id': id}
    new_user = models.User(**record_to_be_added)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    user_record = new_user


    import requests

    headers = {}
    
    payload = {}
    apiResponse = requests.delete(
        'https://jsonplaceholder.typicode.com/users/2',
        headers=headers,
        json=payload if 'params' == 'raw' else None
    )
    user_delete_api = apiResponse.json() if 'dict' == 'raw' else apiResponse.text
    res = {
        'user_inserted_record': user_record,
    }
    return res

async def put_user_id(db: Session, raw_data: schemas.PutUserId):
    id:str = raw_data.id
    first_name:str = raw_data.first_name
    last_name:str = raw_data.last_name


    user_edited_record = db.query(models.User).filter(models.User.id == id).first()
    for key, value in {'id': id, 'first_name': first_name, 'last_name': last_name}.items():
          setattr(user_edited_record, key, value)
    db.commit()
    db.refresh(user_edited_record)
    user_edited_record = user_edited_record



    import requests

    headers = {}
    
    payload = {'name': 'test', 'username': 'test', 'email': 'test'}
    apiResponse = requests.post(
        'https://jsonplaceholder.typicode.com/users',
        headers=headers,
        json=payload if 'raw' == 'raw' else None
    )
    user_get_api1 = apiResponse.json() if 'dict' == 'raw' else apiResponse.text


    import requests

    headers = {}
    
    payload = {'name': 'test', 'username': 'test', 'email': 'test'}
    apiResponse = requests.put(
        'https://jsonplaceholder.typicode.com/users/1',
        headers=headers,
        json=payload if 'raw' == 'raw' else None
    )
    user_update_api = apiResponse.json() if 'dict' == 'raw' else apiResponse.text
    res = {
        'user_edited_record': user_edited_record,
    }
    return res

async def delete_user_id(db: Session, id: int):

    user_deleted = None
    record_to_delete = db.query(models.User).filter(models.User.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        user_deleted = record_to_delete
    res = {
        'user_deleted': user_deleted,
    }
    return res

