# CleanQ
CleanQ (clearly a play on Clinic and a Clean Queue), aims to create a platform in which clinics can sign up to accept patients, and patients can make reservations on clinics.

#### HOW TO START:
### Commands
~~~~~~~~
git clone https://github.com/M-b850/CleanQ.git
cd CleanQ/
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
./manage.py migrate  
./manage.py makemigrations
./manage.py migrate  
./manage.py runserver
~~~~~~~~
