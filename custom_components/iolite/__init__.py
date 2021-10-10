from homeassistant import config_entries, core

from .const import DOMAIN


async def async_setup_entry(
    hass: core.HomeAssistant, entry: config_entries.ConfigEntry
) -> bool:
    """Set up platform from a ConfigEntry."""
    # Forward the setup to the climate platform
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "climate")
    )


async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
    """Set up the component from yaml configuration."""
    hass.data.setdefault(DOMAIN, {})
    return True
