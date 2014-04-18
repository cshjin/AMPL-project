/* 
 * The original example is from https://github.com/ampl/ampl/blob/master/solvers/smpswriter/farmer.ampl
 */
 
# The deterministic equivalent of the farmer's problem from "Introduction to Stochastic Programming" by John R. Birge and Francois Louveaux.

set Crops;

set Scenarios;
param P{Scenarios}; # probabilities

param TotalArea;               # acre
param Yield{Crops, Scenarios}; # T/acreb
param PlantingCost{Crops};     # $/acre
param SellingPrice{Crops};     # $/T
param ExcessSellingPrice;      # $/T
param PurchasePrice{Crops};    # $/T
param MinRequirement{Crops};   # T
param BeetsQuota;              # T

# Area in acres devoted to crop c
var area{c in Crops} >= 0, suffix stage 1;

# Tons of crop c sold (at favourable price) under scenario s
var sell{c in Crops, s in Scenarios} >= 0, suffix stage 2;

# Tons of sugar beets sold in excess of the quota under
# scenario s
# var sellExcess{s in Scenarios} >= 0, suffix stage 2;
var sellExcess{s in Scenarios} >= 0, suffix stage 2;
# Tons of crop c bought under scenario s
var buy{c in Crops, s in Scenarios} >= 0, suffix stage 2;

maximize profit: 
    sum{s in Scenarios} P[s] * (
    ExcessSellingPrice * sellExcess[s] +
    sum{c in Crops} (SellingPrice[c] * sell[c, s] -
                     PurchasePrice[c] * buy[c, s]) -
    sum{c in Crops} PlantingCost[c] * area[c]);

s.t. totalArea: sum {c in Crops} area[c] <= TotalArea;

s.t. requirement{c in Crops, s in Scenarios}:
    Yield[c, s] * area[c] - sell[c, s] + buy[c, s]
        >= MinRequirement[c];

s.t. quota{s in Scenarios}: sell['beets', s] <= BeetsQuota;

s.t. sellBeets{s in Scenarios}:
    sell['beets', s] + sellExcess[s]
        <= Yield['beets', s] * area['beets'];