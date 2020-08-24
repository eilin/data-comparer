a_params = {
  'data_name': 'test_a',
  'filename': 'test_a.csv',
  'key_idx': 0,
  'val_idx': 1,
  'is_compound_key': False,
  'ckey_indexes': [0, 1]
}

b_params = {
  'data_name': 'test_b',
  'filename': 'test_b.csv',
  'key_idx': 0,
  'val_idx': 1,
  'is_compound_key': False,
  'ckey_indexes': [0, 1]
}

def build_dict(data_params):
  data_dict = {}
  with open(data_params['filename'], 'r') as f:
    for line in f:
      if '' == line or line[0] == '#':
        continue
      key = build_dataset_key(data_params, line)
      data_dict[key] = line.split(',')[data_params['val_idx']]
  return data_dict

def build_dataset_key(data_params, line):
  key = None
  if data_params['is_compound_key']:
    key = ''
    for i in data_params['ckey_indexes']:
      key = key + line.split(',')[i] + ','
  else:
    key = line.split(',')[data_params['key_idx']]
  return key.replace('\n', '')

def check_data(d1, d2, d2_name):
  with open('not_in_'+d2_name+'.txt', 'w') as out_f:
    for key in d1:
      if key not in d2:
        out_f.write(key + '\n')

def run(a_params, b_params):
  a_dict = build_dict(a_params)
  b_dict = build_dict(b_params)
  check_data(a_dict, b_dict, b_params['data_name'])
  check_data(b_dict, a_dict, a_params['data_name'])

run(a_params, b_params)