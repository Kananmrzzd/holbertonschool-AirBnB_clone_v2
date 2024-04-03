#!/usr/bin/python3
""" Place Module for HBNB project """
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review


place_association = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60), ForeignKey("places.id"),
           primary_key=True),
    Column('amenity_id', String(60), ForeignKey("amenities.id"),
           primary_key=True)
    )

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship('Review', cascade='all, delete', backref='place')
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))
    amenities = relationship('Amenity', secondary='place_amenity',
                             viewonly=False)
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """getter function"""
            from models import storage
            result = []
            review = storage.all(Review).values()
            for rev in review:
                if rev.place_id == self.id:
                    result.append(rev)
            return result

        @property
        def amenities(self):
            """getter Function"""
            from models import storage
            result = []
            all_amenities = storage.all(Amenity).values()
            for amenity in all_amenities:
                if amenity.id in self.amenity_ids:
                    result.append(amenity)
            return result

        @amenities.setter
        def amenities(self, obj):
            """setter Function"""
            if type(obj) is Amenity:
                self.amenity_ids.append(obj.id)
