import json
from geopy.distance import lonlat, distance

__author__ = 'Hendrik, Jean'
__status__ = 'DEV'

'''
    Final
'''
class ClinicLocator:
    def __init__(self):
        with open('hospitals.geojson') as f:
            self.data = json.load(f)
        self.kkh_dic = {}
        self.kkh_ort = {}
        self.kkh_strasse = {}
        self.kkh_plz = {}
        for krankenhaus in self.data['features']:
            self.kkh_dic[krankenhaus['properties']['kh_name']] = krankenhaus['geometry']['coordinates']
            self.kkh_ort[krankenhaus['properties']['kh_name']] = krankenhaus['properties']['geo_ort']
            self.kkh_strasse[krankenhaus['properties']['kh_name']] = krankenhaus['properties']['geo_street'] + " " + \
                                                                     krankenhaus['properties']['geo_nr']
            self.kkh_plz[krankenhaus['properties']['kh_name']] = krankenhaus['properties']['geo_plz']

    def get_coordinates_by_name(self, name):
        return self.kkh_dic[name]

    def get_ort_by_name(self, name):
        return self.kkh_ort[name]

    def get_strasse_by_name(self, name):
        return self.kkh_strasse[name]

    def get_plz_by_name(self, name):
        return self.kkh_plz[name]

    def get_hospitals_by_coordinates(self, la, lo, radius):  # radius in meter

        dist_list = []  # (Distance,Name)
        for k in self.kkh_dic:
            dist_list.append((distance(lonlat(*(la, lo)), self.kkh_dic[k]).m, k))
        # print(min(dist, key=dist.get)) #nearest
        dist_list.sort(key=lambda tup: tup[0])  # sorts in place
        # print(dist_list[:5]) # N-nearest hospitals
        result = []
        for d in dist_list:
            if d[0] < radius:
                entry = {'distance': d[0], 'name': d[1], 'strasse': self.get_strasse_by_name(d[1]),
                         'plz': self.get_plz_by_name(d[1]), 'ort': self.get_ort_by_name(d[1])}
                result.append(entry)
            else:
                break
        return result

