import  pandas as pd

data= pd.read_csv("data/CRDC2013_14.csv",encoding ="Latin-1")

races=["HI","AM","AS","HP","BL","WH","TR"]

data["total_enrollment"]=data["TOT_ENR_M"]+data["TOT_ENR_F"]
all_enrollment =data["total_enrollment"].sum()

totals ={}

for race in races:
	race_f ="SCH_ENR_"+race+"_F"
	race_m ="SCH_ENR_"+race+"_M"
	total_race ="total_"+race
	totals[total_race] =100*(data[race_m].sum()+data[race_f].sum())/all_enrollment

for k,v, in totals.items():
	print(k,v)
