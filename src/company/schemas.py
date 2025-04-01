from pydantic import BaseModel, EmailStr


class NewCompanySchema(BaseModel):
    company_name: str
    company_address: str | None = None
    company_email: EmailStr
    company_phone: str | None = None


class UpdateCompanySchema(BaseModel):
    company_name: str | None = None
    company_address: str | None = None
    company_email: EmailStr | None = None
    company_phone: str | None = None


class CompanySchema(BaseModel):
    company_id: int
    company_name: str | None = None
    company_address: str | None = None
    company_email: EmailStr
    company_phone: str | None = None

