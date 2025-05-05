#! /usr/bin/python3
import numpy as np
import h5py
import hdf5plugin
import sys
import os.path

import param

if len(param.models)==1 and param.models[0]=='*': #reading entire Data/ directory
    param.models=[f for f in os.listdir('Data/') if f!='.gitignore']

nsnaps=len(param.snapshots) #number of snapshots
nmodels=len(param.models)
ntypes=len(param.ttype)


if nmodels==0:
    sys.exit('Data directory is empty, ending:/')


hval=np.array(param.h) #h parameter(s)
if len(param.h)==1: #all models with the same Hubble param
        hval=param.h[0]*np.ones(nmodels)
elif len(param.h)!=nmodels: #wrongly inserted
        sys.exit('Error: Hubble parameter must be either {len(models)}- sized array,\
        or one-sized (->same h for all models)')


def H(z,H0,OmM,Omk,OmL):
    return H0*(OmM*(1.+z)**3 + Omk*(1.+z)**2 +OmL)**.5



def Set_H():
    Hubble=np.zeros((nmodels,nsnaps)) #Hubble factor at all snapshots km/s/Mpc
    OmMval=np.array(param.Om_M)
    Omkval=np.array(param.Om_k)
    OmLval=np.array(param.Om_L)
    
    if len(param.Om_M)==1: #all models with the same Om_M
        OmMval=param.Om_M[0]*np.ones(nmodels)
    if len(param.Om_k)==1: #all models with the same Om_k
        Omkval=param.Om_k[0]*np.ones(nmodels)
    if len(param.Om_L)==1: #all models with the same Om_L
        OmLval=param.Om_L[0]*np.ones(nmodels)
        
    for i in range(0,nmodels):
        Hubble[i,:]=H(np.array(param.zz),100.*hval[i],OmMval[i],Omkval[i],OmLval[i])
    
    return Hubble







def Periodic_boundary(arr):
    for i in range(0,len(arr)):
        if arr[i]<0: arr[i]+=boxsize
        if arr[i]>=boxsize: arr[i]-=boxsize
    return arr







def Dset2numpy(dset): #reading hdf5 dataset into numpy array
    arr=np.zeros(np.shape(dset))
    dset.read_direct(arr)
    return arr



#-----------------------------------------------------------------------------------------------------------------------------
if ntypes!=1 and ntypes!=2:
    sys.exit('Size of ttype should be either 1 (e.g. \'BOX\') or 2(e.g. \'BOX\',\'RSD\')')

Hubble=Set_H() #setting array of Hubble param for models and snapshots
fout_RSDx,fout_RSDy,fout_RSDz=['','','']
err=0

for i in range(0,nmodels):
    if err==1: break
    for j in range(0,param.nreals):
        if err==1: break
        for k in range(0,nsnaps):
            if err==1: break
            for l in range(0,param.nparts): #will merge all parts
                
                fname=param.Fname_in(i,j,param.snapshots[k],l)
                if os.path.isfile(fname)!=True:
                    print(f'File: {fname} doesn\'t exist, ignoring?: {param.ignore_noexist}')
                    if param.ignore_noexist==0:
                        err=1
                        break
                
                print(f'Creating catalog(s) from {fname}')
                
                r,v=np.zeros(0),np.zeros(0)
                
                if param.data_format=='hdf5':
                    f=h5py.File(fname,'r')
                    r=Dset2numpy(f[param.parttype][param.coords_flag])
                    v=Dset2numpy(f[param.parttype][param.vels_flag])
                    if np.shape(r)[0]==3: #data in hdf5 file is tranpsosed
                        r=r.transpose()
                        v=v.transpose()
                elif data_format=='ascii':
                    r=np.genfromtxt(fname,usecols=(param.cols_r[0],param.cols_r[1],param.cols_r[2]),unpack=True).transpose()
                    v=np.genfromtxt(fname,usecols=(param.cols_v[0],param.cols_v[1],param.cols_v[2]),unpack=True).transpose()
                else:
                    err=1
                    print('incorrect parameter: [data_format] :(')
                    break
                
                if pos_units_Mpch!=1: #change units to [Mpc/h]
                    r*=pos_units_Mpch
                
                #output file for real space
                fout_BOX=open(param.Fname_out(i,j+1,param.snapshots[k],param.ttype[0]),'a')
                np.savetxt(fout_BOX, r, fmt=param.output_precision) #saving real space data
                fout_BOX.close()
                
                if ntypes==2: #making RSD catalogs
                #output files for RSD
                    fout_RSDx=open(param.Fname_out(i,j+1,param.snapshots[k],param.ttype[1]),'a')
                    fout_RSDy=open(param.Fname_out(i,j+1+param.nreals,param.snapshots[k],param.ttype[1]),'a')
                    fout_RSDz=open(param.Fname_out(i,j+1+2*param.nreals,param.snapshots[k],param.ttype[1]),'a')
                    
                    x,y,z=r[:,0],r[:,1],r[:,2]
                    x_rsd=Periodic_boundary(x+ hval[i]*v[:,0]*(1.+param.zz[k])/Hubble[i,k]) #still Mpc/h units!
                    y_rsd=Periodic_boundary(y+ hval[i]*v[:,1]*(1.+param.zz[k])/Hubble[i,k]) #still Mpc/h units!
                    z_rsd=Periodic_boundary(z+ hval[i]*v[:,2]*(1.+param.zz[k])/Hubble[i,k]) #still Mpc/h units!
                    
                    #saving z-space data:
                    np.savetxt(fout_RSDx,np.transpose((x_rsd,y,z)), fmt=param.output_precision)
                    np.savetxt(fout_RSDy,np.transpose((y_rsd,x,z)), fmt=param.output_precision)
                    np.savetxt(fout_RSDz,np.transpose((z_rsd,y,x)), fmt=param.output_precision)
                    
                    fout_RSDx.close()
                    fout_RSDy.close()
                    fout_RSDz.close()

if err==1: print('Error occurred, check input data')
print('Done, have a great day :)')
