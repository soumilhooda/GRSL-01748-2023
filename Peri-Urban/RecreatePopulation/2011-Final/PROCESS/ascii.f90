integer, parameter :: nx=1001,ny=1001
real, parameter    :: reso=0.005,slat=15.0025,slon=77.0025
real(kind=4)  :: var11(nx,ny),var22(nx,ny),var33(nx,ny),var44(nx,ny),var55(nx,ny),var66(nx,ny)
real(kind=4)  :: alat(ny),alon(nx)
open(11,file='light2011.bin',access='direct',recl=nx*ny)
open(22,file='pop2011.bin',access='direct',recl=nx*ny)
!open(33,file='ndvi2013.bin',access='direct',recl=nx*ny)
!open(44,file='ndvi2020.bin',access='direct',recl=nx*ny)
!open(55,file='lulc2013.bin',access='direct',recl=nx*ny)
!open(66,file='lulc2020.bin',access='direct',recl=nx*ny)
read(11,rec=1)var11
read(22,rec=1)var22
!read(33,rec=1)var33
!read(44,rec=1)var44
!read(55,rec=1)var55
!read(66,rec=1)var66

do jj=1,nx
  alon(jj)=slon+(jj-1)*reso
enddo
do jj=1,ny
  alat(jj)=slat+(jj-1)*reso
enddo

do jj=1,nx
    do kk=1,ny
            if(var11(jj,kk) >= 0 .and. var22(jj,kk)  >= 0)then
!           if(var33(jj,kk) >= -1 .and. var44(jj,kk) >= -11)then
!           if(var55(jj,kk) >= 1 .and. var66(jj,kk)  >=  1)then
                 write(998,'(11(f12.4,2x))')alat(kk),alon(jj),var11(jj,kk),var22(jj,kk) !,var11(jj,kk)-var22(jj,kk), & 
                                                             !var33(jj,kk),var44(jj,kk),var33(jj,kk)-var44(jj,kk), &
                                                             !var55(jj,kk),var66(jj,kk),var55(jj,kk)-var66(jj,kk)
             endif
!             endif
!             endif
    enddo
enddo
stop
end
