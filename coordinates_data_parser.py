import re

class CoordinatesDataParser:
    def __init__(self):
        return

    def get_coords(self, response):
        html = response.xpath('.//body').extract_first()
        longitude = re.search(r'-\d+\.\d{5,}', html)
        longitude = longitude.group() if longitude else None
        if longitude:
            # split response.html into a list of 2 parts 
            html_section = html.split(longitude)
            # find latitude based on location of longitude
            for section in html_section:
                latitude = re.search(r'\d{2}\.\d{5,}', section)
                latitude = latitude.group() if latitude else None
                if latitude:
                    break
            return {'latitude': latitude, 'longitude': longitude}
        return None
