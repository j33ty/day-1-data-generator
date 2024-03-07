import utils

class ElasticsearchSink():
    """
    Data sink for Elasticsearch.
    """

    def sink_name(self):
        return 'elasticsearch_7'

    def sink_format(self):
        return 'json'

    def help_text(self):
        return """
            curl -XPOST -H "Content-Type: application/x-ndjson" \
                --data-binary "@bulk_data.json" \
                "localhost:9200/_bulk"
        """

    def generate(self, num_records):
        data = []
        for _ in range(num_records):
            record = {
                "id": utils.random_string(),
                "name": utils.random_string(),
                "age": utils.random_int(100),
                "salary": utils.random_float(100000.0),
                "isActive": utils.random_boolean(),
                "details": utils.random_nested_object()
            }
            data.append(record)
        return data
