# click_test
A quick command line interface proof of concept using Click

Install by creating a virtualenv in the project directory, then run:

	pip install --editable .

The executable will be venv/bin/click_test (assuming you called the
virtualenv "venv." Substitute whatever directory name you used.

Note: This is not a project of any kind. It is simply some basic test
code I used to get myself familiar with different options in the Click
framework, some of which were initially confusing to me. The examples are
highly contrived.

Also note: Need to remove directly executed methods in main file. This will
be handled by the entry point command in the setup file. Currently the entry
point just handles the non-class test cases. Again, this is all for testing
functionality only... it doesn't have to make much sense.
