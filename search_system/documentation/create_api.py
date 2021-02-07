#https://apispec.readthedocs.io/en/latest/api_core.html#apispec.APISpec.path


from apispec import APISpec
from flask.views import View

spec = APISpec(
    title="Search System",
    version="1.0.0",
    openapi_version="3.0.2",
    info=dict(description="A simple search system project"),
    url="https://github.com/AnnaZhuravleva/search_system_project/",
    description="https://github.com/AnnaZhuravleva/search_system_project/blob/main/README.txt",
    contact=dict(url="zhuravlevahanna@gmail.com"),
)

spec.components.schema(
    "Index",
    {
        "type":"object",
        "properties": {
            "df": {"type": "pandas.core.frame.DataFrame"},
            "es": {"type": "elasticsearch.client.Elasticsearch"},
        }
    },
)

spec.path(
    path="/",
    operations={"get": {
        "responses": {
            "200": {
                "description": "standard response"}}}},
    summary="Index page"
)

spec.path(
    path="/result",
    summary="Response  to a user's query",
    description="Based on the users's query, shows a table of most relevant documents from a database ",
    parameters={
        "in":"query",
        "name":"sentence",
        "description":"User's query",
        "required":True,
        "schema":{
            "type":"string"
        }
    },
    operations=dict(
        get=dict(
            responses={"200": {
                "decription": "Based on the user's response, 'search' method of class Index is called. \
                                Text query is searched in the Index database (parameter 'self.es'), and \
                                20 most relevant documents are returned with the meta stored in the\
                                database (parameter 'self.df')",
                "content":{
                    "application/json": {
                        "schema": "Index"
                        }
                    }
                }
            },
        ),
    )
)


import json
with open('docs.json', 'w', encoding='utf-8') as f:
    json.dump(spec.to_dict(), f)