from search_system import Index
from .configs import LOGGER
import os
import pandas as pd
from flask import Flask
from flask import request, render_template


host = ['https://9a669b1781184222b80810649034afc6.eastus2.azure.elastic-cloud.com:9243']
cloud_id = 'i-o-optimized-deployment:ZWFzdHVzMi5henVyZS5lbGFzdGljLWNsb3VkLmNvbTo5MjQzJDlhNjY5YjE3ODExODQyMjJiODA4MTA2NDkwMzRhZmM2JDcxNGJmOTU5OTZiYzRhNGJiYzk5OTk5ZmZkZTZjNTVi'       
login = 'elastic'
password =  'Ok3cBcvx9Rz0wtboxPl2oO2F'
api_key='aUl4emFYY0IzLUx4dVVHTFg2LVE6ek1wdXBtM2dSaHkwOEU4OWtfVGg1UQ=='
posts = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'srcs/posts.csv'))
posts['idx'] = list(range(posts.shape[0]))


my_es = Index(host, cloud_id, login, password, api_key, posts)
app = Flask(__name__)

@app.route("/")
def home():
  return render_template('index.html')

@app.route('/result', methods=['GET'])
def get_result():
  try:
    query = request.args['sentence']
    table = my_es.search(query)
    return render_template('index.html', text=query, n=len(table), table=table)
  except Exception as e:
    LOGGER.info(f'Exception: {e}')
    return render_template('index.html', exception=1)

def start():
  app.run()
