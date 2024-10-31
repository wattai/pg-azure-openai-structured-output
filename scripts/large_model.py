from pydantic import BaseModel
from typing import List, Optional


class PersonalInfoModel(BaseModel):
    name: str
    age: int
    gender: Optional[str] = None
    email: str  # EmailStr


class AddressModel(BaseModel):
    country: str
    city: str
    postal_code: str
    street_address: str
    apartment_number: Optional[str] = None


class EducationModel(BaseModel):
    highest_degree: str
    institution_name: str
    graduation_year: int
    major: Optional[str] = None


class EmploymentModel(BaseModel):
    current_position: str
    company_name: str
    years_of_experience: int
    skills: List[str]


class HealthModel(BaseModel):
    has_allergies: bool
    allergies: Optional[List[str]] = None
    blood_type: Optional[str] = None
    has_chronic_conditions: bool
    chronic_conditions: Optional[List[str]] = None


class PreferencesModel(BaseModel):
    preferred_language: str
    hobbies: List[str]
    dietary_preferences: Optional[List[str]] = None
    favorite_genre: str


class FinancialModel(BaseModel):
    income: float
    has_debt: bool
    debt_amount: Optional[float] = None
    credit_score: Optional[int] = None


class ContactModel(BaseModel):
    primary_contact_number: str
    secondary_contact_number: Optional[str] = None
    emergency_contact_name: str
    emergency_contact_number: str


class TravelModel(BaseModel):
    has_passport: bool
    countries_visited: List[str]
    favorite_destination: Optional[str] = None
    travel_frequency_per_year: int


class FeedbackModel(BaseModel):
    survey_date: str  # date
    satisfaction_level: int  # 1 to 10 scale
    comments: Optional[str] = None
    suggestions: Optional[str] = None


class ParentModel(BaseModel):
    personal_info: PersonalInfoModel
    address: AddressModel
    education: EducationModel
    employment: EmploymentModel
    health: HealthModel
    preferences: PreferencesModel
    financial: FinancialModel
    contact: ContactModel
    travel: TravelModel
    feedback: FeedbackModel
