# fancode-sdet-assignment

- Project is developed in Python programming language. After cloning the project, configure the python interpreter (
  Python 3.11 was used while developing)
- Pip is the tool used for requirements management, though it comes with the Python readily but if not install it
  separately
- Install requirements using command -> pip install -r requirements.txt
- Tests are written in pytest
- The test for validation completion percentage can be run using this command -> pytest .\tests\test_users.py
- If report is required then run this command -> pytest --html=\<filepath> .\tests\test_users.py  (Note: \<filepath> ->
  replace with the folder path to store the report in, and also append \report_name.html, where report_name is the name of the
  report file and can be any valid file name)
