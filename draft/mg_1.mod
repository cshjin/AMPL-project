model;

set Directions;

param InitBattery;
param Demand;
param Resources;
param BatteryCapacity;
param TransitionPrice;
param ReservePrice;
param SellingPrice;
param BuyingPrice;

var amount{d in Directions} >=0;

minimize cost:
	TransitionPrice * (amount['BC']+amount['BG']
		+amount['GB']+amount['RB']) +
	ReservePrice * (InitBattery-amount['BC'] - amount['BG']
		+amount['GB']+amount['RB']) +
	BuyingPrice * (amount['GB'] + amount['GC']) -
	SellingPrice * (amount['BG'] + amount['RG']);

s.t. meetDemand:
	amount['BC'] + amount['GC'] + amount['RC'] 
		>= Demand;
s.t. batteryLimit:
	0 <= InitBattery-amount['BC'] - amount['BG']
		+amount['GB']+amount['RB'] <= BatteryCapacity;
s.t. resourcesLimit:
	amount['RB'] + amount['RC'] + amount['RG'] <=Resources;
data;

set Directions:= BC BG GB GC RB RC RG;

param InitBattery := 50;
param Demand := 250;
param Resources := 400;
param BatteryCapacity := 100;
param TransitionPrice := 0.002;
param ReservePrice := 0.001;
param SellingPrice := 0.0408;
param BuyingPrice :=0.051;