def build_query_string(query_string):
    return '&'.join(sorted([f"{k}{'='}{v}" for k, v in query_string.items()]))

print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))
