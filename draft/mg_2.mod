model;

set Directions;
set Scenarios;
set Time;

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
param SellingPrice_stage{s in Scenarios};
param BuyingPrice_stage{s in Scenarios};

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
		BuyingPrice_stage[s] * (
			amount_stage['GB',s] 
			+ amount_stage['GC',s]) -
		SellingPrice_stage[s] * (
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
set Time := 1 2;
param P:=
	N 0.7
	A 0.2
	M 0.1;
param InitBattery:= 50;
param Demand:= 1000;
param Resources := 500;
param Resources_stage := 
	N 500
	A 250
	M 125;
param BatteryCapacity := 100;
param TransitionPrice := 0.002;
param ReservePrice := 0.001;
param SellingPrice := 0.074;
param BuyingPrice :=0.091;
param SellingPrice_stage :=
	N 0.074
	A 0.063
	M 0.047;
param BuyingPrice_stage :=
	N 0.091
	A 0.084
	M 0.057;