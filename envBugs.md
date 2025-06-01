
# fixes in my env:

pip uninstall pymunk
pip install pymunk==6.6.0	

to have:
	python -c "import pymunk; print(hasattr(pymunk.Space(), 'add_collision_handler'))"
