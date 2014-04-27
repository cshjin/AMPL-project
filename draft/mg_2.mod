model;

set Directions;
set Scenarios;
param SIZE;
set Time:={1..SIZE};

param P{s in Scenarios};
param InitBattery;
param Demand;
param Resources;
param Resources_stage{s in Scenarios};
param BatteryCapacity;
param TransitionPrice;
param ReservePrice;
param SellingPrice;
param BuyingPrice;
param SellingPrice_stage;
param BuyingPrice_stage;
param WindSpeed{t in Time};

var amount{d in Directions} >=0;
var amount_stage{d in Directions, s in Scenarios} >=0, suffix stage 2;

minimize cost:
	TransitionPrice * (amount['BC']+amount['BG']
		+amount['GB']+amount['RB']) +
	ReservePrice * (InitBattery-amount['BC'] - amount['BG']
		+amount['GB']+amount['RB']) +
	BuyingPrice * (amount['GB'] + amount['GC']) -
	SellingPrice * (amount['BG'] + amount['RG']) + 
	
	sum {s in Scenarios} P[s] * (
		TransitionPrice * (
			amount_stage['BC',s]
			+amount_stage['BG',s]
			+amount_stage['GB',s]
			+amount_stage['RB',s]) +
		ReservePrice * (
			InitBattery
			-amount['BC'] 
			-amount['BG']
			+amount['GB']
			+amount['RB'] 
			-amount_stage['BC',s]
			-amount_stage['BG',s]
			+amount_stage['GB',s]
			+amount_stage['RB',s]) +
		BuyingPrice_stage * (
			amount_stage['GB',s] 
			+ amount_stage['GC',s]) -
		SellingPrice_stage * (
			amount_stage['BG',s] 
			+ amount_stage['RG',s]));

s.t. meetDemand:
	amount['BC'] + amount['GC'] + amount['RC'] 
		>= Demand;
s.t. meetDemand_stage{s in Scenarios}:
	amount_stage['BC',s]+amount_stage['GC',s]+ amount_stage['RC',s]
		>=Demand;

s.t. batteryLimit:
	0 <= InitBattery-amount['BC'] - amount['BG']
		+amount['GB']+amount['RB'] <= BatteryCapacity;
s.t. batteryLimit_stage{s in Scenarios}:
	0 <= InitBattery-amount['BC'] - amount['BG']
		+amount['GB']+amount['RB'] 
		-amount_stage['BC',s] - amount_stage['BG',s]
		+amount_stage['GB',s] + amount_stage['RB',s]
		<= BatteryCapacity;

s.t. resourcesLimit:
	amount['RB'] + amount['RC'] + amount['RG'] <=Resources;
s.t. resourcesLimit_stage{s in Scenarios}:
	amount_stage['RB',s] + amount_stage['RC',s] + amount_stage['RG',s] <=Resources_stage[s];




######################## data ########################
data;

set Directions:= BC BG GB GC RB RC RG;
set Scenarios := N A M;
param SIZE:=8759;
param P:=
	N 0.7
	A 0.2
	M 0.1;
param InitBattery:= 50;
param Demand:= 1000;
param Resources := 800;
param Resources_stage := 
	N 800
	A 400
	M 200;
param BatteryCapacity := 100;
param TransitionPrice := 0.002;
param ReservePrice := 0.001;
param SellingPrice := 0.0408;
param BuyingPrice :=0.051;
param SellingPrice_stage := 0.0408;
#	N 0.074
#	A 0.063
#	M 0.047;
param BuyingPrice_stage := 0.051;
#	N 0.091
#	A 0.084
#	M 0.057;
param WindSpeed default 0;