import os
import webbrowser

root_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'text_files')
webbrowser.open_new(os.path.join(root_path, 'sqlcreate.pdf'))
