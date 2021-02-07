from elasticsearch import Elasticsearch


class Index:

  def __init__(self, host, cloud_id, login, password, api_key, posts):
    self.df = posts
    self.es = Elasticsearch(host, cloud_id=cloud_id, 
                            http_auth = (login, password),
                            api_key=api_key,
                            )
    
  def add_data(self, posts=None):
    """
    Adds data from .csv database to the Index 
    :posts: pd.DataFrame formed from .csv database
    """
    if posts is None:
      posts = self.df
    for idx, row in posts.iterrows():
      doc = {
          'iD': idx,
          'text': row.text,
      }
      self.es.index(index="test-index", id=idx, body=doc)

  def delete_by_id(self, idx):
    """
    Deletes element from DataBase and Index by index (initial index in posts.csv)
    :idx: index of element to delete
    """
    index = self.df[self.df['idx'] == idx].index[0]
    self.df = self.df.drop(index=index, axis=1)
    self.es.delete(index="test-index", id=idx) 

  def get_id(self, idx):
    """
    Show element in Index by id
    :idx: Index of element to show
    :return: element in Index
    """
    return self.es.get(index='test-index', id=idx)

  def search(self, text):
    """
    Search a query in the database
    :text: text of the query to search
    :return: 20 most relevant documents
    """
    res = self.es.search(
        index="test-index", 
        body={"query": { "match": {"text": text}}},
        size=20 
        )
    res = [i['_source']['iD'] for i in res['hits']['hits']]
    res = self.df.iloc[res].sort_values(by='created_date', ascending=False)
    return res.values.tolist()
