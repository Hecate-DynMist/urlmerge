
# coding: utf-8

import pandas as pd
daily = pd.read_csv('dailies.csv')
da = daily[['title','content','url']]

egin = pd.read_csv('eigen.csv',delimiter=None)

# categories distribution
egin['c']=egin.Source.map(lambda x:x.split(',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,')[0][-1])
egin.groupby(['c']).count()


# extract clean, prettify content from egin tables.
ei = egin.Source.map(lambda x:x.split('doc_vec')[0])
ei = pd.DataFrame(ei)

ei['Source'] = ei['Source'].map(lambda x:x[9:])
ei = ei.drop_duplicates()
ei = ei[~ei.Source.str.startswith('{\'""desc')]

ei['url'] = ei.Source.map(lambda x:x.split('""prob')[0][15:-6])
ei['content'] = ei.Source.map(lambda x:x.split('""content')[1])
ei['content'] = ei.content.map(lambda x:x.split('""pubdate')[0])

ei.drop('Source',1,inplace=True)
ei = ei.drop_duplicates(subset=['url'])
ei['content'] = ei.content.map(lambda x:x[8:-10])



# merge two tables on key url
daei = pd.merge(da,ei,on='url',how='left')
daeii = daei[daei.astype(str)['content_y']!='nan']
daeii.to_excel('matched.xlsx')

