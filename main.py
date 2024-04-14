from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import JSONResponse
import httpx
import base64 
import os
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
load_dotenv()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/history")
async def read_history(request: Request):
    return templates.TemplateResponse("history.html", {"request": request})

# api処理
@app.get("/api/posts")
async def get_posts():
    url = os.getenv("API_URL")
    headers = {
        "X-Cybozu-API-Token": os.getenv("API_KEY_MESSAGE")
    }
    params = {
        "app": "5",  # アプリケーションID
        #fields": ["user_id", "user_name", "message", "作成日時"],
        "fields": ["user_id", "message", "作成日時"],
        "query":"order by 作成日時 desc limit 20"
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, params=params)
            response.raise_for_status()  # ステータスコードが400以上の場合、例外を発生させる
            return response.json()
        except httpx.HTTPStatusError as exc:
            raise HTTPException(status_code=exc.response.status_code, detail=str(exc))

@app.get("/api/history")
async def search_records(user_id: str):  
    print(f"URL: {API_URL}, Key Message: {API_KEY_MESSAGE}, Key Reaction: {API_KEY_REACTION}")


    print("test")
    api_url = os.getenv("API_URL")
    app_id = "6"
    api_token = os.getenv("API_KEY_REACTION")
    headers = {
        "X-Cybozu-API-Token": api_token,
    }
    query = f'user_id = "{user_id}"'

    params = {
        "app": app_id,
        "fields": ["user_name","reaction", "作成日時"],
        "query": f"{query} order by 作成日時 desc limit 10"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(api_url, headers=headers, params=params)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to retrieve records from kintone")

    return response.json()




    # リクエストデータのモデルを定義
class RecordData(BaseModel):
    user_id: str
    # user_name: str
    reaction: str


# kintoneに新しいレコードを追加するエンドポイント
@app.post("/api/reaction")
async def add_kintone_record(data: RecordData):
    url = os.getenv("API_URL")
    headers = {
        "X-Cybozu-API-Token": os.getenv("API_KEY_REACTION"),
        "Content-Type": "application/json"
    }
    # kintoneのフィールドコードに基づいてパラメータを設定
    params = {
        "app": "6",  # アプリケーションID
        "record": {
            "user_id": {
                "value": data.user_id
            },
            # "user_name": {
            #     "value": data.user_name
            # },
            "reaction": {
                "value": data.reaction
            }
        }
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=params)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to retrieve records from kintone")

    return response.json()