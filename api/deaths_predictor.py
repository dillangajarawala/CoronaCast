from pickle import load
from sklearn import linear_model
from sklearn import preprocessing

pop_hash = {'al': 4903185, 'ak': 731545, 'as': 55312, 'az': 7278717, 'ar': 3017804, 'ca': 39512223, 'co': 5758736, 'ct': 3565287, 'de': 973764, 'dc': 705749, 'fm': 104929, 'fl': 21477737, 'ga': 10617423, 'gu': 167294, 'hi': 1415872, 'id': 1787065, 'il': 12671821, 'in': 6732219, 'ia': 3155070, 'ks': 2913314, 'ky': 4467673, 'la': 4648794, 'me': 1344212, 'mh': 58791, 'md': 6045680, 'ma': 6892503, 'mi': 9986857, 'mn': 5639632, 'ms': 2976149, 'mo': 6137428, 'mt': 1068778, 'ne': 1934408, 'nv': 3080156, 'nh': 1359711, 'nj': 8882190, 'nm': 2096829, 'ny': 19453561, 'nc': 10488084, 'nd': 762062, 'mp': 51994, 'oh': 11689100, 'ok': 3956971, 'or': 4217737, 'pw': 18008, 'pa': 12801989, 'pr': 3193694, 'ri': 1059361, 'sc': 5148714, 'sd': 884659, 'tn': 6829174, 'tx': 28995881, 'ut': 3205958, 'vt': 623989, 'vi': 104578, 'va': 8535519, 'wa': 7614893, 'wv': 1792147, 'wi': 5822434, 'wy': 578759}

class DeathsPredictor(object):

    def __init__(self):
        self.model = load(open("./../model/deathsmodel.pkl", 'rb'))
        self.scaler = load(open("./../model/deathsscaler.pkl"), 'rb')
    
    def get_state_population(state):
        return pop_hash[state]
    
    def scale_features(self, features_to_be_scaled):
        x = self.scaler.transform([features_to_be_scaled]).toarray()[0]
        return x
    
    def predict_cases(self, cases, features_to_be_scaled, state):
        state_population = self.get_state_population(state)
        scaled_features = self.scale_features([state_population] + features_to_be_scaled)
        features = scaled_features + cases
        deaths = self.model.predict([features])[0]
        return deaths
    
