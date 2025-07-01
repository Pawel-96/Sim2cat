#**********Sim2cat parameter file**********#

models=['*'] #models in Data (if ==['*'], then reading entire Data/ dir)

Om_M=[0.3175] #Omega_M (if single value -> the same for every model)
Om_k=[0.] #Omega_k (if single value -> the same for every model)
Om_b=[0.049] #Omega_b (not unavoidable, but may be necessary for other parameters/filenames)
Om_L=[1.-Om_M[0]-Om_b[0]] #Omega_L (if single value -> the same for every model)

h=[0.6711] #h parameter for models (if single value -> the same for every model)
boxsize=500. #box size in Mpc/h (assumed the same for all models)

nreals=5 #number of realizations (can be also =1)
nparts=64 #number of parts of one file (can be also =1)

snapshots=['0p000','0p100'] #available snapshots numbers
zz=[0.,0.1] #redshifts corresponding with available snapshots

pos_units_Mpch=1e-3 #position units in Mpc/h (if simulation provides kpc/h, set this to 1e-3)

ignore_noexist=0 #ignoring not existing files? 0->no, raise error, 1->yes, continue
data_format='gadget' #input data format; available: hdf5,gadget,ascii

#*****relevant only if data_format=='hdf5' or format=='gadget'*****
coords_dset='pos' #dataset with coords
vels_dset='vel' #dataset with velocities

#*****relevant only if data_format=='ascii'*****
cols_r=[0,1,2] #position columns
cols_v=[3,4,5] #velocity columns



ttype=['BOX','RSD'] #output types: one item, e.g. ['BOX'] -> creating only real-space catalogs, 2 items, e.g. ['BOX','RSD'] -> creating real and z-space catalogs
output_precision='%1.4f' #precision for catalog data
output_format='ascii' #output data format: ascii/hdf5


#simulation file name
def Fname_in(nmodel,nreal,snap,part):
   return 'Data/'+models[nmodel]+'/'+str(nreal)+'/snap_00'+str(snap)+'.'+str(part)+'.txt'


#output catalog file name
def Fname_out(nmodel,nreal,snap,vtype):
    return 'Catalogs/'+vtype+'_'+models[nmodel]+'_box'+str(nreal)+'_out'+str(snap)+'.txt'