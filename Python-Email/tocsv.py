# import pandas as pd
# import numpy as np
# import csv
# import os
# from imap_tools import MailBox, MailMessage



# # MailData = pd.DataFrame(columns=['Sender','Receiver','CarbonCopy','Subject','Date','Body','isSpam'])
# with open("MailData.csv", "w", newline='', encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['index','Sender','Receiver','CarbonCopy','Subject','Date','Body','isSpam'])

#     with open('D:/360yundata/trec07p/full/index', 'r') as f:
#         for line in f:
#             str_list = line.split(' ')
#             print(str_list)

#             # Set Junk mail is 0
#             if str_list[0] == 'spam':
#                 label = '0'
#             # Set normal mail is 1
#             elif str_list[0] == 'ham':
#                 label = '1'

#             index = os.path.split(str_list[1].split("\n")[0])[1]
#             with open('D:/360yundata/trec07p/data/' + index, 'rb') as f:
#                 msg = MailMessage.from_bytes(f.read())
#                 writer.writerow([index, msg.from_, msg.to, msg.cc, msg.subject,
#                                  msg.date, msg.text, label])
#             # print(index)

# %matplotlib inline

import numpy as np
import warnings
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')
np.random.seed(123)

from autogluon.core.utils.loaders import load_pd
train_data = load_pd.load('https://autogluon-text.s3-accelerate.amazonaws.com/glue/sst/train.parquet')
test_data = load_pd.load('https://autogluon-text.s3-accelerate.amazonaws.com/glue/sst/dev.parquet')
subsample_size = 1000  # subsample data for faster demo, try setting this to larger values
train_data = train_data.sample(n=subsample_size, random_state=0)
print(train_data.head(10))
