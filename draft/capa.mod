reset;
## declaration of set, parameters, variables, problem and constraints.
model;

set Generator;
set Demander;
set Scenarios := {1..27};

param COST {g in Generator, d in Demander};
#param DEMAND {dl in DLevel, d in Demander};
#param DEMAND_PROB {dl in DLevel, d in Demander};
param INSTALLATION_COST {g in Generator};
#param RELIABILITY {gl in GLevel, g in Generator};
#param RELIABILITY_PROB {gl in GLevel, g in Generator};
param SCENARIOS_PROB {s in Scenarios};
param DEMAND{s in Scenarios, d in Demander};
# capacity installed in generators 1 & 2;


var x {g in Generator} >= 0;

# capacity transfered from genertors g to demander d;
var y {g in Generator, d in Demander, s in Scenarios} >= 0, suffix stage 2;

# if necessary, transfer subcounter to demander d; 
var z {d in Demander, s in Scenarios} >= 0, suffix stage 2;

minimize total_cost :
	sum {g in Generator} x[g] * INSTALLATION_COST[g] + 
	sum {g in Generator, d in Demander, s in Scenarios}  
		SCENARIOS_PROB[s]*(y[g, d, s]* COST[g, d] + z[d, s]*6000);

s.t. total_capacity : 
	sum {g in Generator} x[g] <= 10000;

s.t. supply_constraint {g in Generator, s in Scenarios}: 
	sum {d in Demander} y[g, d, s] <= x[g];

s.t. demand_constraint {d in Demander, s in Scenarios}:
	sum {g in Generator} y[g, d, s] + z[d, s]>= DEMAND[s, d];

## set all the data according to the variables.
data;
set Generator := g1 g2;
set Demander := d1 d2 d3;
#set GLevel := gl1 gl2 gl3;
#set DLevel := dl1 dl2 dl3;


param COST: 
		d1 	d2 	d3 :=
	g1 	4.3 2 	0.5
	g2 	7.7 3 	1;

#param DEMAND:
#		d1	d2 	d3 :=
#	dl1	900 900 900
#	dl2  1000 1000 1100
#	dl3  1300 1250 1400;

#param DEMAND_PROB:
#		d1	d2 	d3 :=
#	dl1	0.35 0.35 0.35
#	dl2  0.55 0.55 0.55
#	dl3  0.1 0.1 0.1;	

param INSTALLATION_COST :=
	g1 400
	g2 350;

#param RELIABILITY:
#			g1 	g2:=
#	gl1 	1 	1
#	gl2  	0.95 0.8
#	gl3  	0.3 0;

#param RELIABILITY_PROB:
#		g1 		g2:=
#	gl1 	0.9 	0.85
#	gl2 	0.05	0.1
#	gl3		0.05	0.05;

param SCENARIOS_PROB :=
	1	0.042875
	2	0.067375
	3	0.01225
	4	0.067375
	5	0.105875
	6	0.01925
	7	0.01225
	8	0.01925
	9	0.0035
	10	0.067375
	11	0.105875
	12	0.01925
	13	0.105875
	14	0.166375
	15	0.03025
	16	0.01925
	17	0.03025
	18	0.0055
	19	0.01225
	20	0.01925
	21	0.0035
	22	0.01925
	23	0.03025
	24	0.0055
	25	0.0035
	26	0.0055
	27	0.001;

param DEMAND:
		d1  d2  d3:=
	1	900	900	900
	2	900	900	1100
	3	900	900	1400
	4	900	1000	900
	5	900	1000	1100
	6	900	1000	1400
	7	900	1250	900
	8	900	1250	1100
	9	900	1250	1400
	10	1000	900	900
	11	1000	900	1100
	12	1000	900	1400
	13	1000	1000	900
	14	1000	1000	1100
	15	1000	1000	1400
	16	1000	1250	900
	17	1000	1250	1100
	18	1000	1250	1400
	19	1300	900		900
	20	1300	900		1100
	21	1300	900		1400
	22	1300	1000	900
	23	1300	1000	1100
	24	1300	1000	1400
	25	1300	1250	900
	26	1300	1250	1100
	27	1300	1250	1400
;