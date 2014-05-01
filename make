find forms/ui/ -name '*.ui' -exec basename \{} .ui \;| xargs -I{} pyside-uic forms/ui/{}.ui -o forms/ui/{}_ui.py
