from .Artifact import Artifact

class WindowHistory(Artifact):
    def __init__(self, timestamp, ip_address, mac_address, annotations, tags,
    screen_res,
    window_pos,
    is_visible,
    wp_command, # windowplacement
    minimize,
    maximize,
    app_name,
    window_type,
    window_title,
    window_creation,
    window_destruction
    ):
        super().__init__(timestamp, ip_address, mac_address, annotations, tags)
        self.screen_res = screen_res
        self.window_pos = window_pos
        self.is_visible = is_visible
        self.wp_command = wp_command
        self.minimize = minimize
        self.maximize = maximize
        self.app_name = app_name
        self.window_type = window_type
        self.window_title = window_title
        self.window_creation = window_creation
        self.window_destruction = window_destruction

    def __getitem__(self, item):
        return getattr(self, item)

