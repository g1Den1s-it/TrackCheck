from fastapi import Depends
from fastapi.routing import APIRouter

from src.company.dependencies import valid_new_company, valid_list_companies
from src.company.schemas import CompanySchema, NewCompanySchema
from src.company.services import get_list_companies

company_router = APIRouter(prefix="/company")


@company_router.post("/create/",
                     response_model=CompanySchema,
                     status_code=201)
async def create_company(company: NewCompanySchema = Depends(valid_new_company)):
    return company


@company_router.get("/list/",
                    response_model=list[CompanySchema],
                    status_code=200)
async def list_companies(companies: list[CompanySchema] = Depends(valid_list_companies)):
    return companies
