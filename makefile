all:
	python code.py
	convert info.ppm img.png

clean:
	rm *.ppm
	rm *.png
