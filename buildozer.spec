[app]

# (str) Title of your application
title = Moja Gra Voxel

# (str) Package name
package.name = voxelgame

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source file where the main entry point of your application resides
source.dir = .

# (list) Source files to include (let it include py and other assets)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*

# (list) Source files to exclude (let's empty it)
source.exclude_exts = spec

# (list) List of directory to exclude
source.exclude_dirs = tests, bin, .git, .github

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,pygame,sdl2_image,sdl2_mixer,sdl2_ttf,sdl2

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.min_api = 21

# (str) Android NDK version to use (stabilna wersja naprawiająca błędy kompilacji)
android.ndk = 25b

# (bool) Indicate whether you accept the Android SDK license
android.accept_sdk_license = True

# (str) Supported orientations
orientation = landscape

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = Bool)
warn_on_root = 1
