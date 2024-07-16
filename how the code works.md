3. **Manager**: Gets created, storing all assets and initiating mods.
4. **Mods**: Initiate their respective editors and modules.

### Methods

- **add_myself**: Most components are initiated with this method, which also returns the component itself, simplifying the coding process.

## Modules and Editors

### Modules

Modules modify the viewport and are loaded and applied simultaneously. They remain active until RWE# is closed. 

### Editors

Editors modify the viewport and interaction with it, but only one editor can be active at a time. Editors must have a UI tab for creation and can directly function with mouse movements and presses. Most functionalities in RWE# are powered by configurables.

## Configurables

Configurables are classes that can be saved and loaded between sessions, providing convenience and flexibility. They can be linked to UI elements, ensuring synchronized states. 

### Key Points

- **Instances**: Can be created anywhere, requiring only the mod for data persistence.
- **Linking**: Configurables can be linked to multiple elements, keeping values synchronized.
- **Settings UI**: Ensures values can be reset when using settings.

## Renderables

Renderables are classes for modifying the viewport, adding graphics directly. They include:

- **RenderImage**: Shows images on the viewport.
- **RenderRect**: Adds rectangles to the scene.
- **RenderLevelImage**: Similar to RenderImage but sized according to the level.

Renderables stay synchronized with the viewport's position and zoom.

## UI

The UI consists of components related to tabs, visuals, and settings. There are three classes for UI connectors:

- **UI**: For any UI, mostly editor UI.
- **ViewUI**: For visual UIs.
- **SettingUI**: Specifically for the settings menu.

## Tree Elements

Tree elements are used for settings and hotkeys menus, containing a list of other tree elements. The main classes are:

- **SettingElement**: Can have SettingUI tied to it.
- **HotkeyElement**: Can have KeyConfigurable tied to it.

## Additional Components

- **RWELevel**: Class that stores the level and history system.
- **Palettes**: Abstract class for modifying RWE#'s appearance, with the current theme being RaspberryDark.

## Notes

- **HistoryElement**: Modifies levels and can undo changes, delegating level modifications to history elements.
- **ConfigModule**: Part of the mod that stores all configurables specified for the mod.
- **Renderable Changes**: Renderables now have a `remove_graphics` method to remove graphics when the editor is changed.