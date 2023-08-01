from fastapi import APIRouter, Query, status, HTTPException
from typing import List, Union
import edgedb
from queries import (
    get_company_async_edgeql as get_company_qry,
    create_company_async_edgeql as create_company_qry,
)
from schemas.company_schema import Company

router = APIRouter()
client = edgedb.create_async_client()


@router.get("/company_profile", response_model=Company)
async def get_company() -> get_company_qry.GetCompanyResult:
    """
    Get company profile.
    """
    company = await get_company_qry.get_company(client)
    return company


@router.post(
    "/company_profile", status_code=status.HTTP_201_CREATED, response_model=Company
)
async def create_company(company: Company) -> create_company_qry.CreateCompanyResult:
    """
    Create a new company profile.
    """
    try:
        created_company = await create_company_qry.create_company(
            client,
            name=company.name,
            founded_date=company.founded_date,
            country=company.country,
            website=company.website,
            email=company.email,
            contact_no=company.contact_no,
        )
    except edgedb.errors.ConstraintViolationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": f"Company '{company.name}' already exists."},
        )
    return created_company
