from .message import MESSAGE_KEYBOARD as message

start_keyboard = [[message['settings_city_1'], message['settings_city_2'], message['settings_city_3']]]

menu_keyboard = [[message['start_keyb_kontroler']],
                 [message['start_keyb_settings']],
                 [message['start_keyb_info']]]

kontroler_keyboard = [[message['kontroler_keyb_clear_stop'], message['kontroler_keyb_dirty_stop']],
                      [message['kontroler_keyb_bus'], message['kontroler_keyb_trolleybus']],
                      [message['back_keyb'], message['menu_keyb']]]

kontroler_bus = [[message['back_keyb'], message['menu_keyb']]]

settings_keyboard = [[message['settings_keyb_time'], message['settings_keyb_display']],
                     [message['settings_keyb_sort'], message['settings_city']],
                     [message['back_keyb'], message['menu_keyb']]]

settings_time_keyboard = [[message['settings_keyb_time_inside_1'], message['settings_keyb_time_inside_2']],
                          [message['settings_keyb_time_inside_3'], message['settings_keyb_time_inside_4']],
                          [message['settings_keyb_time_inside_5'], message['settings_keyb_time_inside_6']],
                          [message['back_keyb'], message['menu_keyb']]]

settings_sort_keyboard = [[message['settings_keyb_sort_inside_1'], message['settings_keyb_sort_inside_2']],
                          [message['back_keyb'], message['menu_keyb']]]

settings_display_keyboard = [[message['settings_keyb_display_inside_1'], message['settings_keyb_display_inside_2']],
                             [message['back_keyb'], message['menu_keyb']]]

settings_city_keyboard = [[message['settings_city_1'], message['settings_city_2'], message['settings_city_3']],
                          [message['back_keyb'], message['menu_keyb']]]
