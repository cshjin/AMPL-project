var Xbeef >= 0; 
var Xchk >= 0; 
var Xfish >= 0;
var Xham >= 0; 
var Xmch >= 0; 
var Xmtl >= 0;
var Xspg >= 0; 
var Xtur >= 0;

minimize cost:
	3.19*Xbeef + 2.59*Xchk + 2.29*Xfish + 2.89*Xham +
	1.89*Xmch + 1.99*Xmtl + 1.99*Xspg + 2.49*Xtur;

subject to A:
	60*Xbeef + 8*Xchk + 8*Xfish + 40*Xham +
	15*Xmch + 70*Xmtl + 25*Xspg + 60*Xtur >= 700;
subject to C:
	20*Xbeef + 0*Xchk + 10*Xfish + 40*Xham +
	35*Xmch + 30*Xmtl + 50*Xspg + 20*Xtur >= 700;
subject to B1:
	10*Xbeef + 20*Xchk + 15*Xfish + 35*Xham +
	15*Xmch + 15*Xmtl + 25*Xspg + 15*Xtur >= 700;
subject to B2:
	15*Xbeef + 20*Xchk + 10*Xfish + 10*Xham +
	15*Xmch + 15*Xmtl + 15*Xspg + 10*Xtur >= 700;
