WINDOWS=MainWindow.py
WINDOWS+=ProgressForm.py

all: $(WINDOWS)

%.py: ../ui/%.ui
	pyside2-uic $< > $@

clean:
	rm -f $(WINDOWS)
