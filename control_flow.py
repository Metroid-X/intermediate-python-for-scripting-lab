def test_for_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(test_for_prime(3331))

def prnt_diction(d):
    D=dict(d)
    D_i=list(D.items())
    D_k=list(D.keys())
    D_v=list(D.values())
    Space='    '
    


    for i in range(len(D_i)):
        item = f'item {i}:'

        key = f'\n{Space}Key:   {D_k[i]}'
        
        value = f'\n{Space}Value: {D_v[i]}'
        
        print(f'{item}{key}{value}')

prnt_diction({'d': 4, 'x': 24})

def count_to_n(n):
    n_=1
    while(n_ <= n):
        print(n_)
        n_+=1

count_to_n(9)