find forms/ui/ -name '*.ui' -exec basename \{} .ui \;| xargs -I{} pyuic4 forms/ui/{}.ui -o forms/ui/{}_ui.py
