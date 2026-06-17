chage -l test  
Last password change                                    						: Nov 03, 2023  
Password expires                                        							: never  
Password inactive                                      				 			: never  
Account expires                                         							: never  
Minimum number of days between password change          		: 0  
Maximum number of days between password change          	: 99999  
Number of days of warning before password expires       		: 7  











 -d, --lastday LAST_DAY        			set date of last password change to LAST_DAY  
  -E, --expiredate EXPIRE_DATE  		set account expiration date to EXPIRE_DATE  
  -h, --help                    					display this help message and exit  
  -i, --iso8601                 				use YYYY-MM-DD when printing dates  
  -I, --inactive INACTIVE       			set password inactive after expiration  
                                					to INACTIVE  
  -l, --list                    					show account aging information  
  -m, --mindays MIN_DAYS        		set minimum number of days before password
                                					change to MIN_DAYS  
  -M, --maxdays MAX_DAYS        		set maximum number of days before password
         											change to MAX_DAYS  
     												Passing the number -1 as MAX_DAYS will remove checking a password's  
          		 									validity.                                               
  -R, --root CHROOT_DIR         		directory to chroot into  
  -W, --warndays WARN_DAYS      	set expiration warning days to WARN_DAYS  
