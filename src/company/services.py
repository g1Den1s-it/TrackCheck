from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.company.models import Company
from src.company.schemas import NewCompanySchema


async def create_company(company_data: NewCompanySchema, db: AsyncSession) -> Company | Exception:
    try:
        company = Company(
            company_address=company_data.company_address,
            company_name=company_data.company_name,
            company_email=company_data.company_email,
            company_phone=company_data.company_phone,
        )

        db.add(company)
        await db.commit()

        return company

    except Exception as e:
        await db.rollback()
        return e


async def get_list_companies(db: AsyncSession) -> list[Company] | Exception:
    try:
        query = select(Company)

        res = await db.execute(query)
        list_companies = list(res.scalars().all())

        return list_companies

    except Exception as e:
        await db.rollback()
        return e