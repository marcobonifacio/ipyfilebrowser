import os
import ipywidgets as widgets
import traitlets


class FileBrowser(widgets.VBox):
    def __init__(self, path=os.getcwd(), ext=''):
        super(FileBrowser, self).__init__()
        self.add_traits(path=traitlets.Unicode(path))
        self.add_traits(ext=traitlets.Unicode(ext))
        self._update_files(self.path)
        self._update()

    @traitlets.observe('path', 'ext')
    def _update_files(self, change):
        self.files = list()
        self.dirs = list()
        if(os.path.isdir(self.path)):
            for f in os.listdir(self.path):
                ff = os.path.join(self.path, f)
                if os.path.isdir(ff):
                    self.dirs.append(f)
                else:
                    if self.ext == '':
                        self.files.append(f)
                    else:
                        if os.path.splitext(os.path.basename(f))[1] == self.ext:
                            self.files.append(f)
        self._update()

    @traitlets.validate('path')
    def _validate_path(self, proposal):
        path = proposal['value']
        if os.path.exists(path):
            return(proposal['value'])
        else:
            raise traitlets.TraitError('Non-existent path')

    @traitlets.validate('ext')
    def _validate_ext(self, proposal):
        ext = proposal['value']
        if ext == '' or ext[0] == '.':
            return(proposal['value'])
        else:
            raise traitlets.TraitError('Extension should be None or Unicode string starting with "." (dot)')

    def _update(self):

        def on_click(b):
            if b.description == '..':
                self.path = os.path.split(self.path)[0]
            else:
                self.path = os.path.join(self.path, b.description)
            self._update()

        buttons = []
        layout = widgets.Layout(width='300px')
        title = widgets.HTML('{}'.format(self.path), layout=layout)
        button = widgets.Button(description='..', style={'button_color': '#666666'},
                                tooltip=os.path.split(self.path)[0], layout=layout)
        button.on_click(on_click)
        buttons.append(button)
        for f in self.dirs:
            button = widgets.Button(description=f, style={'button_color': '#666666'},
                                    tooltip=os.path.join(self.path, f), layout=layout)
            button.on_click(on_click)
            buttons.append(button)
        for f in self.files:
            button = widgets.Button(description=f, style={'button_color': '#6a5acd'},
                                    tooltip=os.path.join(self.path, f), layout=layout)
            button.on_click(on_click)
            buttons.append(button)
        self.children = tuple([title] + buttons)
