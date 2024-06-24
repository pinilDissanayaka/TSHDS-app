from fastapi import FastAPI, HTTPException, Request
from database.user import User

app=FastAPI()
user=User()


@app.get('/')
async def root():
    return {"massage" : "hello"}

@app.get('/item/{item_id}')
async def root_item(item_id:int):
    return {"massage" :user}


@app.post('/add_user')
async def addUser(request :Request):
    try:
        data=await request.json()
        
        if 'userName' not in data or 'password' not in data:
            raise HTTPException(status_code=422,
                                detail="Incomplete data provided")
        else:
            user.addUser(data=data)
    except HTTPException as e:
        raise e
    
            