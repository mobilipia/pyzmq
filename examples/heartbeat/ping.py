#!/usr/bin/env python
import time
import numpy
import zmq

ctx = zmq.Context()

req = ctx.socket(zmq.REQ)
req.connect('tcp://127.0.0.1:10111')

#wait for connects
time.sleep(1)
n=0
while True:
    time.sleep(numpy.random.random())
    for i in range(4):
        n+=1
        msg = 'ping %i'%n
        tic = time.time()
        req.send(msg)
        resp = req.recv()
        print msg, time.time()-tic
        assert msg == resp

