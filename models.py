from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field

class ZoneMetric(BaseModel):
    id: str
    name: str
    category: str  # "Commercial Hub", "Industrial Belt", "Residential Core", "Waterfront Eco-Corridor", "Suburban Sprawl"
    center: List[float] = Field(..., description="[lat, lon]")
    polygon: List[List[float]] = Field(..., description="List of [lat, lon] coordinates")
    current_temp_c: float
    baseline_temp_c: float
    temp_anomaly_c: float
    heat_island_index: int = Field(..., ge=0, le=100)
    aqi: int
    canopy_cover_pct: float
    albedo_score: float  # 0.0 to 1.0 (reflectivity)
    solar_potential_mwh: float
    vulnerability_tier: str  # "Low", "Moderate", "High", "Critical"
    population: int
    key_interventions: List[str]

class SimulationRequest(BaseModel):
    zone_id: str
    canopy_increase_pct: float = Field(0.0, ge=0.0, le=50.0)
    cool_roof_adoption_pct: float = Field(0.0, ge=0.0, le=100.0)
    solar_pv_coverage_pct: float = Field(0.0, ge=0.0, le=100.0)
    permeable_pavement_pct: float = Field(0.0, ge=0.0, le=100.0)

class SimulationResponse(BaseModel):
    zone_id: str
    zone_name: str
    original_temp_c: float
    projected_temp_c: float
    temp_reduction_c: float
    surface_cooling_c: float
    heat_stress_hours_saved_annually: int
    annual_carbon_offset_metric_tons: float
    annual_energy_savings_mwh: float
    estimated_annual_cost_savings_usd: float
    roi_payback_years: float
    resilience_score_delta: int
    new_resilience_score: int
    executive_takeaway: str
    recommended_tree_species: List[str]

class VisionAnalysisRequest(BaseModel):
    image_base64: str
    image_type: str = "aerial"  # "aerial", "satellite", "street", "rooftop"
    location_name: Optional[str] = "Metropolitan Zone"
    custom_notes: Optional[str] = None

class VisionAnalysisResponse(BaseModel):
    status: str
    location_name: str
    surface_composition: Dict[str, float]  # e.g. {"impervious_asphalt": 45, "concrete_structures": 30, "vegetation_canopy": 12, "water_bodies": 3, "reflective_surfaces": 10}
    estimated_surface_temp_c: float
    heat_island_risk_level: str  # "Low", "Moderate", "High", "Extreme"
    canopy_deficit_pct: float
    solar_suitability: Dict[str, Any]
    detected_vulnerabilities: List[str]
    priority_interventions: List[Dict[str, Any]]
    gemini_ai_diagnosis: str
    is_mock: bool = False

class ResiliencePlanRequest(BaseModel):
    city_name: str
    target_year: int = 2030
    budget_level: str = "balanced"  # "conservative", "balanced", "aggressive"
    focus_priorities: List[str] = ["Heat Island Abatement", "Renewable Solar Harvest", "Air Quality & Canopy", "Social Equity"]
    selected_zone_ids: Optional[List[str]] = None

class ResiliencePlanResponse(BaseModel):
    city_name: str
    generated_at: str
    executive_summary: str
    strategic_pillars: List[Dict[str, Any]]
    zone_allocation_table: List[Dict[str, Any]]
    environmental_impact_projections: Dict[str, Any]
    financial_roadmap: Dict[str, Any]
    policy_recommendations: List[str]
    markdown_report: str
    is_mock: bool = False

class CitizenReportRequest(BaseModel):
    citizen_name: str
    neighborhood: str
    category: str
    description: str
    lat: float
    lon: float
    image_base64: Optional[str] = None

class CitizenReportResponse(BaseModel):
    report_id: str
    status: str
    verification_tier: str
    points_awarded: int
    badge: str
    ai_validation_summary: str
    estimated_neighborhood_impact: str
