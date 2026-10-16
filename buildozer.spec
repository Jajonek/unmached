[app]

# (str) Title of your application
title = Unmached

# (str) Package name
package.name = voxelgame

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source directory
source.dir = .

# (list) Source files extensions to include
source.include_exts = py,png,jpg,kv,atlas,ttf,wav,ogg

# (list) Source files to exclude
source.exclude_exts = spec

# (list) List of directory to exclude
source.exclude_dirs = tests, bin, .git, .github

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,pygame

# (str) Bootstrap to use (sdl2 dla Pygame)
p4a.bootstrap = sdl2

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API supported
android.min_api = 21

# (bool) Accept Android SDK license
android.accept_sdk_license = True

# (str) Supported orientations
orientation = landscape

# (bool) Fullscreen
fullscreen = 1

[buildozer]

# (int) Log level (2 = debug with command output)
log_level = 2
