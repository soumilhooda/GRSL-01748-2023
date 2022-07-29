#!/bin/bash
#-----------------------------------------------------------
exec<list
while read file
do
echo $file
ofile=`expr substr $file 1 23`
echo $ofile
echo '-------------------------------------------------------------------------------'
echo 'Extract'
echo '-------------------------------------------------------------------------------'
rm -f data.bin qc.bin Time_Info.DAT
hdp dumpsds -n "500m 16 days NDVI"              -d -o data.bin -b $file
hdp dumpsds -n "500m 16 days pixel reliability" -d -o qc.bin   -b $file
mv data.bin $ofile'.val'
mv qc.bin $ofile'.qc'
echo '-------------------------------------------------------------------------------'
done
exit
#cat>Time_Info.DAT << EOF
#$year$month$bday$hr$mn
#EOF
#echo '-------------------------------------------------------------------------------'
#gfortran -o read_modisir.exe readir.f90
#./read_modisir.exe
#echo '-------------------------------------------------------------------------------'
done 
exit
