#!/usr/bin/python

from jsonschema import validate
from jsonschema.exceptions import ValidationError, SchemaError
import json
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print ('Usage:\n\t{} manifest schema'.format(sys.argv[0]))
        exit(-1)
    with open(sys.argv[1]) as json_file:
        print ('Loading: {}'.format(sys.argv[1])) 
        iiif_json = json.load(json_file)

    with open(sys.argv[2]) as schema_file:
        print ('Loading schema: {}'.format(sys.argv[2])) 
        schema = json.load(schema_file)

    try:
        validate(iiif_json, schema)
        print ('Passed Validation!')
    except ValidationError as err:
        print('Validation Failed due to:\n')
        print(err)
    except SchemaError as err:    
        print('Problem with the supplied schema:\n')
        print(err)
