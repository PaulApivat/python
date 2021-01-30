# coding: utf-8
dct = dict()
type(dct)
dct = {
  "data": {
    "counts": [
      {
        "id": "all",
        "orderEstate": 20658,
        "orderParcel": 45615,
        "orderTotal": 99787
      }
    ],
    "orders": [
      {
        "category": "estate",
        "id": "0x000086e4043e284a30fb427c7822801280ce5650c718be93eeac826944bdc243",
        "nft": {
          "id": "estate-0x959e104e1a4db6317fa58f8295f586e1a978c297-578"
        },
        "nftAddress": "0x959e104e1a4db6317fa58f8295f586e1a978c297"
      },
      {
        "category": "estate",
        "id": "0x0000fc76f049d9f01b66fc4422fd4fcb88786946e3eba8dbc9576e486ca90505",
        "nft": {
          "id": "estate-0x959e104e1a4db6317fa58f8295f586e1a978c297-640"
        },
        "nftAddress": "0x959e104e1a4db6317fa58f8295f586e1a978c297"
      },
      {
        "category": "parcel",
        "id": "0x000102bd9e56dca2c01de721c32886c851f96e4881e8a8eccad4e20796644ec8",
        "nft": {
          "id": "parcel-0xf87e31492faf9a91b02ee0deaad50d51d56d5d4d-115792089237316195423570985008687907847825466794905548624043590289004838256681"
        },
        "nftAddress": "0xf87e31492faf9a91b02ee0deaad50d51d56d5d4d"
      },
      {
        "category": "wearable",
        "id": "0x0001db119d76b5477ab6ca6e34fdac4e2b2e006f60be63223bfc0604248a4a9b",
        "nft": {
          "id": "wearable-0xd35147be6401dcb20811f2104c33de8e97ed6818-25058"
        },
        "nftAddress": "0xd35147be6401dcb20811f2104c33de8e97ed6818"
      },
      {
        "category": "parcel",
        "id": "0x00027dbfb5ba4aadc9b53279aa4f223b3bcf4ddbea9b006088af3a88e8db9f32",
        "nft": {
          "id": "parcel-0xf87e31492faf9a91b02ee0deaad50d51d56d5d4d-50361790304298892592579441899901695295430"
        },
        "nftAddress": "0xf87e31492faf9a91b02ee0deaad50d51d56d5d4d"
      }
    ]
  }
}
dct
for x,y in dct.items():
    print(x,y)
    
dct['data']
dct['data']['counts']
dct['data']['orders']
for x,y in dct['data']['orders']:
    print(x,y)
    
for x,y in enumerate(dct['data']['orders']):
    print(x,y)
    
type(dct['data']['orders'])
dct2 = dct['data']['orders']
for x,y in enumerate(dct2):
    for i,j in y.items():
        if i == 'category':
            print(j)
            
lst = []
for x,y in enumerate(dct2):
    for i,j in y.items():
        if i == 'nftAddress':
            lst.append((i,j))
            
          
lst
col = ['nft', 'address']
import pandas as pd
df = pd.DataFrame(lst, columns=col)
print(df)
df.count()
df.count(axis='columns')
df.set_index(['address']).count(level='address')
df.groupby('address', sort=False)
df
df['address']
df['address'].groupby('address').agg('nft')
df.groupby(['address']).cumcount()
df
df.groupby(['address']).cumcount()+ 1
lst
df
for (columnName, columnData) in df.iteritems():
    print('Column Name : ', columnName)
    print('Column Contents : ', columnData.values)
    
df['address']
type(df['address'])
for i in df['address']:
    print(i)
    
for (columnName, columnData) in df.iteritems():
    lst2 = columnData.values
    print(lst2)
    
lst
lst2
counts = dict()
for address in lst2:
    counts[address] = counts.get(address, 0) + 1
    
print(counts)
