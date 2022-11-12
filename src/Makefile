new:
	playwright codegen https://www.coilcraft.com

run_python:
	py test.py

pytest_run:
	pytest -s --headed --base-url=https://www.coilcraft.com --html=report.html --self-contained-html --log-cli-level=INFO --capture=tee-sys

q:
	pytest -s --headed --base-url=https://www.coilcraft.com --html=report.html --self-contained-html --log-cli-level=INFO --capture=tee-sys --tracing=on

w:
	playwright show-trace test-results\trace.zip

z:
	pytest -s -k 'test_login_page_contents' --headed --base-url=https://www.coilcraft.com --html=report.html --self-contained-html --log-cli-level=INFO --capture=tee-sys