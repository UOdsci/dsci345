%.slides.html : %.ipynb
	jupyter nbconvert $< --to slides

%.html : %.ipynb
	jupyter nbconvert $< --to html --execute --allow-errors
