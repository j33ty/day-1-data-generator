# Day 1 Data Generator
![DALLE2024-03-0717 49 12-GenerateanotherartisticrepresentationofaDay1DataGeneratortoolagainfeaturingthetext_Day1DataGenerator_prominently Thisversiono-ezgif com-webp-to-jpg-converter](https://github.com/j33ty/day-1-data-generator/assets/31261252/6f58145e-c9f3-458e-b797-bdcd12ddbc91)

Generates fake data for several sinks in their supported formats. It makes your day 1 of trying out a new tool slightly more productive.

Note: Currently, only Elasticsearch is supported.

## Usage
```sh
> python3 main.py --sink elasticsearch --records 1000

Generating 100 records for Elasticsearch, index name: idx-2024-03-07-17-18-28
Data written to generated/elasticsearch_7.ndjson. Import with:

curl -XPOST -H "Content-Type: application/x-ndjson" --data-binary "@generated/elasticsearch_7.ndjson" "http://localhost:9200/_bulk"
```

This will generate 1000 records and store them as actions in a file.

## Naming

Need _some_ data in the tool you're trying out? This tool can help you getting started. Ofcourse, it can be used whenever you need some fake data.

## Acknowledgement

This tool uses the [Faker](https://faker.readthedocs.io/en/master/) library to generate fake data. Great library.
