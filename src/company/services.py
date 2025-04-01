from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.company.models import Company
from src.company.schemas import NewCompanySchema, UpdateCompanySchema


async def create_company(company_data: NewCompanySchema,
                         db: AsyncSession) -> Company | Exception:
    try:
        company = Company(
            company_address=company_data.company_address,
            company_name=company_data.company_name,
            company_email=company_data.company_email,
            company_phone=company_data.company_phone,
            user1=company_data.user1,
            user2=company_data.user2,
            user3=company_data.user3
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


async def get_current_company(company_id: int,
                              db: AsyncSession) -> Company | Exception:
    try:
        query = select(Company).where(Company.company_id == company_id)

        res = await db.execute(query)
        company = res.scalars().first()

        return company

    except Exception as e:
        await db.rollback()
        return e


async def update_company(company_id: int,
                         update_data: UpdateCompanySchema,
                         db: AsyncSession) -> Company | Exception:
    try:
        query = (update(Company)
                 .where(Company.company_id == company_id)
                 .values(update_data.model_dump(exclude_none=True))
                 .returning(Company))

        res = await db.execute(query)
        await db.commit()

        updated_company = res.scalars().first()

        return updated_company

    except Exception as e:
        await db.rollback()
        return e


async def delete_company(company_id: int,
                         db: AsyncSession) -> None | Exception:
    try:
        query = delete(Company).where(Company.company_id == company_id)

        await db.execute(query)
        await db.commit()

    except Exception as e:
        await db.rollback()
        return e
