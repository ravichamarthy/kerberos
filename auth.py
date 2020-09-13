#!/bin/bash
echo "kinit with hdfs.keytab for hdfs/stanford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/hdfs.keytab hdfs/stanford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL

echo "kinit with hdfs.keytab for HTTP/stanford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/hdfs.keytab HTTP/stanford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL

echo "kinit with hdfs.keytab for hive/stanford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/hdfs.keytab hive/stanford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL

echo "kinit with hdfs.keytab for hdfs/oxford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/hdfs.keytab hdfs/oxford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL

echo "kinit with hdfs.keytab for HTTP/oxford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/hdfs.keytab HTTP/oxford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL

echo "kinit with hdfs.keytab for hive/oxford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/hdfs.keytab hive/oxford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL

echo "kinit with hdfs.keytab for hdfs/yale1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/hdfs.keytab hdfs/yale1.fyre.ibm.com@HADOOPCLUSTER.LOCAL

echo "kinit with hdfs.keytab for HTTP/yale1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/hdfs.keytab HTTP/yale1.fyre.ibm.com@HADOOPCLUSTER.LOCAL

echo "kinit with hdfs.keytab for hive/yale1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/hdfs.keytab hive/yale1.fyre.ibm.com@HADOOPCLUSTER.LOCAL

echo "kinit with hdfs.keytab for hdfs/cambridge1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/hdfs.keytab hdfs/cambridge1.fyre.ibm.com@HADOOPCLUSTER.LOCAL

echo "kinit with hdfs.keytab for HTTP/cambridge1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/hdfs.keytab HTTP/cambridge1.fyre.ibm.com@HADOOPCLUSTER.LOCAL

echo "kinit with hdfs.keytab for hive/cambridge1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/hdfs.keytab hive/cambridge1.fyre.ibm.com@HADOOPCLUSTER.LOCAL


echo "kinit with yarn.keytab for yarn/stanford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/yarn.keytab yarn/stanford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL

echo "kinit with yarn.keytab for HTTP/stanford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/yarn.keytab HTTP/stanford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL

echo "kinit with yarn.keytab for yarn/cambridge1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/yarn.keytab yarn/cambridge1.fyre.ibm.com@HADOOPCLUSTER.LOCAL

echo "kinit with yarn.keytab for HTTP/cambridge1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/yarn.keytab HTTP/cambridge1.fyre.ibm.com@HADOOPCLUSTER.LOCAL

echo "kinit with yarn.keytab for yarn/oxford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/yarn.keytab yarn/oxford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL

echo "kinit with yarn.keytab for HTTP/oxford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/yarn.keytab HTTP/oxford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL

echo "kinit with yarn.keytab for yarn/yale1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/yarn.keytab yarn/yale1.fyre.ibm.com@HADOOPCLUSTER.LOCAL

echo "kinit with yarn.keytab for HTTP/yale1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/yarn.keytab HTTP/yale1.fyre.ibm.com@HADOOPCLUSTER.LOCAL


echo "kinit with mapred.keytab for mapred/yale1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/mapred.keytab mapred/yale1.fyre.ibm.com@HADOOPCLUSTER.LOCAL

echo "kinit with mapred.keytab for HTTP/yale1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/mapred.keytab HTTP/yale1.fyre.ibm.com@HADOOPCLUSTER.LOCAL

echo "kinit with mapred.keytab for mapred/cambridge1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/mapred.keytab mapred/cambridge1.fyre.ibm.com@HADOOPCLUSTER.LOCAL

echo "kinit with mapred.keytab for HTTP/cambridge1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/mapred.keytab HTTP/cambridge1.fyre.ibm.com@HADOOPCLUSTER.LOCAL

echo "kinit with mapred.keytab for mapred/stanford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/mapred.keytab mapred/stanford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL

echo "kinit with mapred.keytab for HTTP/stanford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/mapred.keytab HTTP/stanford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL

echo "kinit with mapred.keytab for mapred/oxford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/mapred.keytab mapred/oxford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL

echo "kinit with mapred.keytab for HTTP/oxford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
kinit -kt /home/hadoop/hadoop/etc/hadoop/mapred.keytab HTTP/oxford1.fyre.ibm.com@HADOOPCLUSTER.LOCAL