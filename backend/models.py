# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2024-05-07T16:58:42+00:00

from __future__ import annotations

# modified by laia-gen-lib:

from pydantic import ConfigDict
from laiagenlib.Domain.LaiaBaseModel.LaiaBaseModel import LaiaBaseModel
from laiagenlib.Domain.LaiaUser.LaiaUser import LaiaUser
from laiagenlib.Domain.GeoJSON.Geometry import Type, Geometry, LineString, MultiLineString, MultiPoint, MultiPolygon, Point, Polygon

from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, Field


class FlightPlan(LaiaBaseModel):
    model_config = ConfigDict(json_schema_extra={'x-frontend-defaultFields': ['name', 'date', 'drone_reference', 'mission_details', 'route']})
    name: str = Field(..., title='Name', x_frontend_fieldName="Name", x_frontend_fieldDescription="This is the Name of the FlightPlan", x_frontend_editable=True, x_frontend_placeholder="Write the Name of this FlightPlan")
    date: Optional[datetime] = Field(None, title='Date', x_frontend_fieldName="Flight Date", x_frontend_fieldDescription="Departure Datetime of the FlightPlan", x_frontend_editable=True, x_frontend_placeholder="Select a Datetime")
    drone_reference: str = Field(..., title='Drone Reference', x_frontend_fieldName="Drone Reference", x_frontend_fieldDescription="This is the Drone Reference", x_frontend_editable=True, x_frontend_placeholder="Add the Drone Reference")
    mission_details: Optional[str] = Field('', title='MissionDetails', x_frontend_fieldName="Mission Details", x_frontend_fieldDescription="These are the important details for the mission", x_frontend_editable=True, x_frontend_placeholder="Write the mission details here")
    route: Optional[LineString] = Field(None, title='Route', x_frontend_fieldName="Route", x_frontend_fieldDescription="This is Route of the FlightPlan", x_frontend_editable=True, x_frontend_placeholder="Add the coordinates for the Route", x_frontend_uspaceMap=True)
