model;

set Crops;

param TotalArea;
param Yield{Crops};
param PlantingCost{Crops};
param SellingPrice{Crops};
param ExcessSellingPrice;
param BuyingPrice{Crops};
param MinRequirement{Crops};
param BeetsQuota;

var area{c in Crops} >= 0;
var sell{c in Crops} >= 0;
var sellExcess >=0;
var buy{c in Crops} >=0;

maximize profit:
	ExcessSellingPrice * sellExcess + 
	sum{c in Crops} (SellingPrice[c] * sell[c] - 
		BuyingPrice[c] * buy[c]  - 
		PlantingCost[c] * area[c]);

subject to totalArea: 
	sum {c in Crops} area[c] <= TotalArea;

subject to requirement{c in Crops}:
	Yield[c] * area[c] - sell[c] + buy[c] 
		>=MinRequirement[c];

subject to quota: sell['beets'] <=BeetsQuota;
subject to sellBeets: sell['beets'] + sellExcess 
		<=Yield['beets'] * area['beets'];