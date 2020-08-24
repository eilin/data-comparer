# CSV Comparer

Lets you compare two sets of data A and B, and will output the differences (data not in A, data not in B) into new text files.

Params are configured in the 'a_params' and 'b_params' dictionaries.
'data_name': this is just a label used for the output file
'filename': name of the CSV file
'key_idx': index in the CSV line to use as your data's key
'val_idx': optional, just a value for the datasets dictionary
'is_compound_key': specify as True if you need to build a unique key out of multiple parts in the CSV line
'ckey_indexes': required if is_compound_key is True. An array of the indexes you want use to build the dictionary key (examples: [0, 1], [5, 2], etc)

You can ignore the header line (and any other line) of your CSV file by starting the line with a #

