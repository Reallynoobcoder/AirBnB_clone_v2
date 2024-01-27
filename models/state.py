#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class for storing state information """

    __tablename__ = 'states'
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade="all,delete", backref="state")
    else:
        name = ""

    def cities(self):
        """getter docuemnt"""
        from models import storage
        citiesList = []
        citiesAll = storage.all(City)
        for city in citiesAll.values():
            if city.state_id == self.id:
                citiesList.append(city)
        return citiesList
