from fastapi import FastAPI
from pathlib import Path
import json
import uvicorn
from pydantic import BaseModel




app = FastAPI()

DB_PATH = Path("/app/db/shopping_list.json ")



def read_db():
    with DB_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)




@app.get("/items")
def get_items():
   db = read_db()
   return db



def write_db(data: dict) -> None:
    with DB_PATH.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)







class Products(BaseModel):
    id:int
    name: str
    quantity: int



@app.post("/items")
def create_items(product:Products):
    db = read_db()

    db.append ( {
        "id": product.id,
        "name":product.name,
        "quantity":product.quantity
    })

    write_db(db)
    return db




if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

