import os


for en_var_key, en_var in os.environ.items():
    print('{}: {}'.format(en_var_key, en_var))


