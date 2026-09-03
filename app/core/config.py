from dataclasses import dataclass

@dataclass
class Config:
    app_name: str = "MiniPlatform"
    debug: bool = False