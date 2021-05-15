import pandas as pd
import pickle
from sklearn.externals import joblib
import argparse

parser = argparse.ArgumentParser('my_parser')

def predict_model(filename):
  lst_drops = ['92', 'Прожиточный минимум']
  drop_list = ['Регион','Качество жизни']
  target = 'Качество жизни'
  df1 = df.copy(deep = True).drop(lst_drops, axis=1)
  df1 = df1.copy(deep = True).drop(drop_list, axis = 1)
  x_test_scaled = (x_test-np.min(x_test))/(np.max(x_test)-np.min(x_test))
  clf=Ridge(alpha = 1, solver= 'sparse_cg')
  loaded_model = pickle.load(open('finalized_model.pklz', 'rb'))
  result = loaded_model.predict(x_test_scaled)
  return result

if __name__ == '__main__':
    parser.add_argument('--input_filename')
    args = parser.parse_args()
    filename = args.input_filename
    predict_model(input_filename)


    >>> import requests

    >>> r = requests.get('https://jfx.ac/hero/heroes.txt')
    >>> names = [n for n in r.text.split('\n')]
    >>> import random

    >>> name = random.choice(names)
    >>> name
