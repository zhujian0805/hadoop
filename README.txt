Introduction:
----------------------------------
This is a demo for running Hadoop streaming jobs. The mapper and reducer are
written by python. and this mapper script can read an external configuration
file.

usage:

hadoop jar /opt/hadoop/contrib/streaming/hadoop-streaming-1.2.1.jar -file pymap.py -mapper pymap.py -file pyreduce.py -reducer pyreduce.py -input /test01/input -output /test01/input.out -file test01.cfg

Scripts:
------------
the mapper script: pymap.py
the reducer script: pyreduce.py

The Input&Output:
------------
the input: /test01/input
the output: /test01/input.out

The configuration file read by mapper script:
------------
test01.cfg
