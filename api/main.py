"""
Main API Application File

This module serves as the entry point for our Factory Machine Monitoring API.
It sets up the FastAPI application, defines root endpoints, and serves as the 
central configuration point for our web service.

Key Responsibilities:
- Initialize FastAPI application
- Define root/health check endpoints
- Configure global middleware (if needed)
- Set up application-wide settings
"""

from fastapi import FastAPI
from datetime import datetime

# Create FastAPI application instance
# This is the core of our API, handling routing, documentation, and request management
app = FastAPI(
    title="Factory Machine Monitoring API",  # Descriptive title for API documentation
    description="API for tracking and monitoring factory machine parameters",
    version="0.1.0",  # Semantic versioning of the API
    # Additional metadata can be added here
    contact={
        "name": "Dwika Widyantama",
        "email": "support@factorymonitoring.com"
    }
)

# Root endpoint: Provides basic API information and health check
@app.get("/")
def read_root():
    """
    Root endpoint for API health check and basic information.
    
    Returns:
        dict: Current API status and timestamp
    
    Purpose:
    - Confirms API is running
    - Provides basic system information
    - Can be used by monitoring systems to check service health
    """
    return {
        "message": "Welcome to Factory Monitoring API",
        "timestamp": datetime.utcnow(),
        "status": "healthy"
    }