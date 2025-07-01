Simple code for merging partitioned raw data from cosmological simulations and creating real and z-space catalogs.

## Requirements and running:
- numpy
- pynbody
- h5py, hdf5plugin

Running: **python3 Make_catalogs.py**


## Parameter file:
File param.py contans code settings.  

**models**  
Array containing names of directories with models, see Fname_in() function.  
If models=['\*'], code reads entire Data/ directory  
\[Attention\] Data/ should contain directories with model names that math own-defined Fname_in() format  
(see below for Fname_in() and Fname_out() descriptions).  
If Data/ contains only files and models='\*', code will not recognize them correctly.
In such situation, select models array to correspond with recognizable parts of file names in Data/. 

**Om_M**  
Array with Omega_Matter values for corresponding models.  
If one value given -> code will assume the same value for all models

**Om_k**  
Array with Omega_k values for corresponding models.  
If one value given -> code will assume the same value for all models

**Om_b**  
Array with Omega_baryon values for corresponding models.  
If one value given -> code will assume the same value for all models

**Om_L**  
Array with Omega_Lambda values for corresponding models.  
If one value given -> code will assume the same value for all models

**h**  
Array with h parameter (h=H_0/100 [km/s^-1Mpc^_1]) values for corresponding models.  
If one value given -> code will assume the same value for all models

**boxsize**  
Size of simulation box [Mpc/h], assumed to be the same for all models

**nreals**  
Number of simulation realizations

**nparts**  
Number of files into which the same output (one model, one realization) was divided

**snapshots**  
Array with numbers of available simulation snapshots

**zz**  
Array with values of redshifts corresponding with given snapshots

**pos_units_Mpch**  
Position units in Mpc/h. If data is in kpc/h, set it to 1000

**ignore_noexist**  
Flag: [0] - if some files do not exist (check Fname_in() function), raise error; [1] - ignore, code will not provide outputs for these files.
Assumed number of all files within data directory (see Fname_in() function) is: len(models) x nreals x nparts x nsnapshots

**data_format**  
Input data format: \[hdf5/gadget/ascii\]

**coords_dset**  
\[Relevant only if data_format=hdf5 or gadget\]: name of dataset containing positions

**vels_dset**  
\[Relevant only if data_format=hdf5 or gadget\]: name of dataset containing velocities (assuming units of [km/s])

**cols_r**  
\[Relevant only if data_format=ascii\]: number of columns with positions (numbering starts from 0)

**cols_v**  
\[Relevant only if data_format=ascii\]: number of columns with velocities (numbering starts from 0)


**ttype**  
Array with output data types: e.g. if ttype=\['BOX'\], code will create only real-space output, labelled with 'BOX'  
if ttype=\['BOX','RSD'\], code will create bot real and z-space output, labelled with 'BOX' and 'RSD' respectively


**output_precision**  
Precision of output, e.g. output_precision='%1.4f' 

**Fname_in() and Fname_out()**  
Functions defining naming format of input and output files, corresponding with:  
model\[nmodel\], nreal (realization), snap (snapshot number), part (part of file, see **nparts** parameter), vtype (see **ttype**)   
If something does not apply, set appriopriate number to 1 and ignore it inside Fname_in(), for examle:  
if there are no realizations distinguished in the data and everything is in one file,  
set nreals=1, nparts=1, Fname_in(): return 'Data/'+model\[nmodel\]+str(snap)   (or any other format)  
\[Attention\]: the file names returned by Fname_out() need to have dependence on nreal since this is how z-space
results along x,y,z axes are being distinguished. For catalog file of realization nreal, z-space catalog realization numbers are:  
- RSD along x axis: nreal  
- RSD along y axis: nreal+nreals  
- RSD along z axis: nreal+2\*nreals  
Z-space outputs are always rotated to have z-space effect at first column, i.e.: (x_rsd,y,z), (y_rsd,x,z), (z_rsd,y,x)


## Improvements to add:
- HDF5 outputs (now ascii/gadget/hdf5 input, but output  available only in ascii)
