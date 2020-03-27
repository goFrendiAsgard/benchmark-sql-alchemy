# Benchmark sql-alchemy

```
-> % ./test-all.sh
 ____  _  _             _ 
|___ \| || |           / |
  __) | || |_   _____  | |
 / __/|__   _| |_____| | |
|_____|  |_|           |_|
                          
BENCHMARK ./test-bulk.py WITH 24 AND 1 FIELDS
INSERT TIME     : 0.03236222267150879 ms
SELECT TIME     : 0.0021533966064453125 ms
GET 24 DATA
0.17user 0.10system 0:00.40elapsed 69%CPU (0avgtext+0avgdata 24392maxresident)k
0inputs+0outputs (0major+6489minor)pagefaults 0swaps

BENCHMARK ./test-session-per-thread.py WITH 24 AND 1 FIELDS
INSERT TIME     : 0.05413222312927246 ms
SELECT TIME     : 0.02197861671447754 ms
GET 24 DATA
0.17user 0.15system 0:00.47elapsed 69%CPU (0avgtext+0avgdata 26296maxresident)k
0inputs+0outputs (0major+6965minor)pagefaults 0swaps

BENCHMARK ./test-simple.py WITH 24 AND 1 FIELDS
INSERT TIME     : 0.18828082084655762 ms
SELECT TIME     : 0.0019059181213378906 ms
GET 24 DATA
0.10user 0.18system 0:00.54elapsed 54%CPU (0avgtext+0avgdata 24320maxresident)k
0inputs+0outputs (0major+6515minor)pagefaults 0swaps

 ____  _  _    ___            _ 
|___ \| || |  / _ \          / |
  __) | || |_| | | |  _____  | |
 / __/|__   _| |_| | |_____| | |
|_____|  |_|  \___/          |_|
                                
BENCHMARK ./test-bulk.py WITH 240 AND 1 FIELDS
INSERT TIME     : 0.04040026664733887 ms
SELECT TIME     : 0.0047457218170166016 ms
GET 240 DATA
0.15user 0.10system 0:00.39elapsed 66%CPU (0avgtext+0avgdata 24996maxresident)k
0inputs+0outputs (0major+6635minor)pagefaults 0swaps

BENCHMARK ./test-session-per-thread.py WITH 240 AND 1 FIELDS
INSERT TIME     : 0.0605776309967041 ms
SELECT TIME     : 0.03196597099304199 ms
GET 240 DATA
0.21user 0.15system 0:00.46elapsed 80%CPU (0avgtext+0avgdata 26944maxresident)k
0inputs+0outputs (0major+7147minor)pagefaults 0swaps

BENCHMARK ./test-simple.py WITH 240 AND 1 FIELDS
INSERT TIME     : 1.7545838356018066 ms
SELECT TIME     : 0.005639314651489258 ms
GET 240 DATA
0.29user 0.14system 0:02.13elapsed 20%CPU (0avgtext+0avgdata 24732maxresident)k
0inputs+0outputs (0major+6544minor)pagefaults 0swaps

 ____  _  _    ___   ___            _ 
|___ \| || |  / _ \ / _ \          / |
  __) | || |_| | | | | | |  _____  | |
 / __/|__   _| |_| | |_| | |_____| | |
|_____|  |_|  \___/ \___/          |_|
                                      
BENCHMARK ./test-bulk.py WITH 2400 AND 1 FIELDS
INSERT TIME     : 0.14381170272827148 ms
SELECT TIME     : 0.03122854232788086 ms
GET 2400 DATA
0.28user 0.12system 0:00.53elapsed 75%CPU (0avgtext+0avgdata 32252maxresident)k
0inputs+0outputs (0major+8590minor)pagefaults 0swaps

BENCHMARK ./test-session-per-thread.py WITH 2400 AND 1 FIELDS
INSERT TIME     : 0.14800620079040527 ms
SELECT TIME     : 0.1033778190612793 ms
GET 2400 DATA
0.39user 0.18system 0:00.70elapsed 81%CPU (0avgtext+0avgdata 33580maxresident)k
0inputs+0outputs (0major+8776minor)pagefaults 0swaps

BENCHMARK ./test-simple.py WITH 2400 AND 1 FIELDS
INSERT TIME     : 17.121562004089355 ms
SELECT TIME     : 0.047338008880615234 ms
GET 2400 DATA
1.93user 0.39system 0:17.53elapsed 13%CPU (0avgtext+0avgdata 29700maxresident)k
0inputs+0outputs (0major+7839minor)pagefaults 0swaps

 ____  _  _             _  ___  
|___ \| || |           / |/ _ \ 
  __) | || |_   _____  | | | | |
 / __/|__   _| |_____| | | |_| |
|_____|  |_|           |_|\___/ 
                                
BENCHMARK ./test-bulk.py WITH 24 AND 10 FIELDS
INSERT TIME     : 0.03294730186462402 ms
SELECT TIME     : 0.003318309783935547 ms
GET 24 DATA
0.14user 0.12system 0:00.40elapsed 66%CPU (0avgtext+0avgdata 24516maxresident)k
0inputs+0outputs (0major+6494minor)pagefaults 0swaps

BENCHMARK ./test-session-per-thread.py WITH 24 AND 10 FIELDS
INSERT TIME     : 0.052983999252319336 ms
SELECT TIME     : 0.0345306396484375 ms
GET 24 DATA
0.21user 0.12system 0:00.48elapsed 71%CPU (0avgtext+0avgdata 26572maxresident)k
0inputs+0outputs (0major+7079minor)pagefaults 0swaps

BENCHMARK ./test-simple.py WITH 24 AND 10 FIELDS
INSERT TIME     : 0.18550634384155273 ms
SELECT TIME     : 0.003152608871459961 ms
GET 24 DATA
0.20user 0.12system 0:00.55elapsed 59%CPU (0avgtext+0avgdata 24432maxresident)k
0inputs+0outputs (0major+6534minor)pagefaults 0swaps

 ____  _  _    ___            _  ___  
|___ \| || |  / _ \          / |/ _ \ 
  __) | || |_| | | |  _____  | | | | |
 / __/|__   _| |_| | |_____| | | |_| |
|_____|  |_|  \___/          |_|\___/ 
                                      
BENCHMARK ./test-bulk.py WITH 240 AND 10 FIELDS
INSERT TIME     : 0.04670000076293945 ms
SELECT TIME     : 0.008317947387695312 ms
GET 240 DATA
0.20user 0.10system 0:00.42elapsed 74%CPU (0avgtext+0avgdata 25880maxresident)k
0inputs+0outputs (0major+6859minor)pagefaults 0swaps

BENCHMARK ./test-session-per-thread.py WITH 240 AND 10 FIELDS
INSERT TIME     : 0.06617045402526855 ms
SELECT TIME     : 0.04489731788635254 ms
GET 240 DATA
0.26user 0.10system 0:00.57elapsed 64%CPU (0avgtext+0avgdata 27876maxresident)k
0inputs+0outputs (0major+7355minor)pagefaults 0swaps

BENCHMARK ./test-simple.py WITH 240 AND 10 FIELDS
INSERT TIME     : 1.6958844661712646 ms
SELECT TIME     : 0.008783578872680664 ms
GET 240 DATA
0.37user 0.14system 0:02.07elapsed 24%CPU (0avgtext+0avgdata 25056maxresident)k
0inputs+0outputs (0major+6665minor)pagefaults 0swaps

 ____  _  _    ___   ___            _  ___  
|___ \| || |  / _ \ / _ \          / |/ _ \ 
  __) | || |_| | | | | | |  _____  | | | | |
 / __/|__   _| |_| | |_| | |_____| | | |_| |
|_____|  |_|  \___/ \___/          |_|\___/ 
                                            
BENCHMARK ./test-bulk.py WITH 2400 AND 10 FIELDS
INSERT TIME     : 0.2728536128997803 ms
SELECT TIME     : 0.062195539474487305 ms
GET 2400 DATA
0.37user 0.14system 0:00.70elapsed 73%CPU (0avgtext+0avgdata 40356maxresident)k
0inputs+0outputs (0major+10588minor)pagefaults 0swaps

BENCHMARK ./test-session-per-thread.py WITH 2400 AND 10 FIELDS
INSERT TIME     : 0.2902538776397705 ms
SELECT TIME     : 0.13677358627319336 ms
GET 2400 DATA
0.53user 0.20system 0:00.90elapsed 81%CPU (0avgtext+0avgdata 41928maxresident)k
0inputs+0outputs (0major+10889minor)pagefaults 0swaps

BENCHMARK ./test-simple.py WITH 2400 AND 10 FIELDS
INSERT TIME     : 17.225300312042236 ms
SELECT TIME     : 0.07263016700744629 ms
GET 2400 DATA
1.96user 0.50system 0:17.66elapsed 13%CPU (0avgtext+0avgdata 31948maxresident)k
0inputs+0outputs (0major+8384minor)pagefaults 0swaps

 ____  _  _             _  ___   ___  
|___ \| || |           / |/ _ \ / _ \ 
  __) | || |_   _____  | | | | | | | |
 / __/|__   _| |_____| | | |_| | |_| |
|_____|  |_|           |_|\___/ \___/ 
                                      
BENCHMARK ./test-bulk.py WITH 24 AND 100 FIELDS
INSERT TIME     : 0.04717087745666504 ms
SELECT TIME     : 0.010123491287231445 ms
GET 24 DATA
0.12user 0.17system 0:00.42elapsed 70%CPU (0avgtext+0avgdata 26068maxresident)k
0inputs+0outputs (0major+6891minor)pagefaults 0swaps

BENCHMARK ./test-session-per-thread.py WITH 24 AND 100 FIELDS
INSERT TIME     : 0.05912971496582031 ms
SELECT TIME     : 0.09122419357299805 ms
GET 24 DATA
0.34user 0.09system 0:00.59elapsed 72%CPU (0avgtext+0avgdata 29624maxresident)k
0inputs+0outputs (0major+7867minor)pagefaults 0swaps

BENCHMARK ./test-simple.py WITH 24 AND 100 FIELDS
INSERT TIME     : 0.19969940185546875 ms
SELECT TIME     : 0.009831905364990234 ms
GET 24 DATA
0.17user 0.10system 0:00.57elapsed 48%CPU (0avgtext+0avgdata 25724maxresident)k
0inputs+0outputs (0major+6807minor)pagefaults 0swaps

 ____  _  _    ___            _  ___   ___  
|___ \| || |  / _ \          / |/ _ \ / _ \ 
  __) | || |_| | | |  _____  | | | | | | | |
 / __/|__   _| |_| | |_____| | | |_| | |_| |
|_____|  |_|  \___/          |_|\___/ \___/ 
                                            
BENCHMARK ./test-bulk.py WITH 240 AND 100 FIELDS
INSERT TIME     : 0.1831684112548828 ms
SELECT TIME     : 0.041983842849731445 ms
GET 240 DATA
0.29user 0.15system 0:00.59elapsed 75%CPU (0avgtext+0avgdata 32288maxresident)k
0inputs+0outputs (0major+8638minor)pagefaults 0swaps

BENCHMARK ./test-session-per-thread.py WITH 240 AND 100 FIELDS
INSERT TIME     : 0.17082500457763672 ms
SELECT TIME     : 0.1303415298461914 ms
GET 240 DATA
0.42user 0.20system 0:00.70elapsed 88%CPU (0avgtext+0avgdata 36032maxresident)k
0inputs+0outputs (0major+9441minor)pagefaults 0swaps

BENCHMARK ./test-simple.py WITH 240 AND 100 FIELDS
INSERT TIME     : 2.0949153900146484 ms
SELECT TIME     : 0.03718757629394531 ms
GET 240 DATA
0.53user 0.18system 0:02.50elapsed 28%CPU (0avgtext+0avgdata 28188maxresident)k
0inputs+0outputs (0major+7423minor)pagefaults 0swaps

 ____  _  _    ___   ___            _  ___   ___  
|___ \| || |  / _ \ / _ \          / |/ _ \ / _ \ 
  __) | || |_| | | | | | |  _____  | | | | | | | |
 / __/|__   _| |_| | |_| | |_____| | | |_| | |_| |
|_____|  |_|  \___/ \___/          |_|\___/ \___/ 
                                                  
BENCHMARK ./test-bulk.py WITH 2400 AND 100 FIELDS
INSERT TIME     : 1.4155569076538086 ms
SELECT TIME     : 0.34490084648132324 ms
GET 2400 DATA
1.54user 0.15system 0:02.17elapsed 78%CPU (0avgtext+0avgdata 99084maxresident)k
0inputs+0outputs (0major+25487minor)pagefaults 0swaps

BENCHMARK ./test-session-per-thread.py WITH 2400 AND 100 FIELDS
INSERT TIME     : 1.2152178287506104 ms
SELECT TIME     : 0.47725987434387207 ms
GET 2400 DATA
1.78user 0.39system 0:02.16elapsed 100%CPU (0avgtext+0avgdata 101828maxresident)k
0inputs+0outputs (0major+25962minor)pagefaults 0swaps

BENCHMARK ./test-simple.py WITH 2400 AND 100 FIELDS
INSERT TIME     : 19.115511178970337 ms
SELECT TIME     : 0.2989647388458252 ms
GET 2400 DATA
3.17user 0.25system 0:19.82elapsed 17%CPU (0avgtext+0avgdata 53980maxresident)k
0inputs+0outputs (0major+13897minor)pagefaults 0swaps

```