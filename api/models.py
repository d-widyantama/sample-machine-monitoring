"""
Data Models Module

Defines Pydantic models for data validation and serialization.
Pydantic ensures type safety, provides automatic documentation,
and helps prevent invalid data from entering the system.
"""

from pydantic import BaseModel, Field
from datetime import datetime

class MachineParameters(BaseModel):
    """
    Represents a comprehensive set of machine parameters.
    
    Design Considerations:
    - Uses Pydantic for automatic validation
    - Provides type hints for each parameter
    - Includes default values and field constraints
    
    Key Features:
    - Automatic timestamp generation
    - Field-level validation
    - Easy serialization/deserialization
    """
    
    # Timestamp of data collection, defaults to current UTC time
    timestamp: datetime = Field(
        default_factory=datetime.utcnow, 
        description="Automatic timestamp for data collection"
    )
    
    # Example fields with validation
    # Add more fields specific to your factory monitoring needs
    efficiency: float = Field(
        ...,  # Ellipsis means this field is required
        ge=0,  # Greater than or equal to 0
        le=100,  # Less than or equal to 100
        description="Machine efficiency percentage (0-100)"
    )
    
    # Additional placeholder fields
    status: str = Field(
        description="Current machine operational status",
        examples=["Running", "Stopped", "Maintenance"]
    )
