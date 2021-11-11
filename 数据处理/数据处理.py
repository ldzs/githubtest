import pandas as pd
import math
#df = pd.DataFrame(columns=['index', 'PCIE_ns', 'PCIE_date','PCIE_time','m_ms','m_date','m_time'])
df = pd.read_fwf('./head100w_11050229_1')
df.columns = ['index', 'PCIE_ns','PCIE_date','PCIE_time','m_ms','m_date','m_time']
print(df.head())
#print(df.index)
#print(df.columns)
#print(df.describe())

dfres=pd.DataFrame(columns=['结果'])
dfres['结果']=df.apply(lambda x: (x['PCIE_ns']*10**3-x['m_ms'])*10**3,axis=1)
#print(dfres.head())
#print(dfres.index)
#print(dfres.describe())

bin_min=math.floor(dfres['结果'].min())
bin_max=math.ceil(dfres['结果'].max())

bins=range(bin_min, bin_max+1 ,1)

cuts=pd.cut(dfres['结果'],bins,right=False)
#print(cuts)
counts = pd.value_counts(cuts).sort_index()
print(counts)

