# Code snippets
# pd.isnull(data)
# np.where(pd.isnull(data))
# sns.set(style="ticks", palette="pastel")
# df['new column name'] = df['df column_name'].apply(lambda x: 'value if condition is met' if x condition else 'value if condition is not met'
# datab.rename(columns = {'Time_ms':'Generator_ms'}, inplace= True)

# Code snippet
# df[['actuator_fdbk_sense', 'engine_rpm']] = df[['actuator_fdbk_sense', 'engine_rpm']].shift(2)
# Code snippet
# data.engine_rpm[(data.engine_rpm<2010)&(data.engine_rpm>1990)]
# Code snippet
# Remove a column I sue drop method in following context
# data_b.drop(columns= ['value'], inplace= True)
# data_b['freq'] = data_b.freq.notnull()
# data_b[data_b.freq.notnull()]
# Snippets
# df.loc[selection criteria, columns I want] = value
# df.loc[df['a'] == 0, 'b'] = np.nan
# Switch data in coulumns
# df['b'] = np.where(df.a.values == 0, np.nan, df.b.values)
# df.drop_duplicates(['col_1','col_2'])
# drop_duplicates(subset=None, keep ='first', inplace = False)
# plt.style.available
###### Shift values
# df = data[['actuator_fdbk_sense', 'engine_rpm', 'act_tool_id']]
# df = shift_values(df,['actuator_fdbk_sense', 'engine_rpm'], 2 )
# df.head(7)
#### Renaming
# data.rename(columns = {'Time_ms':'Act_ms'}, inplace= True)
