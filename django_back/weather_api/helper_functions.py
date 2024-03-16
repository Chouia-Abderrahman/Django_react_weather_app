from geopy.geocoders import Nominatim


def get_coordinates(location_name):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(location_name)

    if location:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude
    else:
        return None, None

#
# # Example usage:
location_name = "Annaba"
latitude, longitude = get_coordinates(location_name)
# if latitude is not None and longitude is not None:
#     print(f"Latitude: {latitude}, Longitude: {longitude}")
# else:
#     print("Location not found or coordinates not available.")
