import json
import utils
from datetime import datetime
from faker import Faker

fake = Faker(['en_US'])

class ElasticsearchSink():
    """
    Data sink for Elasticsearch.
    """

    def __init__(self):
        self.baseurl = "http://localhost:9200"
        self.index_name = "idx-{}".format(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

    def sink_name(self):
        return 'elasticsearch_7'

    def import_cmd(self, filepath):
        return 'curl -XPOST -H "Content-Type: application/x-ndjson" --data-binary "@{}" "{}/_bulk"'.format(filepath, self.baseurl)

    def write(self, filepath, num_records):
        print("Generating {} records for Elasticsearch, index name: {}".format(num_records, self.index_name))

        with open(filepath, 'w') as file:
            for i in range(num_records):
                record = self.generate_one()

                # Add the action metadata before each JSON object
                action_metadata = '{{"index": {{"_index" : "{}"}}}}\n'.format(self.index_name)
                file.write(action_metadata)

                # `default`` is a function applied to objects that aren't serializable.
                # In this case it's str, so it just converts everything it doesn't know to strings.
                # This is great for serialization but not so great when deserializing.
                file.write(json.dumps(record, default=str))

                # Add a newline character before each JSON object to create a valid NDJSON file.
                file.write('\n')

        print("Data written to {}. Import with:\n{}".format(filepath, self.import_cmd(filepath)))

    def generate_one(self):
        return {
            "id": utils.random_string(),
            "about": fake.text(),
            "address": fake.address(),
            "age": utils.random_int(100),
            "color": fake.color(),
            "company": fake.company(),
            "credit_card": fake.credit_card_full(),
            "currency": fake.currency(),
            "date_time": fake.date_time(),
            "details": utils.random_nested_object(),
            "emoji": fake.emoji(),
            "photo": fake.file_name(extension='jpg'),
            "geo": fake.local_latlng(),
            "isActive": utils.random_boolean(),
            "job": fake.job(),
            "lorem": fake.paragraph(nb_sentences=5),
            "name": fake.name(),
            "phone_number": fake.phone_number(),
            "profile": fake.profile(),
            "salary": utils.random_float(100000.0),
            "user_agent": fake.user_agent(),
        }
