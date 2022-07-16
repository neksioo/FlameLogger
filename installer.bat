@echo off
MODE 80,1
title [Flame Installer] - Installing modules: discum
pip install discum
cls
title [Flame Installer] - Installing modules: ctypes
pip install ctypes
cls
title [Flame Installer] - Installing modules: json
pip install json
cls
title [Flame Installer] - Installing modules: string
pip install string
cls
title [Flame Installer] - Installing modules: random
pip install random
cls
title [Flame Installer] - Installing modules: os
pip install os
cls
title [Flame Installer] - Installing modules: datetime
pip install datetime
cls
title [Flame Installer] - Installing modules: colorama
pip install colorama
cls
title [Flame Installer] - Modules installed
timeout 2 >nul
title [Flame Installer] - Creating FlameLogger folder
mkdir FlameLogger
timeout 2 >nul
title [Flame Installer] - Created FlameLogger folder
timeout 2 >nul
title [Flame Installer] - Opening config.json file
timeout 2 >nul
start config.json
timeout 2 >nul
title [Flame Installer] - Opened config.json file
timeout 2 >nul
title [Flame Installer] - Click anything to open main.py
timeout 2 >nul
start main.py
@echo>"launcher.bat"
set file="launcher.bat"
echo @echo off> %file%
echo start main.py>> %file%
del installer.bat
