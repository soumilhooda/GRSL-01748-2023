
c	---------------------------------------------------------
	real,allocatable:: sumzf(:,:,:),zmin(:),zmax(:)
     1  ,kkk(:,:),ssha(:)
	real missing,dx,dy,srad,xmin,xmax,ymin,ymax,latmin,lonmin,
     1	latmax,lonmax
	integer*2 id1,im1,iy1
	integer year(100),days(12)
c	data year/2000,2001,2002,2003,2004/
	data days/31,28,31,30,31,30,31,31,30,31,30,31/
	character*8 infile1
	character*8 infile2
	character*1 axx
	character*40 ifile,ofile
	character*2 hh
	character*10 oo
	character*4 yr
	character*13 orbit
	nc=2
	if(nc.eq.2)then
C*************************************************************************************
C	GRIDDING ROUTINE
        open(55,file='filelist1')
        do jj=1,2
        write(*,*)jj
	read(55,*)ifile
	write(*,*)ifile
        grdsiz=0.004 !!! Randhir 
	inp=1 !!!! Randhir 
	infile1='dump.dat'
        latmin=15.0
        latmax=20.0
        lonmin=77.0
        lonmax=82.0
	nx=(lonmax-lonmin)/grdsiz+1
	ny=(latmax-latmin)/grdsiz+1
	ofile=trim(ifile)//'.grd'
	ixcol=2
	iycol=1
	izcol=3
	ncol=inp+2
	missing=-999.
	dx=grdsiz
	dy=grdsiz
	allocate(sumzf(nx,ny,inp))
	allocate(zmin(inp))
	allocate(zmax(inp))
	allocate(ssha(inp))
	allocate(kkk(nx,ny))
	open(2,file=trim(ifile),status='old')
	open(22,file='dump.dat',status='unknown')
888	read(2,*,end=889)ala,alo,(ssha(i),i=1,inp)
	if(alo.le.lonmax.and.alo.ge.lonmin.and.ala.le.latmax.
     1	and.ala.ge.latmin)write(22,*)ala,alo,(ssha(i),i=1,inp)
	goto 888
889	continue	
	close(22)
	nm=2     !!!! Randhir 
	if(nm.eq.2)then
        srad=0.005    !!!! Randhir 
               	call GRD(2,lonmin,lonmax,latmin,latmax,
     1		nx,ny,ncol,ixcol,iycol,izcol,inp,infile1,dx,
     1         	dy,srad,missing,sumzf,zmin,zmax)
	elseif(nm.eq.1)then
		call XGRD(grdsiz,inp,lonmin,lonmax,latmin
     1		,latmax,nx,ny,infile1,sumzf)
	else
		write(*,*)'NOT A VALID OPTION'
		stop
	endif
	kx=0
	open(file=trim(ofile),access='direct'
     1,recl=4*nx,status='unknown',unit=20)
	itt=0
	do im=1,inp
		do j=1,ny
			itt=itt+1
			write(20,rec=itt)(sumzf(i,j,im),i=1,nx)
		enddo
	enddo
	irec=1
	write(*,29)'GRIDDED FILE',ofile,'CREATED'
29	format(a,1x,a,1x,a)
	call mkctl(ofile,nx,ny,inp,irec,lonmin,latmin,grdsiz)
	deallocate(sumzf,zmin,zmax,ssha,kkk)
	close(20)
        enddo !!!! Randhir 
C*********************************************************************
	elseif(nc.eq.1)then
	write(*,'(a,40x,a,$)')'Spatial Resolution',':'
	read(*,*)grdsiz
	write(*,'(a,17x,a,$)')
     1'Temporal Resolution (write 0 for monthly)',':'
	read(*,*)itemp
	write(*,'(a,17x,a,$)')
     1'Input Filename 				',':'
	read(*,*)ifile
	write(*,'(a,17x,a,$)')
     1'No. of Input parameters	to be averaged		',':'
	read(*,*)inp
	read(*,*)latmin,lonmin,latmax,lonmax
	read(*,*)iyy
	read(*,*)nyer
	year(1)=iyy
	if(nyer.gt.1)then
		do k=2,nyer
			year(k)=year(k-1)+1
		enddo
	endif
	if(itemp.eq.0)then
	ofile=trim(ifile)//'mon.grd'
	else
	ofile=trim(ifile)
	endif
	infile1='dump.dat'
	nx=(lonmax-lonmin)/grdsiz+1
	ny=(latmax-latmin)/grdsiz+1
	ixcol=2
	iycol=1
	izcol=3
	ncol=inp+2
	missing=-999.
	dx=grdsiz
	dy=grdsiz
	allocate(sumzf(nx,ny,inp))
	allocate(zmin(inp))
	allocate(zmax(inp))
	allocate(ssha(inp))
	allocate(kkk(nx,ny))
	open(2,file=ifile,status='old')
34	format(i4.4)
35	format(i10.10)
	jd=0
	if(itemp.eq.0)goto 72
	goto 73
72		open(24,file=trim(ofile),status='unknown',form=
     1  	'unformatted',access='direct',recl=nx)
		irec=0
		irr=0
	do it=1,nyer
		iday=0
		write(yr,34)year(it)
		if(mod(year(it),4).eq.0)then
			days(2)=29
			ndays=366
		else
			ndays=365
		endif
		imn=1
		do  ij=1,12
			irr=irr+1
			open(22,file='dump.dat',status='unknown')
			ijk=0
101			read(2,*,end=99)
     1id,im,iy,ala,alo,(ssha(i),i=1,inp)
			if(im.eq.ij.and.year(it).eq.iy)then
				if(ala.ge.latmin.and.ala.le.latmax.
     1				and.alo.le.lonmax.and.alo.ge.lonmin)then
				ijk=ijk+1
     				write(22,*)ala,alo,(ssha(i),i=1,inp)
			endif
			endif
			goto 101
99			continue
			close(22)
			rewind(2)
			if(ijk.gt.0)then
				call 
     1XGRD(grdsiz,inp,lonmin,lonmax,latmin,latmax,nx,ny,infile1
     1				,sumzf)
			else
				sumzf=-999.
				write(*,*)
     1'No points in The Year',year(it),'Month',ij,'Day',kf
			endif
			do l=1,inp
				do j=1,ny
					irec=irec+1
					write(24,rec=irec)
     1(sumzf(i,j,l),i=1,nx)
				enddo
			enddo
			write(29,*)irec,kf,ij,year(it)
			write(*,*)
			write(*,*)'**************REC='
     1,irec,ij,year(it),'***************'
908			continue
			close(8)
		enddo
c	write(*,*)it
	enddo
	write(*,29)'GRIDDED FILE ',trim(ofile),'CREATED'
	call mkctl(ofile,nx,ny,inp,irr,lonmin,latmin,grdsiz)
	goto 801
20	format(6i5,20f7.3)
73	continue
	write(*,20)
	write(*,*)
	write(*,20)
     1'3.IF YOU WANT TO RESAMPLE THE DATA FOR THE YEARS BEFORE 2000 
	1THEN YOU HAVE TO CHANGE THE'
	write(*,*)
	write(*,20)
     1'THE REFERENCE JULIAN DAY WHICH IS AT PRESENT SET 01-01-2000.'
36	format(i2.2)
		write(hh,36)itemp
		open(24,file=trim(ofile)//hh//'day.grd'
     1,status='unknown',form=
     1  	'unformatted',access='direct',recl=nx)
		jd=18261
		write(*,20)
		write(*,*)'END YEAR'
		read(*,*)iend
		write(*,20)'HOW MANY LEAP YEARS IN BETWEEN'
		read(*,*)ileap
		nyrs=iend-2000+1
		jdend=18261+nyrs*365+ileap
		irec=0
		itt=0
		itempi=0
182		continue
		it=it+1
			open(22,file='dump.dat',status='unknown')
			write(oo,35)jd
c			open(8,file='junk/'//oo//'id.dat'
c     1,status='unknown')
		if(jd.gt.jdend)goto 801
			jd1=jd+itemp
			ijk=0
121 			read(2,*,end=122)
     1id,im,iy,ala,alo,(ssha(i),i=1,inp)
			iyc=18261
			if=0
			if(iy.gt.2000)then
			kyy=iy-2000
			do iii=1,kyy
			iycount=365
			jkj=iii+2000
			if(mod(jkj,4).eq.0)iycount=366
			iyc=iyc+iycount
			enddo
			endif
				do mm=1,im-1
					if=if+days(mm)
				enddo
				ijd=id+if+iyc
				if(ijd.ge.jd.and.ijd.lt.jd1)then
				if(ala.ge.latmin.and.ala.le.
     1				latmax.and.alo.le.lonmax.and.
     1alo.ge.lonmin)then
				jdavg=(jd+jd1)/2.
				ifd=id
				ifm=im
				ify=kyy
c				write(8,8)ijd,id,im,iy,ala,alo
				ijk=ijk+1
				write(22,*)ala,alo,(ssha(i),i=1,inp)
				endif
				endif
			goto 121
122			continue
			close(22)
			rewind(2)
			if(ijk.le.0)then
c				write(*,*)
c     1'No points for the julian day',jd,jd1
				sumzf=-999.
			else
C******************** INV INTERPOLATION METHOD***********
c                        	call GRD(2,lonmin,lonmax,latmin,
c     1                  	latmax,nx,ny,ncol,ixcol,iycol,izcol,inp,infile1,dx,
c     1                  	dy,srad,missing,sumzf,zmin,zmax)
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
C*******************BOX AVG METHOD***********************
				call XGRD(grdsiz,inp,lonmin,
     1lonmax,latmin,latmax,nx,ny,infile1 
     1				,sumzf)
			endif
			itempi=itempi+1
			do l=1,inp
			do j=1,ny
			irec=irec+1
			write(24,rec=irec)(sumzf(i,j,l),i=1,nx)
			enddo
			enddo
				write(29,*)irec,kf,ij,year(it)
c				write(*,*)
				write(*,2)
     1'REC=',irec,'Center Julian Day',jdavg,'Date',
     1				ifd,'Month',ifm,'Year',ify
c				write(*,25)it,irec,jd1,jd,ifd,ifm,ify
124			continue
			close(8)
		jd=jd+itemp
		close(8)
		goto 182	
		close(24)
801	continue		
	if(itemp.ne.0)then
	ofile=trim(ofile)//hh//'day.grd'
	write(*,32)'GRIDDED FILE',trim(ofile)
32	format(a,1x,a)
	call mkctl(ofile,nx,ny,inp,itempi,lonmin,latmin,grdsiz)
	endif
	endif
100	format(2i4,20f7.3)
91	format(7(a,3x,i3,3x))
90	format(i5,2(1x,i4))
2	format(a,1x,i15,2x,a,i7,3(1x,a,i3,1x))
8	format(4i7,2f10.3)
25	format(i5,1x,3i10,3i4)
	end
	SUBROUTINE XGRD(grdsiz,inp,lonmin,lonmax,latmin,
     1	latmax,nx,ny,infile,rst1)
	real nn1(nx,ny,inp),rst1(nx,ny,inp),grd(2)
     1	,latmin,latmax,lonmin,lonmax
	character*8 infile
	real rssh(inp)
	open(1,file=infile,status='old')
c	grdsiz=0.1
c	write(*,*)grdsiz,nx,ny
	n=0
	nn1=0.
	rst1=0.
1	format(a)
4	format(i6,a,2x,a)
2	format(24x,5f10.3)
3	format(5f10.3)
8	read(1,*,end=99)(grd(j),j=1,2),(rssh(i),i=1,inp)
	n=n+1
	ii=(grd(2)-lonmin)/grdsiz+1
	jj=(grd(1)-latmin)/grdsiz+1
	do ik=1,inp
	if(rssh(ik).gt.-900.)then
	rst1(ii,jj,ik)=rst1(ii,jj,ik)+rssh(ik)
	nn1(ii,jj,ik)=nn1(ii,jj,ik)+1
	endif
	enddo
	goto 8
99	continue
	do ii=1,nx
	do jj=1,ny
	do ik=1,inp
	if(nn1(ii,jj,ik).gt.0)then
c	write(*,*)ii,jj
	fn1=(nn1(ii,jj,ik))
	rst1(ii,jj,ik)=rst1(ii,jj,ik)/fn1
	else
	rst1(ii,jj,ik)=-999.
	endif
	alat=((jj-1)*grdsiz+latmin)
	alon=((ii-1)*grdsiz+lonmin)
c	if(nn1(ii,jj,ik).ne.0)write(8,7)alon,alat,nn1(ii,jj,ik),rst1(ii,jj,ik)
800	continue
	enddo
	enddo
	enddo
	close(8)
	close(1)
	it=it+1
c	enddo
999	continue
c	write(*,*)'************************************'
c	write(*,*)'No. Of Points in X-Direction	',nx
c	write(*,*)'No. Of Points in Y-Direction	',ny
c	write(*,*)'************************************'
7	format(5f10.3)
67	format(2i6,f10.3)
	return
	end
	SUBROUTINE GRD(ifl,xmin,xmax,ymin,ymax,nx,ny,ncol,ixcol
     1  ,iycol,izcol,inp,infile,dx,dy,srad,
     1  missing,sumz,zmin,zmax)
	real gx(nx),gy(ny),sumw(nx,ny,inp),sumz(nx,ny,inp),z(inp)
     1  ,tmp(ncol),zmax(inp),zmin(inp)
	integer xcol,ycol,izcol,xminlimit,xmaxlimit,yminlimit,ymaxlimit
	real missing
	character*8 infile
	do ikk=1,inp
	zmax(ikk)=-999999999.
	zmin(ikk)=999999999.
	enddo
	write(*,1)'INSIDE SUB. WE GOT THE FOLLOWING VALUES'
	write(*,2)'Z Column No.		',izcol
	write(*,2)'Total No. Of variables. ',inp
	write(*,2)'No. Of Columns in File. ',ncol
	write(*,3)'INPUT FILE NAME.	',infile
2	format(a,10x,'=',2x,i5)
3	format(a,10x,'=',2x,a)
1	format(a)
C
C--------------------- Intiallizing The Grids---------------------
C
	do i=1,ny
	gy(i)=(i*dy)+ymin
c	gy(i)=float(i*dy)+ymin
	enddo
	do i=1,nx
	gx(i)=(i*dx)+xmin
c	gx(i)=float(i*dx)+xmin
	enddo
C
C-------- Start Griding Using Inverse Square Distance Technique----
c	ifl=2
C
	if(ifl.eq.1)then
	open(30,file=infile,status='old',form='unformatted')
	sumz=0.
	sumw=0.
	goto 34
	else
	open(30,file=infile,status='old')
	endif
	write(*,*)'CAME HERE'
	sumz=0.
	sumw=0.
33	read(30,*,end=99)(tmp(j),j=1,ncol)
	goto 109
34	read(30,end=99)(tmp(j),j=1,ncol)
109	continue
	x=tmp(ixcol)
	y=tmp(iycol)
	do ik=1,inp
	z(ik)=tmp(izcol+ik-1)
c	if(ik.eq.5)write(*,*)z(ik)
	enddo
	do ik=1,inp
	if(z(ik).lt.-900.)goto 101
	xminlimit=int((x-xmin-srad)/dx)-5
	yminlimit=int((y-ymin-srad)/dy)-5
	xmaxlimit=int((x-xmin-srad)/dx)+5
	ymaxlimit=int((y-ymin-srad)/dy)+5
	if(xminlimit.lt.0)xminlimit=0
	if(yminlimit.lt.0)yminlimit=0
	if(xmaxlimit.gt.nx)xmaxlimit=nx
	if(ymaxlimit.gt.ny)ymaxlimit=ny
	do i=xminlimit,xmaxlimit
	do j=yminlimit,ymaxlimit
	dx1=x-gx(i)
	dy1=y-gy(j)
	dist=sqrt(dx1*dx1+dy1*dy1)
c	write(*,*)dist,srad
	if(dist.lt.srad)then
c	write(*,*)sumz(i,j,ik)
	sumz(i,j,ik)=sumz(i,j,ik)+(z(ik)/(dist*dist+1.))
	sumw(i,j,ik)=sumw(i,j,ik)+(1./(dist*dist+1.))
	endif
	enddo
	enddo
101	continue
	enddo
	if(ifl.eq.1)then
	goto 34
	else
	goto 33
	endif
99	do ik=1,inp
c	write(*,*)'CAME HERE'
	do i=1,nx
	do j=1,ny
	if(sumw(i,j,ik).gt.0.)then
	sumz(i,j,ik)=sumz(i,j,ik)/sumw(i,j,ik)
	else 
	sumz(i,j,ik)=missing	
	endif
	if(sumz(i,j,ik).gt.zmax(ik).and.sumw(i,j,ik).gt.0.)
     1  zmax(ik)=max(0.0,sumz(i,j,ik))
	if(sumz(i,j,ik).lt.zmin(ik).and.sumw(i,j,ik).gt.0.)
     1  zmin(ik)=sumz(i,j,ik)
	enddo
	enddo
c	write(40,40)((sumz(i,j,inp),i=1,nx),j=1,ny)
	enddo
	close(30)
40	format(20f15.4)
	write(*,1)'Total No. Of Points In '
	write(*,21)'x-direction			:',nx
	write(*,21)'y-direction			:',ny
	write(*,22)'Min. Val Of Lon		:',xmin
	write(*,22)'Max. Val Of Lon		:',xmax
	write(*,22)'Min. Val Of Lat		:',ymin
	write(*,22)'Max. Val Of Lat		:',ymax
	write(*,22)'Min. Val Of Parameter	:',zmin(1),zmin(2)
	write(*,22)'Max. Val Of Parameter	:',zmax(1),zmax(2)
	write(*,24)'Value For Missing Data Pts	:',missing
21      format(a,3x,i5)
22      format(a,8x,':',2x,4f15.3)
24      format(a,2x,f8.3)
23      format(3f10.3)
	return
	end
	subroutine mkctl(ofile,nx,ny,inp,it,alomin,alamin,grdsiz)
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
C
C       Writing CTL and GS files for Mean Profiles
C
C
	character*20 ofile
	open(17,file='plot.ctl',status='unknown')
	alomin=alomin+(grdsiz/2.)
	alamin=alamin+(grdsiz/2.)
        write(17,32)'DSET',trim(ofile)
        write(17,1)'undef -999.'
        write(17,1)'TITLE Altimeter August'
        write(17,34)'XDEF',nx, 'LINEAR' ,alomin,grdsiz
        write(17,34)'YDEF',ny, 'LINEAR' ,alamin,grdsiz
        write(17,33)'ZDEF',1,'LINEAR 1 1'
        write(17,33)'TDEF',it,'LINEAR 01JUL0000 1DY'
        write(17,1)'VARS 3'
        write(17,1)'var1 0 99 XXXXXXXX'
        write(17,1)'var2 0 99 XXXXXXXX'
        write(17,1)'var3 0 99 XXXXXXXX'
        write(17,1)'ENDVARS'
1	format(a)
32      format(a,2x,a)
33      format(a,2x,i5,2x,a)
34	format(a,1x,i5,1x,a,1x,2f17.3)
	write(*,1)'GRADS CTL FILE "plot.ctl" CREATED'
	write(*,1)'BYE'
	return
	end
