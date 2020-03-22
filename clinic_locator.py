import json
from geopy.distance import lonlat, distance
__author__='Hendrik, Jean'
__status__='DEV'

class ClinicLocator:
    def __init__(self):
        with open('hospitals.geojson') as f:
            self.data = json.load(f)
        self.kkh_dic = {}
        self.kkh_ort={}
        for krankenhaus in self.data['features']:
            self.kkh_dic[krankenhaus['properties']['kh_name']] = krankenhaus['geometry']['coordinates']
            self.kkh_ort[krankenhaus['properties']['kh_name']] = krankenhaus['properties']['geo_ort']
    def get_coordinates_by_name(self, name):
        return self.kkh_dic[name]

    def get_ort_by_name(self, name):
        return self.kkh_ort[name]

    def get_hospitals_by_coordinates(self, la, lo, radius):  # radius in meter
        '''
        {
            "name": "Krankenhaus"
            "address": "Marienberg 99, 093773 Berlin",
            "distance": "3", //drei kilometer entfernt,
            "description": "Wir suchen 63 Blutabnehmer und zweie mit Erfahrung im Beatmen" (max)
        }
        '''
        dist_list = []  # (Distance,Name)
        for k in self.kkh_dic:
            dist_list.append((distance(lonlat(*(la, lo)), self.kkh_dic[k]).m, k))
        # print(min(dist, key=dist.get)) #nearest
        dist_list.sort(key=lambda tup: tup[0])  # sorts in place
        # print(dist_list[:5]) # N-nearest hospitals
        result = []
        for d in dist_list:
            if d[0] < radius:
                result.append(d[1])
            else:
                break
        return result
