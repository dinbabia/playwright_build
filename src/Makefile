new:
	playwright codegen https://omayo.blogspot.com/search?q=sdf

new_login:
	playwright codegen https://www.saucedemo.com/

q:
	pytest -s -k 'test_select_multiple_options' --headed --base-url=https://omayo.blogspot.com/search?q=sdf --html=report.html --self-contained-html --log-cli-level=INFO --capture=tee-sys
	
w:
	pytest -s -k 'test_login_success' --headed --base-url=https://www.saucedemo.com/ --html=report.html --self-contained-html --log-cli-level=INFO --capture=tee-sys

e:
	pytest -s .\WebTestSuites\E2E\test_login.py --headed --base-url=https://www.saucedemo.com/ --html=report.html --self-contained-html --log-cli-level=INFO --capture=tee-sys

r:
	playwright show-trace test-results\trace.zip
	
t:
	pytest -s -k 'test_select_multiple_options' --headed --base-url=https://omayo.blogspot.com/search?q=sdf --html=report.html --self-contained-html --log-cli-level=INFO --capture=tee-sys --tracing=on
	