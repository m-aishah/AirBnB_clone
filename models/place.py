#!/usr/bin/python3
'''Defines the child class - Place.'''

from models.base_model import BaseModel


class Place(BaseModel):
    '''Child class that represents Place.

    Attributes:
        city_id (str) - The City's id.
        user_id (str) - The User's id.
        name (str) - The name of the place.
        description (str) - A description of the place.
        number_rooms (int) - The number of rooms in the place.
        number_bathrooms (int) - The number of bathrooms in the place.
        max_guest (int) - The maximum of guests that can stay in the place.
        price_by_night (int) - How much the place costs per night.
        latitude (float) - The latitude of the place.
        longitude (float) - The longitude of the place.
        amenity_ids (list) - A list of the Amenity ids.
    '''

    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
