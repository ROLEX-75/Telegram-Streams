THEMES = {
    "dark_professional": {
        "name": "Dark Professional",
        "is_dark": True,
        "colors": {
            "primary": "#06B6D4",
            "secondary": "#0891B2",
            "accent": "#22D3EE",
            "background": "#0F172A",
            "card": "#1E293B",
            "border": "#334155",
            "text": "#F8FAFC",
            "text_secondary": "#A9B6C8"
        },
        "css_classes": "theme-dark-professional"
    },
    "purple_gradient": {
        "name": "Purple Gradient",
        "is_dark": False,
        "colors": {
            "primary": "#9333EA",
            "secondary": "#7C3AED",
            "accent": "#A855F7",
            "background": "#F6F4FB",
            "card": "#FFFFFF",
            "border": "#E2DCF0",
            "text": "#1E1B2E",
            "text_secondary": "#5B5470"
        },
        "css_classes": "theme-purple-gradient"
    },
    "blue_navy": {
        "name": "Navy Blue",
        "is_dark": False,
        "colors": {
            "primary": "#2563EB",
            "secondary": "#1E3A8A",
            "accent": "#3B82F6",
            "background": "#F1F5F9",
            "card": "#FFFFFF",
            "border": "#CBD5E1",
            "text": "#1E293B",
            "text_secondary": "#475569"
        },
        "css_classes": "theme-blue-navy"
    },
    "cyber_neon": {
        "name": "Cyber Neon",
        "is_dark": True,
        "colors": {
            "primary": "#22D3EE",
            "secondary": "#E935E9",
            "accent": "#34F5A0",
            "background": "#070A18",
            "card": "#10152E",
            "border": "#27305A",
            "text": "#F2F5FF",
            "text_secondary": "#A4AFD0"
        },
        "css_classes": "theme-cyber-neon"
    },
    "midnight_carbon": {
        "name": "Midnight Carbon",
        "is_dark": True,
        "colors": {
            "primary": "#3B82F6",
            "secondary": "#1D4ED8",
            "accent": "#60A5FA",
            "background": "#030712",
            "card": "#111827",
            "border": "#283443",
            "text": "#F9FAFB",
            "text_secondary": "#AEB7C4"
        },
        "css_classes": "theme-midnight-carbon"
    },
    "ocean_mint": {
        "name": "Ocean Mint",
        "is_dark": False,
        "colors": {
            "primary": "#059669",
            "secondary": "#047857",
            "accent": "#0891B2",
            "background": "#F0FDF4",
            "card": "#FFFFFF",
            "border": "#C9EBD6",
            "text": "#064E3B",
            "text_secondary": "#3F5750"
        },
        "css_classes": "theme-ocean-mint"
    },

    "sunset_warm": {
        "name": "Sunset Warm",
        "is_dark": False,
        "colors": {
            "primary": "#EA580C",
            "secondary": "#DC2626",
            "accent": "#DB2777",
            "background": "#FFFBEB",
            "card": "#FFFFFF",
            "border": "#F5E4C3",
            "text": "#451A03",
            "text_secondary": "#7C3A12"
        },
        "css_classes": "theme-sunset-warm"
    },
    "forest_earth": {
        "name": "Forest Earth",
        "is_dark": False,
        "colors": {
            "primary": "#166534",
            "secondary": "#14532D",
            "accent": "#4D7C4F",
            "background": "#F7F7F2",
            "card": "#FFFFFF",
            "border": "#E0E2DA",
            "text": "#14532D",
            "text_secondary": "#4B5043"
        },
        "css_classes": "theme-forest-earth"
    }
}

def get_theme(theme_name: str = "dark_professional"):
    """Returns the dictionary for the requested theme or the default."""
    return THEMES.get(theme_name, THEMES["dark_professional"])

def get_all_themes():
    """Returns all available theme configurations."""
    return THEMES
