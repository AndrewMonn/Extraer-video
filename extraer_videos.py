from pathlib import Path

import shutil

directorio_actual = Path.cwd()

extensiones = ['.avi', '.mkv', '.mp4']

def mover_videos(extension, dir):

		for ext in extension:

				for archivo in dir.rglob('**/*' + ext):

						if archivo.suffix == ext and archivo.parent != dir:

								shutil.move(str(archivo), dir)

mover_videos(extensiones, directorio_actual)