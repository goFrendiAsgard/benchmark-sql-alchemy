# Benchmark sql-alchemy

```
(brain-py) gofrendi@kalimdor [14:40:46] [/mnt/c/Users/gofrendi/OneDrive/kata/demo-sql-alchemy] [master *]
-> % ./test-all.sh                    
 ____  _  _    ___  
|___ \| || |  / _ \ 
  __) | || |_| | | |
 / __/|__   _| |_| |
|_____|  |_|  \___/ 
                    
BENCHMARK ./test-bulk.py WITH 240 data
INSERT TIME     : 0.04342055320739746 ms
SELECT TIME     : 0.004430055618286133 ms
GET 240 DATA
0.20user 0.07system 0:00.39elapsed 71%CPU (0avgtext+0avgdata 24972maxresident)k
0inputs+0outputs (0major+6638minor)pagefaults 0swaps

BENCHMARK ./test-session-per-thread.py WITH 240 data
INSERT TIME     : 0.10987186431884766 ms
SELECT TIME     : 0.08529186248779297 ms
GET 240 DATA
0.35user 0.15system 0:00.58elapsed 88%CPU (0avgtext+0avgdata 30356maxresident)k
0inputs+0outputs (0major+8085minor)pagefaults 0swaps

BENCHMARK ./test-simple.py WITH 240 data
INSERT TIME     : 1.6558947563171387 ms
SELECT TIME     : 0.005691051483154297 ms
GET 240 DATA
0.29user 0.17system 0:02.00elapsed 23%CPU (0avgtext+0avgdata 24780maxresident)k
0inputs+0outputs (0major+6570minor)pagefaults 0swaps

 ____  _  _    ___   ___  
|___ \| || |  / _ \ / _ \ 
  __) | || |_| | | | | | |
 / __/|__   _| |_| | |_| |
|_____|  |_|  \___/ \___/ 
                          
BENCHMARK ./test-bulk.py WITH 2400 data
INSERT TIME     : 0.17936468124389648 ms
SELECT TIME     : 0.028705358505249023 ms
GET 2400 DATA
0.29user 0.10system 0:00.57elapsed 70%CPU (0avgtext+0avgdata 32132maxresident)k
0inputs+0outputs (0major+8526minor)pagefaults 0swaps

BENCHMARK ./test-session-per-thread.py WITH 2400 data
INSERT TIME     : 0.20264196395874023 ms
SELECT TIME     : 0.16060614585876465 ms
GET 2400 DATA
0.50user 0.26system 0:00.78elapsed 97%CPU (0avgtext+0avgdata 35716maxresident)k
0inputs+0outputs (0major+9408minor)pagefaults 0swaps

BENCHMARK ./test-simple.py WITH 2400 data
INSERT TIME     : 16.025902032852173 ms
SELECT TIME     : 0.04123640060424805 ms
GET 2400 DATA
1.79user 0.50system 0:16.42elapsed 13%CPU (0avgtext+0avgdata 29748maxresident)k
0inputs+0outputs (0major+7852minor)pagefaults 0swaps

 ____  _  _    ___   ___   ___  
|___ \| || |  / _ \ / _ \ / _ \ 
  __) | || |_| | | | | | | | | |
 / __/|__   _| |_| | |_| | |_| |
|_____|  |_|  \___/ \___/ \___/ 
                                
BENCHMARK ./test-bulk.py WITH 24000 data
INSERT TIME     : 1.380565881729126 ms
SELECT TIME     : 0.29285097122192383 ms
GET 24000 DATA
1.40user 0.23system 0:02.12elapsed 77%CPU (0avgtext+0avgdata 106476maxresident)k
0inputs+0outputs (0major+32887minor)pagefaults 0swaps

BENCHMARK ./test-session-per-thread.py WITH 24000 data
INSERT TIME     : 1.1467275619506836 ms
SELECT TIME     : 0.9431312084197998 ms
GET 24000 DATA
2.43user 0.54system 0:02.62elapsed 113%CPU (0avgtext+0avgdata 92740maxresident)k
0inputs+0outputs (0major+24247minor)pagefaults 0swaps

BENCHMARK ./test-simple.py WITH 24000 data
INSERT TIME     : 157.57907390594482 ms
SELECT TIME     : 0.36904144287109375 ms
GET 24000 DATA
15.79user 3.32system 2:38.37elapsed 12%CPU (0avgtext+0avgdata 81764maxresident)k
0inputs+0outputs (0major+21051minor)pagefaults 0swaps

 ____  _  _    ___   ___   ___   ___  
|___ \| || |  / _ \ / _ \ / _ \ / _ \ 
  __) | || |_| | | | | | | | | | | | |
 / __/|__   _| |_| | |_| | |_| | |_| |
|_____|  |_|  \___/ \___/ \___/ \___/ 
                                      
BENCHMARK ./test-bulk.py WITH 240000 data
INSERT TIME     : 12.614972114562988 ms
SELECT TIME     : 3.2728841304779053 ms
GET 240000 DATA
13.17user 1.79system 0:17.12elapsed 87%CPU (0avgtext+0avgdata 805124maxresident)k
0inputs+0outputs (0major+269184minor)pagefaults 0swaps

BENCHMARK ./test-session-per-thread.py WITH 240000 data
INSERT TIME     : 12.2051842212677 ms
SELECT TIME     : 9.972551584243774 ms
GET 240000 DATA
21.15user 6.29system 0:23.32elapsed 117%CPU (0avgtext+0avgdata 557344maxresident)k
0inputs+0outputs (0major+218878minor)pagefaults 0swaps

BENCHMARK ./test-simple.py WITH 240000 data
```