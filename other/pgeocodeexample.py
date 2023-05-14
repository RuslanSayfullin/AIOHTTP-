from pgeocode import GeoQuery

# Create a CeoQuery object with the country code
geo = GeoQuery('IN')

# Get location information using postal code
location = geo.query_postal_code('110001')

# Print the retrieved location information
print(location)
