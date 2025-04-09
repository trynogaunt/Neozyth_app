class OptionController:
    def __init__(self, app):
        self.app = app
        self.option_service = self.load_options()

    
    def load_options(self):
        print("Loading options...")
        return {"Name": 'App'}
    
    def get_options(self):
        return self.option_service.get_options()

    def update_option(self, option_id, value):
        return self.option_service.update_option(option_id, value)
    
    def save_options(self, options):
        return self.option_service.save_options(options)