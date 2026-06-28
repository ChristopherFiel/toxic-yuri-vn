screen disclaimer_screen():
    text """{font=cmunorm.ttf}{size=40}The places, events, and characters
in this game are all works of fiction.
Any similarities to real life are
purely coincidental and do not have
any correlation with the game.{/size}{/font}""":
        xalign 0.5
        yalign 0.45
        text_align 0.5
        line_leading 10


screen basic_controls():
    text """{font=cmunorm.ttf}{size=40} Basic Controls \n
    Left Click / Space / Enter — Advance dialogue \n
    Right Click / Escape — Open menu \n
    Middle Click — Hide textbox \n
    Scroll Up — Rollback \n{/size}{/font}""":
        xalign 0.5
        yalign 0.45
        text_align 0.5
        line_leading 10


screen infinite_scream():
    zorder 50
    default a_str = ""

    # cps ≈ 10
    timer 0.10 repeat True action SetScreenVariable("a_str", a_str + "A")

    python:
        _full  = "WA" + a_str + "A"
        _cpl   = 16   # characters per line — increase if text wraps too early,
        _lines = [ _full[i : i + _cpl] for i in range(0, len(_full), _cpl) ]
        _wrapped = "\n".join(_lines)

    text "{font=Midnightconstellations-YLgo.ttf}{size=160}[_wrapped]{/size}{/font}":
        xalign 0.5
        yalign 0.5
        text_align 0.5