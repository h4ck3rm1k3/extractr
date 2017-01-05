test :
	#python hello.py
	FLASK_DEBUG=1 PYTHONPATH=/home/mdupont/experiments FLASK_APP=hello.py python3 -m flask run --reload --debugger 
