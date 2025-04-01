from fastapi import Depends
from fastapi.routing import APIRouter

from src.company.dependencies import valid_new_company
from src.company.schemas import CompanySchema, NewCompanySchema

company_router = APIRouter(prefix="/company")


@company_router.post("/create/",
                     response_model=CompanySchema,
                     status_code=201)
async def create_company(company: NewCompanySchema = Depends(valid_new_company)):
    return company
