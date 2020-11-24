"""
This script takes the place of tdidf.pl in step 5 of change_format.pl, which itself is step 2 of preprocess.pl.
It takes as input train.clean.rmiw.ind, which has each sentence on its own line, and the words in each sentence have
been mapped to their vocab ids, and words that occur infrequently have been removed.
It generates files idf and train.clean.rmiw.ind.tf.idf
"""

from collections import defaultdict
from math import log
import re
import sys
from typing import List, Dict


def perl_rounding(n: float):
    if int(n) == 0:
        return round(n, 15)

    return round(n, 15 - len(str(int(n))))


# SECTION: Window mode stuff
use_window_mode = False
window_size = 5
# END SECTION: Window mode stuff

is_train = int(sys.argv[1])
input_file = sys.argv[2]
idf_file = sys.argv[3]
use_tf = int(sys.argv[4])
use_idf = int(sys.argv[5])
norm = int(sys.argv[6])

output_file = input_file

if use_tf:
    output_file += '.tf'

if use_idf:
    output_file += '.idf'

if norm:
    output_file += '.norm'

### 1. read data
data: List[Dict[str, int]] = []

if use_window_mode:
    tokens = []

    with open(input_file, 'r') as corpus:
        for line in corpus:
            if line.strip() == '':
                continue

            words = re.split(r'\s+', line.strip())
            tokens += words

    for i in range(len(tokens) - window_size + 1):
        words = tokens[i:i+window_size]
        hash = defaultdict(lambda: 0)

        for w in words:
            hash[w] += 1

        data.append(hash)

else:
    with open(input_file, 'r') as corpus:
        for line in corpus:
            if line.strip() == '':
                continue

            words = re.split(r'\s+', line.strip())
            hash = defaultdict(lambda: 0)

            for w in words:
                hash[w] += 1

            data.append(hash)

### 2. use tf
# If use_tf == 1, there's nothing to do for this step.
assert use_tf == 1

### 3. use idf
idf = defaultdict(lambda: 0.0)

if is_train == 1:
    for doc_hash in data:
        for term in doc_hash.keys():
            idf[term] += 1

    num_docs = len(data)

    for term in idf.keys():
        idf[term] = log(num_docs / (idf[term] + 1))

    with open(idf_file, 'w') as output:
        for term in sorted(idf.keys(), key=int):
            output.write(f'{term} {perl_rounding(idf[term])}\n')

else:
    with open(idf_file, 'r') as f:
        for line in f:
            line = re.sub(r'\s+', '', line)
            term, value = re.split(r'\s+', line)
            idf[term] = value

for doc_hash in data:
    for term in doc_hash.keys():
        if term not in idf:
            raise Exception(term + ' does not exist!')

        doc_hash[term] *= idf[term]

### 4. normalize as unit vectors
# If norm == 0, there's nothing to do for this step.
assert norm == 0

### 5. write data (features are ranked in ascending order)
with open(output_file, 'w') as output:
    for doc_hash in data:
        words = sorted(doc_hash.keys(), key=int)

        for w in words:
            output.write(f'{w} {perl_rounding(doc_hash[w])} ')

        output.write('\n')
