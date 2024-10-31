from pydantic import BaseModel
from typing import List


class PersonalInfoModel(BaseModel):
    name: str
    age: int
    gender: str
    email: str
    marital_status: str
    nationality: str
    date_of_birth: str
    phone_number: str
    occupation: str
    primary_language: str
    secondary_language: str
    number_of_children: int
    height_cm: float
    weight_kg: float
    favorite_color: str
    personality_type: str
    preferred_contact_method: str
    timezone: str
    profile_picture_url: str
    bio: str


class AddressModel(BaseModel):
    country: str
    city: str
    postal_code: str
    street_address: str
    apartment_number: str
    region: str
    nearest_landmark: str
    address_type: str
    coordinates_latitude: float
    coordinates_longitude: float
    building_name: str
    is_residential: bool
    floor_number: int
    is_owned: bool
    years_at_address: int
    previous_address: str
    rent_amount: float
    property_tax: float
    maintenance_fees: float
    additional_directions: str


class EducationModel(BaseModel):
    highest_degree: str
    institution_name: str
    graduation_year: int
    major: str
    minors: List[str]
    gpa: float
    is_honors: bool
    attended_online: bool
    scholarships: List[str]
    study_abroad: bool
    languages_studied: List[str]
    professional_certifications: List[str]
    thesis_title: str
    research_area: str
    awards_received: List[str]
    volunteer_work: str
    student_organizations: List[str]
    favorite_subject: str
    least_favorite_subject: str
    extracurricular_activities: List[str]


class FinancialModel(BaseModel):
    annual_income: float
    savings: float
    investment_portfolio_value: float
    monthly_expenses: float
    retirement_fund: float
    credit_score: int
    has_insurance: bool
    loan_balance: float
    loan_interest_rate: float
    mortgage_balance: float
    rent_or_own: str
    bank_name: str
    financial_goals: List[str]
    emergency_fund: float
    tax_bracket: str
    debts: List[str]
    investments: List[str]
    retirement_plan_type: str
    is_financially_independent: bool
    preferred_payment_method: str


class SocialMediaModel(BaseModel):
    facebook_url: str
    twitter_handle: str
    instagram_username: str
    linkedin_url: str
    tiktok_username: str
    snapchat_username: str
    youtube_channel_url: str
    followers_count: int
    posts_per_week: int
    most_used_platform: str
    is_influencer: bool
    influencer_category: str
    engagement_rate: float
    content_types_shared: List[str]
    preferred_sharing_times: List[str]
    social_media_goals: str
    following_count: int
    hashtags_used: List[str]
    preferred_interaction_type: str
    ads_shown_per_day: int


class ContactModel(BaseModel):
    primary_contact_number: str
    secondary_contact_number: str
    emergency_contact_name: str
    emergency_contact_number: str
    preferred_contact_time: str
    preferred_contact_days: List[str]
    alternative_email: str
    fax_number: str
    skype_id: str
    telegram_handle: str
    whatsapp_number: str
    signal_number: str
    wechat_id: str
    primary_address: str
    alternative_address: str
    preferred_messaging_app: str
    has_viber: bool
    has_line: bool
    has_messenger: bool
    contact_notes: str
    preferred_response_time: str


class TravelModel(BaseModel):
    has_passport: bool
    countries_visited: List[str]
    favorite_destination: str
    travel_frequency_per_year: int
    travel_insurance: bool
    preferred_airline: str
    airline_frequent_flyer_status: str
    hotel_preferences: List[str]
    travel_budget: float
    upcoming_trips: List[str]
    preferred_travel_season: str
    visa_status: str
    preferred_transport_mode: str
    favorite_activity_abroad: str
    last_trip_duration_days: int
    travel_companions: List[str]
    carries_travel_health_kit: bool
    uses_travel_planner_apps: bool
    has_multiple_passports: bool
    travel_reviews_written: int


class FeedbackModel(BaseModel):
    survey_date: str
    satisfaction_level: int
    comments: str
    suggestions: str
    likes: List[str]
    dislikes: List[str]
    improvement_areas: List[str]
    additional_feedback: str
    rating_out_of_five: int
    likely_to_recommend: int
    reviewer_id: int
    email_contact_permission: bool
    phone_contact_permission: bool
    follow_up_requested: bool
    survey_completed_on_time: bool
    review_publication_permission: bool
    general_sentiment: str
    frequency_of_feedback_submission: int
    has_submitted_feedback_before: bool
    overall_experience_comment: str


class ParentModel(BaseModel):
    personal_info: PersonalInfoModel
    address: AddressModel
    education: EducationModel
    financial: FinancialModel
    social_media: SocialMediaModel
    contact: ContactModel
    travel: TravelModel
    feedback: FeedbackModel
