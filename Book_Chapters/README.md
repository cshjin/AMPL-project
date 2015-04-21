In each subfolder, each (mostly) model has three files: 

__*.mod__: for describing model  
__*.dat__: for assigning data  
__*.run__: for excuting programming

Example:  
`ampl prod0.run`  

will give you 
```
MINOS 5.51: optimal solution found.  
2 iterations, objective 192000  
XB = 6000  
XC = 1400  
```

Tips:  
If you have sublime package "AMPL language" installed in your sublime text environment, you could direct use `Ctrl + b` 
in any of its related file to excute *.run file.

Notes:
* please have the AMPL and solver application ready in your PATH environment for Linux, Win and MacOS;
* In this book chapters, two solver are frequently used, MINOS and CPLEX. You can get the trial version from AMPL website.
