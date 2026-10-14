import os
from typing import List, Optional
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from models import (
    ZoneMetric,
    SimulationRequest,
    SimulationResponse,
    VisionAnalysisRequest,
    VisionAnalysisResponse,
    ResiliencePlanRequest,
    ResiliencePlanResponse,
    CitizenReportRequest,
    CitizenReportResponse
)
from services import (
    ZoneService,
    SimulationService,
    GeminiAIService
)

# Load environment variables
load_dotenv()

app = FastAPI(
    title="EcoPulse API - Autonomous Smart City Environmental Resilience Engine",
    description="Multimodal AI-powered platform for Urban Heat Island detection, micro-climate simulation, solar harvesting, and municipal climate action.",
    version="1.0.0"
)

# Allow CORS for Next.js frontend (default port 3000 / 3001)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "system": "EcoPulse Resilience Engine",
        "status": "operational",
        "gemini_api_configured": bool(os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")),
        "version": "1.0.0"
    }


@app.get("/api/health")
def health_check():
    api_key_set = bool(os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY"))
    return {
        "status": "healthy",
        "gemini_configured": api_key_set,
        "mode": "Live Gemini Multimodal" if api_key_set else "Intelligent Heuristic Simulation"
    }


@app.get("/api/samples")
def get_sample_images():
    """Retrieve preloaded aerial and urban imagery for one-click vision auditing."""
    samples_dir = os.path.join(os.path.dirname(__file__), "samples")
    meta = [
        {
            "id": "sample-downtown",
            "filename": "downtown_hotspot.jpg",
            "title": "Downtown Dense Urban Core (UHI Hotspot)",
            "description": "High asphalt and concrete canyon, 88 UHI index, severe thermal radiation.",
            "category": "Commercial Hub",
            "type": "aerial"
        },
        {
            "id": "sample-industrial",
            "filename": "industrial_rooftop.jpg",
            "title": "North Logistics Hub (Solar & Cool Roof Target)",
            "description": "Massive flat commercial roofs, low albedo, prime candidate for 14MW PV array.",
            "category": "Industrial Belt",
            "type": "rooftop"
        },
        {
            "id": "sample-residential",
            "filename": "residential_neighborhood.jpg",
            "title": "Eastside Residential (Canopy Deficit)",
            "description": "Narrow residential streets, dark tar roofs, sparse shade, vulnerable population.",
            "category": "Residential Core",
            "type": "aerial"
        },
        {
            "id": "sample-riverfront",
            "filename": "riverfront_greenery.jpg",
            "title": "West Riverfront Eco-Corridor (Green Benchmark)",
            "description": "Dense riparian vegetation, natural cooling corridor, low thermal stress.",
            "category": "Waterfront Eco-Corridor",
            "type": "satellite"
        }
    ]

    import base64
    result = []
    for item in meta:
        file_path = os.path.join(samples_dir, item["filename"])
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                b64 = base64.b64encode(f.read()).decode("utf-8")
                item_copy = dict(item)
                item_copy["image_base64"] = f"data:image/jpeg;base64,{b64}"
                result.append(item_copy)
    return result


@app.get("/api/zones", response_model=List[ZoneMetric])
def get_zones():
    """Retrieve all urban micro-climate zones with thermal and environmental telemetry."""
    return ZoneService.get_all_zones()


@app.get("/api/zones/{zone_id}", response_model=ZoneMetric)
def get_zone_by_id(zone_id: str):
    """Retrieve detailed telemetry for a specific urban zone."""
    zone = ZoneService.get_zone_by_id(zone_id)
    if not zone:
        raise HTTPException(status_code=404, detail=f"Zone '{zone_id}' not found")
    return zone


@app.post("/api/simulate", response_model=SimulationResponse)
def simulate_microclimate(req: SimulationRequest):
    """Simulate urban cooling interventions (canopy, cool roofs, solar PV, permeable pavement)."""
    return SimulationService.run_simulation(req)


@app.post("/api/analyze-vision", response_model=VisionAnalysisResponse)
def analyze_urban_imagery(req: VisionAnalysisRequest):
    """Analyze aerial, satellite, or street-level photos using Gemini Multimodal Vision."""
    return GeminiAIService.analyze_urban_image(req)


@app.post("/api/generate-plan", response_model=ResiliencePlanResponse)
def generate_resilience_plan(req: ResiliencePlanRequest):
    """Generate a municipal urban resilience and climate investment blueprint using Gemini AI."""
    return GeminiAIService.generate_resilience_plan(req)


@app.post("/api/citizen-report", response_model=CitizenReportResponse)
def submit_citizen_report(req: CitizenReportRequest):
    """Submit a citizen eco-audit, verifying heat pockets or greening opportunities with AI."""
    return GeminiAIService.process_citizen_report(req)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
