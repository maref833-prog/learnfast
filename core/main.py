
from fastapi import FastAPI,Query,status,HTTPException,Path,UploadFile,File,Form
import uvicorn
import random
from typing import Annotated
from fastapi.responses import JSONResponse
from typing import Optional
app=FastAPI()
#تعریف دیتابیس 
namelists=[
    {'id':1,'name':"ali"},
    {'id':2,'name':"asghar"},
    {'id':3,'name':"mmd"},
    {'id':4,'name':"ahmad"},
    {'id':5,'name':"reza"},
    {'id':6,'name':"amir"},
    {'id':7,'name':"aref"}

]
#تست وصل شدن fast api
@app.get("/")
def root():
    return {'message':'hello world'}
#نمایش عناصر دیتابیس
@app.get("/name",status_code=200)
def resive():
  return namelists
#جستجو بر اساس id
@app.get("/name/id/{name_id}")
def name_idd(name_id:int):
    for name in namelists:
        if name["id"] == name_id:
            return name
    return JSONResponse(content="mofagh",status_code=200)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="peid nashod")
#جستجو بر اساس name
@app.get("/name/user/{name_name}",status_code=200)
def r(name_name:str):
    for name in namelists:
        if name['name'] ==name_name:
            return name
        
    return {"input":name_name}
#اضافه کردن
@app.post("/name",status_code=201)
def add(namea:str):
  n={'id':random.randint(8,100),'name':namea}
  namelists.append(n)
  return {"result":namea}
#آپدیت
@app.put("/name/{name_id}",status_code=200)
def update(name_id:int,name:str):
 for items in namelists:
    if items['id']==name_id:
       items['name']=name
       return items
#پاک کردن
@app.delete("/name/{name_id}",status_code=204)
def dele(name_id:int):
 for items in namelists:
    if items['id']==name_id:
       namelists.remove(items)
       return {"deatel:pak shod"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="peid nashod")
#استفاده از کوئری ها
@app.get("/search",status_code=200)
def re(q:str|None =Query(default=None,max_length=50,alias="update",title="update mikoned",description="anjam update")):
   if q:
      return [item for item in namelists if item['name']==q]
   return namelists
@app.post("/files/")
#خواندن فایل
async def create_file(
    file: Annotated[bytes, File()]
):
    return {
        "file_size": len(file),
    }