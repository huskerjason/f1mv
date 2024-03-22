import sys

import win32gui


def replay_live_timing():
    # the timing player can have 1 of 2 titles, try them and see if they exist
    hwnd = win32gui.FindWindow(None, 'Replay Live Timing — MultiViewer')
    if hwnd:
        win32gui.SetWindowPos(hwnd, 0, -7, -25, 1, 1200, 0)
    else:
        hwnd = win32gui.FindWindow(None, 'Live Timing — MultiViewer')
        if hwnd:
            win32gui.SetWindowPos(hwnd, 0, -7, -50, 1, 1200, 0)


def player_launch_menu(size='big'):
    # MV's menu
    def callback(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)

            if 'MultiViewer' in title:
                if any(word in title for word in ['2024', '2023', '2022', '2021', '2020', '2019', '2018', 'Home']):
                    windows.append({"title": title, "hwnd": hwnd})
            elif title == 'MultiViewer':
                windows.append({"title": title, "hwnd": hwnd})

    players = []
    win32gui.EnumWindows(callback, players)
    if players:
        hwnd = players[0]['hwnd']
        if hwnd:
            if size == 'pycharm':
                win32gui.SetWindowPos(hwnd, 0, 1300, 0, 0, 1045, 0)
            else:
                win32gui.SetWindowPos(hwnd, 0, 1024, 0, 0, 1045, 0)


def commentary(size='pycharm'):
    # 
    hwnd_f1live = win32gui.FindWindow(None, 'F1 Live — MultiViewer')
    hwnd_int = win32gui.FindWindow(None, 'International — MultiViewer')
    hwnd_pit = win32gui.FindWindow(None, 'Pit Lane — MultiViewer')

    if size in ['big']:
        if hwnd_f1live:
            win32gui.SetWindowPos(hwnd_f1live, 0, 103, 2, 1806, 1016, 0)
        elif hwnd_int:
            win32gui.SetWindowPos(hwnd_int, 0, 103, 2, 1806, 1016, 0)
        elif hwnd_pit:
            win32gui.SetWindowPos(hwnd_pit, 0, 103, 2, 1806, 1016, 0)


    elif size in ['small']:
        if hwnd_f1live:
            win32gui.SetWindowPos(hwnd_f1live, 0, 123, 1, 1280, 720, 0)
            if hwnd_int:
                win32gui.SetWindowPos(hwnd_int, 0, 475, 726, 553, 311, 0)
        elif hwnd_int:
            win32gui.SetWindowPos(hwnd_int, 0, 123, 1, 1280, 720, 0)
            if hwnd_pit:
                win32gui.SetWindowPos(hwnd_pit, 0, 129, 726, 553, 311, 0)
        elif hwnd_pit:
            win32gui.SetWindowPos(hwnd_pit, 0, 123, 1, 1280, 720, 0)


    elif size in ['pycharm']:
        if hwnd_f1live:
            win32gui.SetWindowPos(hwnd_f1live, 0, 123, 1, 270, 152, 0)
            if hwnd_int:
                win32gui.SetWindowPos(hwnd_int, 0, 395, 1, 270, 152, 0)
        elif hwnd_int:
            win32gui.SetWindowPos(hwnd_int, 0, 123, 1, 270, 152, 0)
            if hwnd_pit:
                win32gui.SetWindowPos(hwnd_pit, 0, 395, 1, 270, 152, 0)
        elif hwnd_pit:
            win32gui.SetWindowPos(hwnd_pit, 0, 123, 1, 270, 152, 0)



if __name__ == "__main__":

    if len(sys.argv) >= 2:
        replay_live_timing()
        player_launch_menu(sys.argv[1])
        commentary(sys.argv[1])
    else:
        replay_live_timing()
        player_launch_menu()
        commentary()
