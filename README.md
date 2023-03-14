# Save Render Presets

This addon allows the user to save render presets per engine. This allows for very easy of switchin between different render qualities and thus no more repetive actions are needed.

A new approach getting engine attributes(setting values), thanks to Daniel Engler (['Eevee-presets'](https://github.com/danielenger/Eevee-Presets/)), makes this addon work on all Blender version without a hustle.

>Please note when presets are moved between from Blender versions, errors can show due to settings not available in lower Blender version. Solution to this is exclude this setting in the preset file (adding # character in that line and save). When moving your presets to a newer version of Blender, which perhaps has newer settings in the render engine. Load that preset and then change the setting to your liking and save the preset under the same name. Below the image you can find the location of the saved presets.


!['Example UI'](https://raw.githubusercontent.com/wiki/schroef/Save-Render-Presets/images/save-render-presets-v006.png?20230314)

<b>OSX: </b>```/Users/{user}/Library/Application/Support/Blender/VERSION/scripts/presets/``` <br>
<b>Windows: </b>```C:\Documents and Settings\%username%\Application Data\Blender Foundation\Blender\VERSION\scripts\presets\``` <br>
<b>Linux: </b>```~/.config/blender/VERSION/scripts/presets/``` <br>


### System Requirements

| **OS** | **Blender** |
| ------------- | ------------- |
| OSX | Blender 2.80+ |
| Windows | Blender 2.80+ |
| Linux | Not Tested |


### Installation Process

1. Download the latest <b>[release](https://github.com/schroef/Save-Render-Presets/releases/)</b>
2. If you downloaded the zip file.
3. Open Blender.
4. Go to File -> User Preferences -> Addons.
5. At the bottom of the window, choose *Install From File*.
6. Select the file `Save-Render-Presets.zip` from your download location..
7. Activate the checkbox for the plugin that you will now find in the list.


### Changelog
[Full Changelog](CHANGELOG.md)

<!--
- Fill in data
 -
 -
-->

