acl = {'write': 'W', 'read': 'R', 'execute': 'X'}
files = {k: v for _ in range(int(input())) for k, *v in [input().split()]}
[print('OK' if acl[a] in files[f] else 'Access denied') for _ in range(int(input())) for a, f in [input().split()]]
