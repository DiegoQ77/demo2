import json


def write_txt_file(data, output_path):
    with open(output_path, 'w') as file:
        file.write(json.dumps(data))
    result_dict = dict({'statusCode': 'ok', 'body': None})
    return result_dict
