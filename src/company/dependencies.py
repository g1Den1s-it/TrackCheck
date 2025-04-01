from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.company.exceptions import HTTPDatabaseError, HTTPClientException, HTTPClientInputException
from src.database import get_db_session
from src.company import services
from src.company.schemas import CompanySchema, NewCompanySchema, UpdateCompanySchema


async def valid_new_company(company_data: NewCompanySchema,
                            db: AsyncSession = Depends(get_db_session)) -> CompanySchema:
    if not company_data:
        raise HTTPClientInputException("Invalid company data provided. Please check your input.")

    company = await services.create_company(company_data, db)

    if isinstance(company, Exception):
        raise HTTPDatabaseError()

    return CompanySchema.model_validate(company, from_attributes=True)


async def valid_list_companies(db: AsyncSession = Depends(get_db_session)
                               ) -> list[CompanySchema]:
    list_companies = await services.get_list_companies(db)

    if isinstance(list_companies, Exception):
        raise HTTPDatabaseError()

    list_companies = [
        CompanySchema.model_validate(company, from_attributes=True)
        for company in list_companies
    ]

    return list_companies


async def valid_company(id: int, db: AsyncSession = Depends(get_db_session)):
    if not id:
        raise HTTPClientException("Company ID is required.")

    company = await services.get_current_company(id, db)

    if isinstance(company, Exception):
        raise HTTPDatabaseError()

    return CompanySchema.model_validate(company, from_attributes=True)


async def valid_update_company(id: int,
                               update_data: UpdateCompanySchema,
                               db: AsyncSession = Depends(get_db_session)
                               ) -> CompanySchema:
    if not id:
        raise HTTPClientException("Company ID is required.")

    if not update_data:
        raise HTTPClientInputException("No valid data provided for update. Please check your input.")

    updated_company = await services.update_company(id, update_data, db)

    if isinstance(updated_company, Exception):
        raise HTTPDatabaseError()

    if not updated_company:
        raise HTTPClientException("Company does not exist.")

    return CompanySchema.model_validate(updated_company, from_attributes=True)


async def valid_delete_company(id: int,
                               db: AsyncSession = Depends(get_db_session)
                               ) -> str:
    if not id:
        raise HTTPClientException("Company ID is required.")

    status = await services.delete_company(id, db)

    if isinstance(status, Exception):
        raise HTTPDatabaseError()

    return "Successfully"
