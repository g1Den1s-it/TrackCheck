from fastapi import FastAPI

from src.company.routers import company_router

app = FastAPI()
app.include_router(company_router)

