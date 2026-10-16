[app]

# (str) Title of your application
title = Moja Gra Voxel

# (str) Package name
package.name = voxelgame

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source directory where the main file resides
source.dir = .

# (list) Source files (relative to your directory)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# Podaj tutaj wymagane biblioteki, np. python3, kivy (lub inne używane w projekcie)
requirements = python3,kivy

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (string) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
#android.api = 33

# (int) Minimum API your APK / AAB will support.
#android.minapi = 21

# (str) Android architectural build (arm64-v8a, armeabi-v7a, x86, x86_64)
android.archs = arm64-v8a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
