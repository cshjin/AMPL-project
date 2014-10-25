## this is a model file

# declaration of set, parameters, variables, problem and constraints.
model;

# define sets of generators and demanders
set Generator;
set Demander;

# define the set of scenarios, fixed to 3^3 in this example
set Scenarios := {1..27};

# declare the parameter of f_{ij}
param COST {g in Generator, d in Demander};

# declare the parameter of c_i
param INSTALLATION_COST {g in Generator};

# declare the probability of scenarios P(s)
param SCENARIOS_PROB {s in Scenarios};

# declare the demand
param DEMAND{s in Scenarios, d in Demander};

# for stage 1, capacity installed in generators 1 & 2;
var x {g in Generator} >= 0, suffix stage 1;

# for stage 2, capacity transfered from genertors g 
#                    to demander d at scenario s;
var y {g in Generator, d in Demander, s in Scenarios} >= 0, suffix stage 2;

# for stage 2, if necessary, transfer subcounter to demander d; 
var z {d in Demander, s in Scenarios} >= 0, suffix stage 2; 

# define the objective, sum both stages cost.
minimize total_cost :
	sum {g in Generator} x[g] * INSTALLATION_COST[g] + 
	sum {g in Generator, d in Demander, s in Scenarios}  
		SCENARIOS_PROB[s]*(y[g, d, s]* COST[g, d] + z[d, s]*6000);

# constraint of total capacity
s.t. total_capacity : 
	sum {g in Generator} x[g] <=10000;

# constraint of suppling from generators must larger than it distributed to demander
s.t. supply_constraint {g in Generator, s in Scenarios}: 
	sum {d in Demander} y[g, d, s] <= x[g];

# for each demander, either from generator or subcontract must meet the requirement
s.t. demand_constraint {d in Demander, s in Scenarios}:
	sum {g in Generator} y[g, d, s] + z[d, s]>= DEMAND[s, d];