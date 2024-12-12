# Project Structure
# /project
# ├── api/
# │   └── index.py           # Main FastAPI application entry point
# ├── requirements.txt       # Python dependencies
# ├── vercel.json            # Vercel configuration file
# └── README.md              # Project documentation

# api/index.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

# Machine Parameter Model
class MachineParameter(BaseModel):
    machine_id: str
    parameter_name: str
    current_value: float
    unit: str
    timestamp: str
    status: Optional[str] = None
    threshold_min: Optional[float] = None
    threshold_max: Optional[float] = None

# FastAPI Application
app = FastAPI(
    title="Factory Machine Monitoring API",
    description="API for monitoring and tracking machine parameters in real-time",
    version="1.0.0"
)

# In-memory storage (replace with database in production)
machine_data = []

@app.post("/parameters", response_model=MachineParameter)
async def add_machine_parameter(parameter: MachineParameter):
    """
    Add a new machine parameter reading
    
    - Validate parameter values
    - Check against thresholds
    - Determine status
    """
    # Basic threshold validation
    if parameter.threshold_min is not None and parameter.current_value < parameter.threshold_min:
        parameter.status = "BELOW_THRESHOLD"
    elif parameter.threshold_max is not None and parameter.current_value > parameter.threshold_max:
        parameter.status = "ABOVE_THRESHOLD"
    else:
        parameter.status = "NORMAL"
    
    machine_data.append(parameter)
    return parameter

@app.get("/parameters", response_model=List[MachineParameter])
async def get_machine_parameters(
    machine_id: Optional[str] = None, 
    status: Optional[str] = None
):
    """
    Retrieve machine parameters with optional filtering
    
    - Filter by machine_id
    - Filter by status
    """
    filtered_data = machine_data
    
    if machine_id:
        filtered_data = [param for param in filtered_data if param.machine_id == machine_id]
    
    if status:
        filtered_data = [param for param in filtered_data if param.status == status]
    
    return filtered_data

@app.get("/health")
async def health_check():
    """
    Simple health check endpoint
    """
    return {"status": "healthy", "total_parameters": len(machine_data)}

# Error Handling
@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """
    Centralized exception handling
    """
    return {
        "error": "Internal Server Error", 
        "message": str(exc)
    }