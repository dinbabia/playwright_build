new:
	playwright codegen https://omayo.blogspot.com/search?q=sdf

run_python:
	py test.py

pytest_run:
	pytest -s --headed --base-url=https://www.coilcraft.com --html=report.html --self-contained-html --log-cli-level=INFO --capture=tee-sys

q:
	pytest -s --headed --base-url=https://www.coilcraft.com --html=report.html --self-contained-html --log-cli-level=INFO --capture=tee-sys --tracing=on

w:
	playwright show-trace test-results\trace.zip

z:
	pytest -s -k 'test_select_multiple_options' --headed --base-url=https://omayo.blogspot.com/search?q=sdf --html=report.html --self-contained-html --log-cli-level=INFO --capture=tee-sys