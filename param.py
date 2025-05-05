#**********Sim2cat parameter file**********#

models=['*'] #models in Data (if ==['*'], then reading entire Data/ dir)

Om_M=[0.3175,0.3075,0.3275] #Omega_M (if single value -> the same for every model)
Om_k=[0.] #Omega_k (if single value -> the same for every model)
Om_b=[0.049,0.049,0.049] #Omega_b (not unavoidable, but may be necessary for other parameters/filenames)
Om_L=[1.-Om_M[0]-Om_b[0],1.-Om_M[1]-Om_b[1],1.-Om_M[2]-Om_b[2]] #Omega_L (if single value -> the same for every model)

h=[0.6711] #h parameter for models (if single value -> the same for every model)
boxsize=1000. #box size in Mpc/h (assumed the same for all models)

nreals=5 #number of realizations (can be also =1)
nparts=8 #number of parts of one file (can be also =1)

snapshots=[4,3,2] #available snapshots numbers
zz=[0.,0.5,1.] #redshifts corresponding with available snapshots

pos_units_Mpch=1e-3 #position units in Mpc/h (if simulation provides kpc/h, set this to 1e-3)

ignore_noexist=0 #ignoring not existing files? 0->no, raise error, 1->yes, continue
data_format='hdf5' #input data format; available: hdf5,ascii

#*****relevant only if data_format=='hdf5'*****
parttype='PartType1' #name of first group in hdf5 data
coords_flag='Coordinates' #name of dataset with coords
vels_flag='Velocities' #name of dataset with velocities

#*****relevant only if data_format=='ascii'*****
cols_r=[0,1,2] #position columns
cols_v=[3,4,5] #velocity columns



ttype=['BOX','RSD'] #output types: one item, e.g. ['BOX'] -> creating only real-space catalogs, 2 items, e.g. ['BOX','RSD'] -> creating real and z-space catalogs
output_precision='%1.4f' #precision for catalog data



#simulation file name
def Fname_in(nmodel,nreal,snap,part):
   return 'Data/'+models[nmodel]+'/'+str(nreal)+'/snap_00'+str(snap)+'.'+str(part)+'.txt'


#output catalog file name
def Fname_out(nmodel,nreal,snap,vtype):
    return 'Catalogs/'+vtype+'_'+models[nmodel]+'_box'+str(nreal)+'_out'+str(snap)+'.txt'