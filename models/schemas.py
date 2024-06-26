from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class Strategy(BaseModel):
    industry: str
    niche: str
    country: str


class Base(BaseModel):
    niche: str
    industry: str


class UserRegister(BaseModel):
    firstname: str = Field(...)
    lastname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)


class UserUpdate(BaseModel):
    firstname: Optional[str] = Field(...)
    lastname: Optional[str] = Field(...)
    email: Optional[EmailStr] = Field(...)
    password: Optional[str] = Field(...)


class UserInput(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)


class User(BaseModel):
    id: int
    firstname: str
    lastname: str
    email: str

    class Config:
        from_attributes = True


class BaseBody(BaseModel):
    name: str | None = None
    font: str | None = None
    strategy: str | None = None
    color: str | None = None
    logo: str | None = None
    messaging: str | None = None
    photography: str | None = None
    illustration: str | None = None
    presentation: str | None = None


class LogoVariant(BaseModel):
    name: str
    url: str

    niche: str
    industry: str


class Logo(BaseModel):
    variants: list[LogoVariant]


class Brand(BaseModel):
    id: int
    name: str
    font: str
    strategy: str
    color: list[str]
    logo: str
    messaging: str
    photography: str
    illustration: str
    presentation: str
    owner_id: int

    class Config:
        from_attributes = True
