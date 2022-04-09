# import pandas as pd 

# result = []
# data_dict = {'serial no.' : [1],
#                  'Product Description' : [1],
#                  'type' : [3],
#                  'Identifier' : [4],
#                  'Service Type' : [5,5],
#                  'Start Date' : [6,7],
#                  'End Date' : [8,8],
#                  'Status' : [8,9]
#         }
# result = []
# data_dict2 = {'serial no.' : '',
#                  'Product Description' : '',
#                  'type' : '',
#                  'Identifier' : [4],
#                  'Service Type' : [5,5],
#                  'Start Date' : [6,7],
#                  'End Date' : [8,8],
#                  'Status' : [8,9]
#         }

# result.append(data_dict)
# result.append(data_dict2)

# df = pd.DataFrame(result)
# print(df)
dictt = {}
for i in range(1,62):
    dictt[i] = str(i)

print(dictt)
