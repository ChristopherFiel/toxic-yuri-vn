transform zoom_to(target_x, target_y, zoom_level=2.0):
    xanchor target_x
    yanchor target_y
    xpos    target_x
    ypos    target_y
    zoom    zoom_level

transform pan_to(target_x, target_y, zoom_level=1.8, dur=1.0):
    linear dur xanchor target_x yanchor target_y xpos target_x ypos target_y zoom zoom_level


transform frantic_shake:
    subpixel True
    pos (0.5, 0.5) anchor (0.5, 0.5)
    zoom 1.05 
    
    block:
        choice:
            linear 0.05 xoffset 18  yoffset -12 blur 2
        choice:
            linear 0.05 xoffset -20 yoffset 15 blur 10
        choice:
            linear 0.05 xoffset 14  yoffset 20 blur 4
        choice:
            linear 0.05 xoffset -16 yoffset -18 blur 8
        choice:
            linear 0.05 xoffset 22  yoffset 10 blur 0
        choice:
            linear 0.05 xoffset -12 yoffset -22 blur 12
        repeat


transform shake_settle(t=3.0):
    subpixel True
    xoffset 20 yoffset -20 blur 10
    easeout t xoffset 0 yoffset 0 blur 0


define arrow_wipe_up    = ImageDissolve("images/wipes/arrow_up.png",    0.5, ramplen=1)
define arrow_wipe_down  = ImageDissolve("images/wipes/arrow_down.png",  0.5, ramplen=1)
define arrow_wipe_left  = ImageDissolve("images/wipes/arrow_left.png",  0.5, ramplen=1)
define arrow_wipe_right = ImageDissolve("images/wipes/arrow_right.png", 0.5, ramplen=1)

define arrow_wipe_up_fast    = ImageDissolve("images/wipes/arrow_up.png",    0.3, ramplen=1)
define arrow_wipe_down_fast  = ImageDissolve("images/wipes/arrow_down.png",  0.3, ramplen=1)
define arrow_wipe_left_fast  = ImageDissolve("images/wipes/arrow_left.png",  0.3, ramplen=1)
define arrow_wipe_right_fast = ImageDissolve("images/wipes/arrow_right.png", 0.3, ramplen=1)

define arrow_wipe_up_slow    = ImageDissolve("images/wipes/arrow_up.png",    1.0, ramplen=1)
define arrow_wipe_down_slow  = ImageDissolve("images/wipes/arrow_down.png",  1.0, ramplen=1)
define arrow_wipe_left_slow  = ImageDissolve("images/wipes/arrow_left.png",  1.0, ramplen=1)
define arrow_wipe_right_slow = ImageDissolve("images/wipes/arrow_right.png", 1.0, ramplen=1)

define fast_wipeup = CropMove(0.25, "wipeup")
define fast_wipedown  = CropMove(0.25, "wipedown")
define fast_wipeleft  = CropMove(0.25, "wipeleft")
define fast_wiperight = CropMove(0.25, "wiperight")