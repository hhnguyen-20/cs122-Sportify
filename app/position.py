def center(root):
    """
    Centers elements in the home page to the center
    :param root: The app home page window
    :return: None
    """
    window_width = 1500
    window_height = 1200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)
    root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')
