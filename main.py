import os
import json
import argparse
from elasticsearch.elasticsearch import ElasticsearchSink

generated_file_location = "generated"

def main():
    parser = argparse.ArgumentParser(
        description="Generate and save data for supported data sinks")
    parser.add_argument("--sink", required=True,
                        help="Type of data sink (e.g., elasticsearch)")
    parser.add_argument("--records", type=int, default=50,
                        help="Number of records to generate")
    args = parser.parse_args()
    run(args)

def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def run(args):
    if args.sink == 'elasticsearch':
        sink = ElasticsearchSink()
        data = sink.generate(args.records)
        file_path = os.path.join(generated_file_location, sink.sink_name() + '.json')
        save_to_json(data, file_path)
    else:
        print(f"Unsupported sink type: {args.sink}")
        return


if __name__ == "__main__":
    main()
