from fastapi import FastAPI

app=FastAPI()


@app.get('/')
async def root():
    return {"massage" : "hello"}

@app.get('/item/{item_id}')
async def root_item(item_id:int):
    return {"massage" :item_id}