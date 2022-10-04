def build_dict_result(item):
    return {
        "serial_no": item.get('serial_no'),
        "asset_type": item.get('asset_type'),
        "hardware_standard": item.get('hardware_standard'),
        "technical_specs": item.get('technical_specs'),
        "asset_status": item.get('asset_status')
    }


def search_asset_by_status(items, asset_status=''):
    list_of_items = []
    list_of_pending = []
    if len(items) == 0:
        return []
    for item in items:
        if (item.get('asset_status')):
            list_of_items.append(item.get('asset_status'))
            if item.get('asset_status') == asset_status:
                list_of_pending.append(item.get('asset_status'))

    if (asset_status == 'Pending return'):
        return list_of_pending
    else:
        return list_of_items


def search_asset_by_technical_specs(items, search_tokens):
    # Destructuring of search tokens
    list_of_items = []
    for item in items:
        # print(item)
        technical_specs = item.get(
            'technical_specs').replace('/', '').lower().split(' ')
        token_one, token_two = search_tokens
        print(technical_specs, 'technical spects')
        if (token_one.lower() in technical_specs and token_two.lower() in technical_specs):
            list_of_items.append(build_dict_result(item))
            return list_of_items
        else:
            return list_of_items

    # search tokens in dictionary items
    # if search_tokens[0] in items[0].values():
    #     return True
    # else:
    #     return list_of_items
