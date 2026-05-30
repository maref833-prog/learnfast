from fastapi import FastAPI,Query
import uvicorn
import random
from typing import Annotated
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
@app.get("/name")
def resive():
  return namelists
#جستجو بر اساس id
@app.get("/name/id/{name_id}")
def name_idd(name_id:int):
    for name in namelists:
        if name["id"] == name_id:
            return name
 
    return {"input":name_id}
#جستجو بر اساس name
@app.get("/name/user/{name_name}")
def r(name_name:str):
    for name in namelists:
        if name['name'] ==name_name:
            return name
        
    return {"input":name_name}
#اضافه کردن
@app.post("/name")
def add(namea:str):
  n={'id':random.randint(8,100),'name':namea}
  namelists.append(n)
  return {"result":namea}
#آپدیت
@app.put("/name/{name_id}")
def update(name_id:int,name:str):
 for items in namelists:
    if items['id']==name_id:
       items['name']=name
       return items
#پاک کردن
@app.delete("/name/{name_id}")
def dele(name_id:int):
 for items in namelists:
    if items['id']==name_id:
       namelists.remove(items)
       return {"deatel:pak shod"}
 return{"deatel:peida nashod"}
@app.get("/search")
def re(q:str|None =Query(default=None,max_length=50)):
   if q:
      return [item for item in namelists if item['name']==q]
   return namelists