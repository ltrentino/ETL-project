#!/usr/bin/env python
# coding: utf-8

# In[30]:


# Import libraries

import requests
import pandas as pd 
import os 
import transform_functions as tf
import pycountry
from sqlalchemy import create_engine


# In[31]:


# Read csv 2019
file = "Resources\world-happiness-report-2019.csv"
df2019 = pd.read_csv(file)
df2019.head()


# In[32]:


# Read csv 2019

file2 = "Resources\world-happiness-report-2021.csv"
df2021 = pd.read_csv(file2)


# In[33]:


# Inspect csv 2021
df2021.info()


# In[34]:


# Inspect csv 2019
df2019.info()


# In[35]:


# Identify cols 2019
df2019.columns


# In[36]:


# Identify cols 2021
df2021.columns


# In[37]:


# Removing unnecessary columns 2021
clean_df2021 = df2021[['Country name','Regional indicator','Ladder score','Standard error of ladder score', 'Logged GDP per capita','Social support', 'Healthy life expectancy',
       'Freedom to make life choices', 'Generosity','Perceptions of corruption']]


# In[38]:


# Renaming columns 2021

clean_2021 = clean_df2021.rename(columns={
    "Country name": "country",
    "Regional indicator": "region",
    "Ladder score": "happiness_score_2021",
    "Standard error of ladder score" : "sd_happiness_score_2021",
    "Logged GDP per capita": "log_GDP_per_capita_2021",
    "Social support": "social_support_2021",
    "Healthy life expectancy": "healthy_life_2021",
    "Freedom to make life choices": "freedom_2021",
    "Generosity": "generosity_2021",
    "Perceptions of corruption":"corruption_2021"
})
clean_2021.head()


# In[39]:


# Count rows
clean_2021.count()


# In[40]:


# Renaming columns 2019
clean_2019 = df2019.rename(columns={
    'Country (region)': "country",
    "Ladder": "happiness_score_2019",
    'SD of Ladder' : "sd_happiness_score_2019",
    'Log of GDP\nper capita': "log_GDP_per_capita_2019",
    'Social support': "social_support_2019",
    'Healthy life\nexpectancy': "healthy_life_2019",
    "Freedom": "freedom_2019",
    "Generosity": "generosity_2019",
    "Corruption":"corruption_2019"
})
clean_2019.head()


# In[41]:


# Merging 2019 and 2021 dfs
merged_df = pd.merge(clean_2021,clean_2019, on="country", how="left")
merged_df.info()


# In[42]:


# Describe merged df
merged_df.describe()


# In[43]:


# Drop any NaN's
main_df = merged_df.dropna()
main_df.count()


# 

# In[44]:


# Check for null values
main_df.isnull().sum()


# In[45]:


# Checking duplicates
main_df.duplicated().sum()


# In[46]:


from transform_functions import convert_country_code


# In[47]:


# Add codes into our main df

main_df["code"] = convert_country_code(main_df)
main_df.head()


# In[48]:


# Filter out Unknown codes leaves us with 121 rows

main_df = main_df[main_df["code"] != "Unknown code"]


# In[49]:


# NORMALIZATION

# Create country DataFrame, setting index to new col countryID

country_df = main_df[["code","country", "region"]]

country_df['countryid'] = country_df.index

country_df.head(20)


# In[50]:


# Create measures DataFrame

measures_df = main_df[["code","freedom_2021", "generosity_2021", "corruption_2021","freedom_2019", "generosity_2019", "corruption_2019",]]
measures_df['measuresid'] = measures_df.index
measures_df.head()


# In[51]:


# Create happiness DataFrame


happiness_df = main_df[["code","happiness_score_2021","sd_happiness_score_2021","happiness_score_2019","sd_happiness_score_2019"]]

happiness_df['happinessid'] = happiness_df.index
happiness_df.head()


# In[52]:


from sqlalchemy.dialects import postgresql
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


# 

# In[53]:


from sqlalchemy.engine import URL
from sqlalchemy.dialects import postgresql
from urllib.parse import quote_plus as urlquote
connection_url = URL.create(
    drivername = "postgresql", 
    username = "postgres",
    password = "postgres",
    host = "localhost", 
    port = 5432,
    database = "world_happiness", 
)

engine = create_engine(connection_url)


# In[54]:


# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)
# reflect the tables
Base.classes.keys()


# In[55]:


session = Session(bind = engine)


# In[56]:


engine.table_names()


# In[57]:


from sqlalchemy import MetaData

metadata_obj = MetaData()
metadata_obj.reflect(bind=engine)
happiness = metadata_obj.tables["happiness"]
measures = metadata_obj.tables["measures"]
country = metadata_obj.tables["country"]


# In[58]:


# Delete tables in reverse order
engine.execute('delete from happiness')
engine.execute('delete from measures')
engine.execute('delete from country')


# In[59]:


# Upsert country
country_df.to_sql(name='country', con=engine, if_exists='append', index=False)


# In[60]:


# Upsert measures
measures_df.to_sql(name='measures', con=engine, if_exists='append', index=False)


# In[61]:


# Upsert happiness
happiness_df.to_sql(name='happiness', con=engine, if_exists='append', index=False)


# In[ ]:




