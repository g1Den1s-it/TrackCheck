from fastapi import Depends
from fastapi.routing import APIRouter

from src.company.dependencies import valid_new_company, valid_list_companies, valid_company, valid_update_company
from src.company.schemas import CompanySchema, NewCompanySchema, UpdateCompanySchema

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


@company_router.get("/{id}/",
                     response_model=CompanySchema,
                     status_code=200)
async def get_company(company: CompanySchema = Depends(valid_company)):
    return company


@company_router.post("/{id}/update/",
                     response_model=CompanySchema,
                     status_code=200)
async def update_company(company: UpdateCompanySchema = Depends(valid_update_company)):
    return company

