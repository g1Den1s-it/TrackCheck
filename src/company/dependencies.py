from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db_session
from src.company import services
from src.company.schemas import CompanySchema, NewCompanySchema, UpdateCompanySchema


async def valid_new_company(company_data: NewCompanySchema,
                            db: AsyncSession = Depends(get_db_session)) -> CompanySchema:
    if not company_data:
        raise

    company = await services.create_company(company_data, db)

    if isinstance(company, Exception):
        raise company

    return CompanySchema.model_validate(company, from_attributes=True)


async def valid_list_companies(db: AsyncSession = Depends(get_db_session)
                               ) -> list[CompanySchema]:
    list_companies = await services.get_list_companies(db)

    if isinstance(list_companies, Exception):
        raise list_companies

    list_companies = [CompanySchema.model_validate(company, from_attributes=True) for company in list_companies]

    return list_companies


async def valid_company(id: int, db: AsyncSession = Depends(get_db_session)):
    if not id:
        raise

    company = await services.get_current_company(id, db)

    if isinstance(company, Exception):
        raise company

    return CompanySchema.model_validate(company, from_attributes=True)


async def valid_update_company(id: int,
                               update_data: UpdateCompanySchema,
                               db: AsyncSession = Depends(get_db_session)
                               ) -> CompanySchema:
    if not id:
        raise

    if not update_data:
        raise

    updated_company = await services.update_company(id, update_data, db)

    if isinstance(updated_company, Exception):
        raise updated_company

    return CompanySchema.model_validate(updated_company, from_attributes=True)

