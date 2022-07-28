integer, parameter :: nx=1251,ny=1251,nyr=9
real, parameter    :: reso=0.004,slat=15.002,slon=77.002
real(kind=4)  :: var1(nx,ny),var2(nx,ny),var11(nx,ny,nyr),var22(nx,ny,nyr)
real(kind=4)  :: slope1(nx,ny),slope2(nx,ny),corr(nx,ny)
real(kind=4)  :: alat(ny),alon(nx)
open(1,file='light2013-2021.grd',access='direct',recl=1*nx*ny)
open(2,file='ndvi2013-2021.grd',access='direct',recl=1*nx*ny)
open(3,file='slope-corr.grd',access='direct',recl=1*nx*ny)
open(997,file='slope-corr.ascii')
open(998,file='light2013-2021.ascii')
open(999,file='ndvi2013-2021.ascii')

read(3,rec=1)slope1
read(3,rec=2)slope2
read(3,rec=3)corr

do iyear=1,nyr
   read(1,rec=iyear)var1
   read(2,rec=iyear)var2
   var11(:,:,iyear)=var1
   var22(:,:,iyear)=var2
enddo

do jj=1,nx
  alon(jj)=slon+(jj-1)*reso
enddo
do jj=1,ny
  alat(jj)=slat+(jj-1)*reso
enddo

do jj=1,nx
    do kk=1,ny
            if(slope1(jj,kk) /= -999.0 .and. slope2(jj,kk) /= -999.0 .and. corr(jj,kk) /= -999.0)then
                 write(997,'(5(f9.4,1x))')alat(kk),alon(jj),slope1(jj,kk),slope2(jj,kk),corr(jj,kk)
             endif
    enddo
    enddo

do jj=1,nx
    do kk=1,ny
            if(all(var11(jj,kk,1:nyr) >= 0) .and. all(var22(jj,kk,1:nyr) >= 0))then
                 write(998,'(11(f9.4,1x))')alat(kk),alon(jj),(var11(jj,kk,iyear),iyear=1,nyr)
                 write(999,'(11(f9.4,1x))')alat(kk),alon(jj),(var22(jj,kk,iyear),iyear=1,nyr)
             endif
    enddo
enddo
stop
end
