publish:
	bash client-gen.sh
	cd dungeons_and_trolls_generated_client && \
	pip3 install build twine && \
	python -m build && \
	twine upload dist/*
