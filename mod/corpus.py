from google.cloud import bigquery
import pandas as pd
import datetime as dt

class corpus():

    def __init__(self, min_date, max_date=None):
        super(corpus, self).__init__()

        today = dt.datetime.today().date().isoformat()
        if max_date:
            today = max_date

        self.Q = """
        select * FROM `stylust-oasis.wizard_data_lake_db.messages`
        where createdAt >= '{}' and createdAt <= '{}'
        """.format(min_date, today)

        self.df = self.query(Q=self.Q)

    def query(self, Q, client='stylust-oasis'):
        client = bigquery.Client(project=client)
        return client.query(query=Q).result().to_dataframe()

    def __call__(self):
        return self.df