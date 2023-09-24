publish:
	cd dungeons_and_trolls_client && \
	pip3 install build twine && \
	python -m build && \
	twine upload dist/*
