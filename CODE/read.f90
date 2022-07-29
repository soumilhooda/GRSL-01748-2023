program modis_lulc
implicit none
character(len=100)     :: infile1,infile2,outfile1,outfile2
character(len=2)       :: THP,TVP
integer                :: i,j,ii,jj,kk,stat,ITHP,ITVP
integer,parameter      :: nx   = 2400
integer,parameter      :: ny   = 2400
real,parameter         :: R    = 6371007.181   !  m,the radius of the idealized sphere representing the Earth
real,parameter         :: T    = 1111950.0     !  m,the height and width of each MODIS tile in the projection plane
real,parameter         :: xmin = -20015109.0   !  m,the western limit of the projection plane;
real,parameter         :: ymax =  10007555.0   !  m,the northern limit of the projection plane;
real,parameter         :: w    =  463.31271653 !  m,the actual size of a “500-m” (T/2400) MODIS, sinusoidal grid cell.
integer(kind=2)        :: var(nx,ny)
integer(kind=1)        :: qc(nx,ny)
real(kind=4)           :: ndvi(nx,ny)
real,dimension(nx)     :: alon
real,dimension(ny)     :: alat
real                   :: xpos,ypos,HP,VP
real,dimension(18,36)  :: minlon,maxlon,minlat,maxlat
integer,dimension(18,36) ::v,h
real                     ::lon1,lon2,lat1,lat2,dx,dy,blat,blon
!----------------------------------------------------------------
!----------------------------------------------------------------
open(33,file='lat-lon.dat',status='old')
read(33,*)
do jj=1,18
   do kk=1,36
    read(33,*)v(jj,kk),h(jj,kk),minlon(jj,kk),maxlon(jj,kk),minlat(jj,kk),maxlat(jj,kk)
enddo
enddo

open(1,file='filelist',iostat=stat)
if(stat == 0)then
  do 
    read(1,*,iostat=stat)infile1
    if(stat /= 0)exit
    infile2=trim(infile1(1:23))//'.qc'
    write(*,*)infile1,infile2
                         outfile1=trim(infile1(1:23))//'.out'
                         THP=trim(infile1(19:20))
                         TVP=trim(infile1(22:23))
                         read(THP,'(I2.2)')ITHP
                         read(TVP,'(I2.2)')ITVP
                         write(*,*)ITHP,ITVP
    open(11,file=trim(infile1),access='direct',recl=2*nx*ny)
    open(22,file=trim(infile2),access='direct',recl=1*nx*ny)
    open(99,file=trim(outfile1))
    read(11,rec=1)var
    read(22,rec=1)qc
!----------------------------------------------------------------
! getting corner lat/lon of the tile
!----------------------------------------------------------------
 do jj=1,17
    do kk=1,36
      if(ITVP == v(jj,kk) .and. ITHP == h(jj,kk)) then
          lon1=minlon(jj,kk)
          lon2=maxlon(jj,kk)
          lat1=minlat(jj,kk)
          lat2=maxlat(jj,kk)
         write(*,*)jj,kk,ITVP,v(jj,kk),ITHP,h(jj,kk),minlon(jj,kk),maxlon(jj,kk),minlat(jj,kk),maxlat(jj,kk)
      endif
   enddo
enddo
!----------------------------------------------------------------
! Get lat/lon From sinusoidal Projection 
!----------------------------------------------------------------
      do jj=1,ny
        do ii=1,nx
        i=ii-1
        j=jj-1
         xpos=(j+0.5)*w+ITHP*T+xmin
         ypos=ymax-(i+0.5)*w-ITVP*T
         blat=ypos/R
         blon=xpos/(R*cos(blat))
         blat=57.2958*blat         !!! Degree
         blon=57.2958*blon         !!! Degree
!        write(666,*)i,j,xpos,ypos,57.2958*blat,57.2958*blon
        if(var(jj,ii) >= -2000 .and. var(jj,ii) <= 10000) then
        if(qc(jj,ii) <= 2 )then
        ndvi(jj,ii)=var(jj,ii)/10000.0 
        write(99,'(3(F15.6,2x),I4,2x)')blat,blon,ndvi(jj,ii),qc(jj,ii)
        endif
        endif
    enddo
enddo
!----------------------------------------------------------------
!----------------------------------------------------------------
  enddo  !!! File loop
endif

end program 
