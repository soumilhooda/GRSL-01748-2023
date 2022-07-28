!-----------------------------------------------------
! gfortran  -mcmodel=large cal-slope.f90
!-----------------------------------------------------
       integer stat,points,imonth,iyear,irec,imon,ii,jj,kk,ilev,ixx
       character(len=20)         :: ofile,ofile1,ofile2,ofile3,infile,ofile4
       character(len=2)          :: id
       integer(kind=2),parameter :: nx=1251,ny=1251,nz=1,nyr=9,slon=77.002,slat=15.002,reso=0.004
       real(kind=4)              :: blight(nx,ny,nyr),alight(nx,ny)
       real(kind=4)              :: bndvi(nx,ny,nyr),andvi(nx,ny)
       real(kind=4)              :: slope1(nx,ny),slope2(nx,ny),acorr(nx,ny)
       real(kind=4)              :: alat(ny),alon(nx),x(nyr),y(nyr),aa(nyr),bb(nyr)
       real(kind=4)              :: slope,corr
!-------------------------------------------------------------
   open(11,file='ndvi2013-2021.grd',access='direct',recl=1*nx*ny)
   open(22,file='light2013-2021.grd',access='direct',recl=1*nx*ny)
   open(99,file='slope-corr.grd',access='direct',recl=1*nx*ny)
!---------------------------------------------------------------------------
! Lat/lon
!---------------------------------------------------------------------------
    do jj=1,nx
       alon(jj)   = slon + (jj-1)*reso
    enddo
       do kk=1,ny
         alat(kk) = slat + (kk-1)*reso
    enddo
!---------------------------------------------------------------------------
! Reading Data 
!---------------------------------------------------------------------------
do iyear=1,nyr
    read(11,rec=iyear)andvi
    read(22,rec=iyear)alight
      bndvi(:,:,iyear)=andvi(:,:)
      blight(:,:,iyear)=alight(:,:)
enddo
!---------------------------------------------------------------------------
!---------------------------------------------------------------------------
slope1=-999.0
slope2=-999.0
acorr=-999.0
do jj=1,nx
        do kk=1,ny
                           points=0
                            do iyear=1,nyr
                             if(bndvi(jj,kk,iyear) > 0 .and. blight(jj,kk,iyear) > 0 )then
                                points=points+1
                                aa(points)=bndvi(jj,kk,iyear)
                                bb(points)=blight(jj,kk,iyear)
                                x(points)=2012+iyear  
                              endif
                           enddo            !!! Year 
                       

                     if (points == 9)then
                            call lslope(x,aa,points,slope)
                     else
                            slope=-999.0
                     endif

                     slope1(jj,kk)=slope 
                     
                     if (points == 9)then
                            call lslope(x,bb,points,slope)
                     else
                            slope=-999.0
                     endif

                     slope2(jj,kk)=slope 

                     if (points == 9)then
                            call fit(aa,bb,points,corr)
                     else
                            corr=-999.0
                     endif

                     acorr(jj,kk)=corr 


     enddo    ! loop lat
   enddo      ! loop lon
!---------------------------------------------------------------------
! Write
!---------------------------------------------------------------------
        write(99,rec=1)slope1
        write(99,rec=2)slope2
        write(99,rec=3)acorr
!---------------------------------------------------------------------------
!---------------------------------------------------------------------------
 stop
 end
!---------------------------------------------------------------------------
!---------------------------------------------------------------------------
!---------------------------------------------------------------------------
subroutine lslope(x,y,icount,slope)
real      :: x(icount),y(icount),newvar(icount)
real      :: slope,slope1,incept,sumx,sumxx,sumy,sumxy,xmean,ymean,newvar1,xstd,ystd,slopestd,tval
integer   :: icount
sumx  = sum(x)
sumxx = sum(x*x)
sumy  = sum(y)
sumxy = sum(x*y)
xmean = sumx/float(icount)
ymean = sumy/float(icount)
slope = (sumxy-sumx*ymean)/(sumxx-sumx*xmean)
incept = ymean-slope*xmean
newvar=y-(slope*x+incept)
xstd=sqrt(sum((x(1:icount)-xmean)*(x(1:icount)-xmean))/(float(1)))       !! for this no need to devide by n
ystd=sqrt(sum((y(1:icount)-ymean)*(y(1:icount)-ymean))/(float(icount)))   
!             t Test , t=slope/SE, SE is Std error in slope
newvar1=sum((y(1:icount)-(slope*x(1:icount)+incept))*(y(1:icount)-(slope*x(1:icount)+incept)))
slopestd=(sqrt((newvar1)/(icount-2)))/(xstd)
tval=abs(slope)/slopestd
!if(tval < 2.26)then    !! 95% !! for N=9
!slope=-999
!else
slope=9*slope !! per decade
!endif
return
end
!---------------------------------------------------------------------------
!---------------------------------------------------------------------------
SUBROUTINE fit(x,y,n,corr)
integer :: n,jj
real :: x(n),y(n)
real :: xmean,ymean,cov,varx,vary,corr
xmean=sum(x)/float(n)
ymean=sum(y)/float(n)
cov=sum((x(1:n)-xmean)*(y(1:n)-ymean))
varx=sum((x(1:n)-xmean)*(x(1:n)-xmean))
vary=sum((y(1:n)-ymean)*(y(1:n)-ymean))
corr=(cov/sqrt(varx))/sqrt(vary)
if(corr  >= -1 .and. corr <= 1)then
corr=corr
else
corr=-999.0
endif
!if(abs(corr) < 0.66)corr=-999.0
return
end
!---------------------------------------------------------------------------
!---------------------------------------------------------------------------

