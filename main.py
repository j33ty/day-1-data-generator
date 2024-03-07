import os
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

def run(args):
    if args.sink == 'elasticsearch':
        sink = ElasticsearchSink()
        file_path = os.path.join(generated_file_location, sink.sink_name() + '.ndjson')
        sink.write(file_path, args.records)
    else:
        print(f"Unsupported sink type: {args.sink}")
        return


if __name__ == "__main__":
    main()
