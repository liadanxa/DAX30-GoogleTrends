from pytrends.request import TrendReq
import pandas as pd
import numpy as np
import os

pytrends_gen = TrendReq(hl='de', tz=360)
pytrends_ai = TrendReq(hl='de', tz=360)

ABSOLUTE_PATH = os.path.dirname(os.path.abspath('Extracted_data'))

keywords = pd.read_excel('keywords.xlsx', header=0, engine='openpyxl')
header = [col for col in keywords.columns if not "Unnamed" in col]
for column_ai in header:
    file_gen = column_ai+'_gen.xlsx'
    file_ai = column_ai+'_ai.xlsx'
    words = [row for row in keywords[column_ai] if str(row) != 'nan']
    counted = False
    for keyword in words:
        print(keyword)
        pytrends_gen.build_payload([keyword], cat=0, timeframe='2010-01-01 2020-12-31') #  cat = Category Codes:   0 -> All  ,  1227 -> Computer Science  ,  1299 -> Machine Learning & Artificial Intelligence
        pytrends_ai.build_payload([keyword], cat=1299, timeframe='2010-01-01 2020-12-31') 
        if counted == False:
            df_gen = pd.DataFrame()
            df_gen = pytrends_gen.interest_over_time()
            if not df_gen.empty:
                df_gen = df_gen.drop(labels=['isPartial'], axis='columns')
            df_ai = pd.DataFrame()
            df_ai = pytrends_ai.interest_over_time()
            if not df_ai.empty:
                df_ai = df_ai.drop(labels=['isPartial'], axis='columns')
            counted = True
        else:
            try:
                column_gen = pd.DataFrame()
                column_gen = pytrends_gen.interest_over_time().drop(columns='isPartial')
                if not column_gen.empty:
                    column_gen = column_gen.drop(labels=['isPartial'], axis='columns')
                else:
                    data_gen = column_gen[keyword]
                    df_gen = df_gen.join(data_gen)
            except:
                df_gen[keyword] = np.nan
                pass
            try:
                column_ai = pd.DataFrame()
                column_ai = pytrends_ai.interest_over_time()
                if not column_ai.empty:
                    column_ai = column_ai.drop(labels=['isPartial'], axis='columns')
                else:
                    data_ai = column_ai[keyword]
                    df_ai = df_ai.join(data_ai)
            except:
                df_ai[keyword] = np.nan
                pass
    df_gen.to_excel(r"Extracted_data/cat_general/"+file_gen, index = True)        
    df_ai.to_excel(r"Extracted_data/cat_ai/"+file_ai, index = True)