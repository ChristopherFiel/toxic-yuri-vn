# Flags are here
default lily_affection = 0


#Warning splash screen
label splashscreen:
    scene black
    with Pause(1)

    show screen warning_screen with dissolve
    with Pause(5)

    hide screen warning_screen with dissolve
    with Pause(1)

    return

# The game starts here.

label start:
    # Disclaimer Screen
    scene black with dissolve
    show screen disclaimer_screen with dissolve
    pause 5
    show screen press_to_continue with dissolve
    pause
    hide screen disclaimer_screen
    hide screen press_to_continue
    with dissolve

    # Basic Controls
    scene black with dissolve
    show screen basic_controls with dissolve
    pause 5
    show screen press_to_continue with dissolve
    pause
    hide screen basic_controls
    hide screen press_to_continue
    with dissolve
    stop sound fadeout 0.5
    scene bg room

    show lily

    l "You've created a new Ren'Py game."

    l "Once you add a story, pictures, and music, you can release it to the world!"

    return
