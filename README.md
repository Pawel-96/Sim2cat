Simple code for merging partitioned raw data from cosmological simulations and creating real and z-space catalogs.

## Requirements and running:
- numpy
- h5py, hdf5plugin

Running: **python3 Make_catalogs.py**


## Parameter file:
File param.py contans code settings.  

**models**  
Array containing names of directories with models, see Fname_in() function.  
If models=['\*'], code reads entire Data/ directory

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
Input data format: \[hdf5/ascii\]

**parttype**  
\[Relevant only if data_format=hdf5\]: name of hdf5 group containing data for catalogs

**coords_flag**  
\[Relevant only if data_format=hdf5\]: name of hdf5 dataset containing positions

**vels_flag**  
\[Relevant only if data_format=hdf5\]: name of hdf5 dataset containing velocities (assuming units of [km/s])

**cols_r**  
\[Relevant only if data_format=ascii\]: number of columns with positions

**cols_v**  
\[Relevant only if data_format=ascii\]: number of columns with velocities


**ttype**  
Array with output data types: e.g. if ttype=\['BOX'\], code will create only real-space output, labelled with 'BOX'  
if ttype=\['BOX','RSD'\], code will create bot real and z-space output, labelled with 'BOX' and 'RSD' respectively


**output_precision**  
Precision of output, e.g. output_precision='%1.4f' 

**Fname_in() and Fname_out()**  
Functions defining naming format of input and output files, corresponding with:  
model\[nmodel\], nreal (realization), snap (snapshot number), part (part of file, see **nparts** parameter)


## Improvements to add:
- HDF5 outputs (now ascii/hdf5 input, but output only ascii)
- 
